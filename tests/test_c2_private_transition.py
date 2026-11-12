import json
from test_location import *  # noqa: F401,F403
from test_location import PLACES, fix, _shared, _call, location, DEVICE, NOW


def test_making_a_place_private_hides_its_retained_fix_and_visits(home):
    store, phone = _shared(home, fix=fix(place_id="p_home"),
                           events=[{"id": "e_home", "kind": "arrive", "place_id": "p_home",
                                    "at": "2026-10-13T06:50:00+01:00"}])
    # The user marks Home private; the app sends a settings-only batch.
    private = [{**PLACES[0], "private": True}, PLACES[1], PLACES[2]]
    store.ingest(phone.seal(phone.batch(places=private)))
    answer = _call({"action": "now"}, session_id="s")
    print("now:", json.dumps(answer))
    rows, _ = store.history(DEVICE, 0, NOW + 1, 10)
    print("history:", rows)
    assert answer.get("at_saved_place") == "a private place"
    assert "coordinates" not in answer and "area" not in answer
    assert rows == []
