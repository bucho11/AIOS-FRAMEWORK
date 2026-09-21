#!/usr/bin/env bash
# Read-only Zernio verification. Publishes NOTHING.
# Usage:  ZERNIO_API_KEY=sk_... ./tools/verify-zernio.sh
# Closes: OQ-009 (does the connection work), plus the live IG quota value.
set -uo pipefail
K="${ZERNIO_API_KEY:-}"
[ -z "$K" ] && { echo "✗ ZERNIO_API_KEY not set"; exit 1; }
A="https://zernio.com/api/v1"
h=(-H "Authorization: Bearer $K" -H "Content-Type: application/json")
j() { python3 -c "import sys,json;d=json.load(sys.stdin);print(json.dumps(d,indent=2)[:1200])" 2>/dev/null || cat; }

echo "════ 1. AUTH — list profiles ════"
curl -sS --max-time 30 "${h[@]}" "$A/profiles" | j

echo; echo "════ 2. ACCOUNTS — what is connected ════"
ACC=$(curl -sS --max-time 30 "${h[@]}" "$A/accounts")
echo "$ACC" | python3 -c "
import sys,json
d=json.load(sys.stdin)
a=d.get('accounts',d if isinstance(d,list) else [])
print(f'{len(a)} account(s)')
for x in a:
    print(f\"  platform={x.get('platform')} user={x.get('username')} id={x.get('_id') or x.get('id')} active={x.get('isActive')} profile={x.get('profileId')}\")
" 2>/dev/null || echo "$ACC" | head -c 600

echo; echo "════ 3. HEALTH — can it post? ════"
curl -sS --max-time 30 "${h[@]}" "$A/accounts/health" | python3 -c "
import sys,json
d=json.load(sys.stdin)
s=d.get('summary',{})
print('summary:',json.dumps(s))
for x in d.get('accounts',[]):
    print(f\"  {x.get('platform'):10s} {x.get('username','?'):20s} status={x.get('status')} canPost={x.get('canPost')} analytics={x.get('canFetchAnalytics')}\")
" 2>/dev/null || echo "  (unparsed)"

echo; echo "════ 4. INSTAGRAM QUOTA — live quotaTotal ════"
IG=$(echo "$ACC" | python3 -c "
import sys,json
d=json.load(sys.stdin)
for x in d.get('accounts',[]):
    if x.get('platform')=='instagram': print(x.get('_id') or x.get('id')); break
" 2>/dev/null)
if [ -n "$IG" ]; then
  curl -sS --max-time 30 "${h[@]}" "$A/accounts/$IG/instagram/publishing-limit" | j
else
  echo "  no instagram account found — skipping"
fi

echo; echo "════ 5. MEDIA PRESIGN — does it return a publicUrl? ════"
PR=$(curl -sS --max-time 30 "${h[@]}" -X POST "$A/media/presign" \
  -d '{"filename":"verify-test.jpg","contentType":"image/jpeg"}')
echo "$PR" | python3 -c "
import sys,json
d=json.load(sys.stdin)
pu=d.get('publicUrl'); print('publicUrl :',pu)
print('expiresIn :',d.get('expiresIn'),'s')
print('uploadUrl :', (d.get('uploadUrl') or '')[:70]+'…')
open('/tmp/_zernio_publicurl','w').write(pu or '')
" 2>/dev/null || echo "$PR" | head -c 400

echo; echo "════ 6. VALIDATE MEDIA — the tool publish uses ════"
PU=$(cat /tmp/_zernio_publicurl 2>/dev/null)
if [ -n "$PU" ]; then
  curl -sS --max-time 30 "${h[@]}" -X POST "$A/tools/validate/media" -d "{\"url\":\"$PU\"}" | j
else echo "  skipped"; fi

echo; echo "════ 7. MCP tools/list (authenticated) ════"
curl -sS --max-time 40 https://mcp.zernio.com/mcp -X POST \
 -H "Authorization: Bearer $K" -H "Content-Type: application/json" \
 -H "Accept: application/json, text/event-stream" \
 -d '{"jsonrpc":"2.0","method":"tools/list","id":1}' 2>&1 | sed 's/^data: //' | python3 -c "
import sys,json
raw=sys.stdin.read()
ln=[l for l in raw.splitlines() if l.strip().startswith('{')]
if not ln: print('  RAW:',raw[:300]); raise SystemExit
d=json.loads(ln[0])
if 'error' in d: print('  ERROR:',json.dumps(d['error'])[:200]); raise SystemExit
ts=d.get('result',{}).get('tools',[])
print(f'  {len(ts)} tools')
for t in ts[:60]: print('   ',t['name'])
" 2>/dev/null || echo "  (unparsed)"

echo; echo "════ DONE — nothing was published ════"
