# Checks — publish

The last gate before anything reaches a live account. Run every one **before** the
vendor call, and write the evidence report into the packet.
Contract: `${CLAUDE_PLUGIN_ROOT}/shared/proof.md`.

Most of these are blocking, which is correct here and nowhere else: this is the one
skill whose mistakes are visible to her customers and cannot be taken back.

---

### 1 · The packet was approved
**Tier:** blocking
**Evidence:** the packet's approval field — her approval word, her wording, and the
date
**Fails when:** no approval is recorded, or the recorded approval names a different
post
**Report as:** the approval line, or `no approval recorded`

The approval must exist **in the packet**, not only in the conversation. A packet
that is only approved in chat is approved nowhere tomorrow (`the-law.md`, Law 3).

### 2 · It came from Approved, not Drafts
**Tier:** blocking
**Evidence:** the packet's current parent folder
**Fails when:** the packet is in `1 Ideas/` or `2 Drafts/`
**Report as:** the folder it was found in

The folders are the visible half of the approval gate. Publishing from Drafts makes
that gate a decoration.

### 3 · The draft-post checks passed
**Tier:** blocking
**Evidence:** the evidence report already in the packet
**Fails when:** the report is missing, or holds an unresolved blocking failure with
no recorded override
**Report as:** the report's timestamp and its blocking count

This is what stops a blocking check being escaped by going around the skill that
runs it.

### 4 · Media validates
**Tier:** blocking
**Evidence:** the publisher's media validation response for every media item
**Fails when:** any item returns invalid, or exceeds a platform limit
**Report as:** per item — content type, size, and the per-platform verdict

**Validate after upload, never before.** A presigned URL returns 404 until the bytes
are actually there, so a pre-upload check fails for the wrong reason and teaches
everyone to ignore it.

### 5 · Publish-now is only ever explicit
**Tier:** blocking
**Evidence:** the conversation, and the scheduling fields being sent
**Fails when:** an immediate publish is about to be sent and she did not literally
ask for this post to go out now
**Report as:** `scheduled for <local time>` or `publish now — she said: "<her words>"`

### 6 · Scheduled time is sane
**Tier:** needs-a-look
**Evidence:** the scheduled timestamp, converted to her timezone from `0 — Map`
**Fails when:** the time is in the past, more than 30 days out, or between 11pm and
6am her time
**Report as:** the local time and day

### 7 · Daily quota
**Tier:** needs-a-look
**Evidence:** the platform's remaining publish quota for this account
**Fails when:** this post would exceed it, or the remaining quota is unknown
**Report as:** `used 3 of 100 today`

### 8 · Accounts can post
**Tier:** blocking
**Evidence:** account health for every target account
**Fails when:** any target reports it cannot post, or needs reconnecting
**Report as:** per account — the platform and its state

A scheduled post on a disconnected account fails silently, days later, with nobody
watching.

### 9 · The packet id travels
**Tier:** informational
**Evidence:** the vendor payload's metadata
**Fails when:** the packet's Drive id is not attached to the scheduled post
**Report as:** the id sent

This is how `learn` pairs real performance back to the post that produced it. Miss
it and the weekly loop has numbers with nothing to attribute them to.

---

## After it goes out

Two more, run once the vendor confirms:

### 10 · The URL is real
**Tier:** needs-a-look
**Evidence:** an HTTP request to the returned post URL
**Fails when:** it does not resolve, or returns anything other than success
**Report as:** the URL and its status

### 11 · The packet records what happened
**Tier:** needs-a-look
**Evidence:** the packet in `4 Published/`
**Fails when:** it is missing the live URL, the publish time, or the platform
**Report as:** what was written

A published post whose packet does not say so is a post the weekly report cannot
see, and a post nobody can trace when a claim in it is later questioned.
