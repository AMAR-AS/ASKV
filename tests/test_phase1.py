from askv.pipeline import ASKVPhase1


def test_safe_text_reaches_scene_json():
    gate, document = ASKVPhase1().run(
        "A scientist enters a quiet laboratory at dawn."
    )
    assert gate.decision.passed
    assert document is not None
    assert document.scenes[0].location == "laboratory"


def test_blocked_text_does_not_reach_extractor_output():
    gate, document = ASKVPhase1().run(
        "A character creates terrorist propaganda for recruitment."
    )
    assert not gate.decision.passed
    assert document is None


def test_empty_text_is_rejected():
    try:
        ASKVPhase1().run("   ")
    except ValueError:
        return
    raise AssertionError("Empty input should be rejected")
