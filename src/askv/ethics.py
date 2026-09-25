from __future__ import annotations

import re

from .schemas import GateResult, SafetyDecision

# This baseline is deliberately conservative and is NOT a substitute for a
# production safety model. The adapter boundary allows Llama Guard to replace
# it without changing downstream contracts.
DEFAULT_PATTERNS = {
    "sexual_content": re.compile(r"\b(nude|nudity|porn|explicit sex)\b", re.I),
    "child_exploitation": re.compile(r"\b(child sexual|csam|child exploitation)\b", re.I),
    "terrorism": re.compile(r"\b(terrorist recruitment|terrorist propaganda)\b", re.I),
    "self_harm": re.compile(r"\b(suicide instructions|self-harm instructions)\b", re.I),
}


class EthicsEvaluator:
    def __init__(self, patterns: dict[str, re.Pattern[str]] | None = None):
        self.patterns = patterns or DEFAULT_PATTERNS

    def evaluate(self, content: str, stage: str) -> GateResult:
        matches = [name for name, pattern in self.patterns.items() if pattern.search(content)]
        if matches:
            decision = SafetyDecision(
                passed=False,
                categories=matches,
                reason=f"Blocked by baseline policy at {stage}.",
                confidence=0.95,
            )
            return GateResult(decision=decision, blocked_stage=stage)

        return GateResult(
            decision=SafetyDecision(
                passed=True,
                reason="No baseline policy trigger detected.",
                confidence=0.50,
            )
        )
