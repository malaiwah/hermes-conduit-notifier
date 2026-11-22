<!-- claude-projects-attribution: {"github_login":"malaiwah"} -->
_Requested by **Michel** · [project thread](https://claude.ai/code/project/chan_015j3KQQsfFnaJqrgBWyczeJ?thread=cmsg_015j3KQQsfFnaJqrgBWyczeJUJwJnV59Piq8vMtLajMM1d)_

## Summary

Muted chats: the user mutes one chat in Conduit for 15 minutes, an hour, a day or until unmuted, and the plugin skips that chat's pushes.

- `chat_mute.py` (new, standalone like `cron_store.py`): the profile's `conduit-muted-chats.json`, one entry per chat (its ids, when the mute ends or null, when it was set), file-locked writes, 0600, ended mutes dropped on the next write, at most 200 chats, a timed mute at most a year. A file that can't be read mutes nothing, so a fault can only let a push through.
- `GET/PUT /notifications/muted-chats` in `dashboard/api/notifications.py`, capability `chat-mute`. PUT takes `session_ids` (up to 16, as `/notifications/on-screen`) and `mute_s` (seconds, `null` for until unmuted, `0` to unmute); answers list each chat's `session_ids`, `until` and `remaining_s`, so the phone counts down on its own clock.
- `__init__.py` `_chat_muted`: skips the reply push, the failed-turn push and its automatic alert call, and a finished background task's push for a muted chat, and for a chat that continues one through compaction (the lineage is read from `state.db`; a branch is a new chat). Approvals, questions, calls and Pulse still notify. The session store is only read when something is muted.
- Version 0.193.0 with its changelog entry; `upstream/contract.yml` regenerated for the new route.

## Siblings

Entry: Notifications in hermes-conduit (updated in the app PR, link below).
- Reply, failed turn, background task: done, skipped while muted.
- Approval, question, call, Pulse: not needed, they wait on the user, so they still notify (kept on purpose).
- Scheduled jobs: not needed, they keep their own per-job switch.
- The relay and its plain copy: not needed, the plugin never sends the push.
- The app's menu, row bell and translations: done in the app PR.

## Desktop

Follow-up: the Notifications entry's Open gaps records that the desktop has no menu for it yet; the host's mute already covers the pushes it would get.

## Testing

- `tests/test_chat_mute.py` (new): timed mute ends, until unmuted and unmute, re-mute replaces, trimming, bad bodies, unreadable or edited files, routes.
- `tests/test_turn_end_pushes.py`: a muted chat sends no reply, failure or alert call and another chat still does; unmuted it notifies again; muted after compaction, not in a branch.
- `tests/test_capabilities.py`: `chat-mute` maps to its route.
- Whole plugin suite (without the persona suite): 8,427 passed, 15 skipped.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01AMQtiNthaezPFPoDkFqsvx
