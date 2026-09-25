from __future__ import annotations

from .content_extractor import ContentExtractor
from .ethics import EthicsEvaluator
from .schemas import GateResult, SceneDocument


class ASKVPhase1:
    def __init__(self, ethics: EthicsEvaluator | None = None):
        self.ethics = ethics or EthicsEvaluator()
        self.extractor = ContentExtractor()

    def run(self, text: str) -> tuple[GateResult, SceneDocument | None]:
        input_gate = self.ethics.evaluate(text, "input")
        if not input_gate.decision.passed:
            return input_gate, None

        scene_document = self.extractor.extract(text)

        # Gate structured output as well; later phases will gate every handoff.
        output_gate = self.ethics.evaluate(
            scene_document.model_dump_json(),
            "content_extractor_output",
        )
        if not output_gate.decision.passed:
            return output_gate, None

        return output_gate, scene_document
