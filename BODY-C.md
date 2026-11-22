<!-- claude-projects-attribution: {"github_login":"malaiwah"} -->
_Requested by **Michel** · [project thread](https://claude.ai/code/project/chan_015j3KQQsfFnaJqrgBWyczeJ?thread=cmsg_015j3KQQsfFnaJqrgBWyczeJAXPsGFhgUKs3DJxvozJzut)_

## Summary

A missing Conduit push couldn't be traced from the gateway log: only failures were logged, by event type alone, so nothing showed whether the relay took an event, how long it queued, or which retry lines belonged to it. Supersedes malaiwah/hermes-conduit-notifier#3.

- `client.py`: every push line names its event as `type #digest` (10 hex of a sha256 of the event id; never the id itself, which can be an unkeyed digest of hook data, nor content). Retries say their try; a final failure says tries, time queued and time sending. Each event the relay takes logs one line with what it did: delivered, a duplicate, or a WARNING when it chose not to push.
- `live_activity.py`: a relay outage logs one WARNING when it starts and one INFO line when updates get through again, with the count and how long; the failures between go to DEBUG instead of one INFO line every few seconds.
- dashboard: `get_session_messages` is called only with the flags this Hermes takes (`core.supported_flags`, logged once per missing flag). A Hermes without `inline_images` answered every chat history page with a TypeError (157 times in two days on one host).

## Siblings

No user-facing or model-facing text changes: log lines only, plus history on an older Hermes now answering instead of failing (Chat history keeps its behavior on current Hermes). No feature map entry changes.

## Desktop

Not needed: host-side logging and a compatibility fix for older Hermes; the desktop reads the same history route, which now answers on older Hermes too.

## Testing

- `tests/test_delivery.py`, `tests/test_live_activity.py`, `tests/test_history_page.py`, new `tests/test_supported_flags.py`: 141 targeted tests pass; `test_api_layout.py` passes too.
- Full plugin suite: the same failures as main, none new.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01AMQtiNthaezPFPoDkFqsvx
