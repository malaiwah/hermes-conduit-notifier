<!-- claude-projects-attribution: {"github_login":"malaiwah"} -->
_Requested by **Michel** · [project thread](https://claude.ai/code/project/chan_015j3KQQsfFnaJqrgBWyczeJ?thread=cmsg_015j3KQQsfFnaJqrgBWyczeJUJwJnV59Piq8vMtLajMM1d)_

## Summary

Mute a chat's notifications from its menu: **For 15 Minutes, For 1 Hour, For 1 Day, Until I Unmute**. A muted chat shows a crossed-out bell on its Chats row, and its menu offers **Unmute** (with the time it ends, for a timed mute). Shown only with a plugin that reports `chat-mute` (notifier 0.193.0, the companion notifier PR "Muted chats", branch `claude/mute-chat-notifications`).

The plugin keeps the mute and skips the pushes itself, so it holds on every paired device and for sealed pushes; a compaction of the chat stays muted. Approvals, questions, calls and Pulse still notify.

- `Conduit/Models/ChatMutes.swift`: the mutes per dashboard and profile, kept under the chat's ids as Done marks are (lineage root first); the durations, the route's body and answer (read with `remaining_s` against this device's clock).
- `Conduit/Services/AppState+ChatMute.swift`: read with the list (alongside Done marks, at most every 30 s), set at once from the menu, one write at a time per profile, a read from before a write dropped, an error shown on failure.
- `SidebarView.swift` `ChatMuteMenu` in every row's menu; `V2SessionRow` draws the bell (and says "Notifications muted" to VoiceOver).
- 9 strings in `Chat.xcstrings`, translated in all 13 shipped languages.

## Siblings

Entry: Notifications (updated: siblings, code, a ruling, open gaps, Checked).
- Reply, failed turn, background task: done in the notifier PR (skipped while muted).
- Approval, question, call, Pulse: not needed, they wait on the user.
- Scheduled jobs: not needed, they keep their own switch.
- Settings > Notifications: gap left open (no list of muted chats yet); recorded in Open gaps.
- A Mute action on the notification itself: gap left open, recorded.
- The Watch: its pushes are covered by the host's mute; no menu there, recorded.
- Project pages and search rows: no bell yet, recorded.

## Desktop

Follow-up: the Notifications entry's Open gaps records that the desktop has no menu for it; the host's mute already covers its pushes.

## Testing

- Built the Conduit scheme for an iPhone 17 Pro simulator (iOS 27.0, Xcode 27.2): no errors.
- `SidebarLayoutTests`, including the new `testChatMutesFollowTheConversationAndEnd`: 144 of 145 passed. The one failure, `testChatsListReRunLeavesUnchangedRowsAlone`, also fails on main without this change (run twice on c579d98).
- `NotificationCopyTests`: 25 of 25.
- `check-l10n-coverage`: OK. `check-feature-map`: OK except `notifier/chat_mute.py`, which lands with the notifier PR.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01AMQtiNthaezPFPoDkFqsvx
