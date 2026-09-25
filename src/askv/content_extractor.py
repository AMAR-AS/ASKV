from __future__ import annotations

import re

from .schemas import Character, Scene, SceneDocument


class ContentExtractor:
    """Phase-1 deterministic extractor.

    The production implementation will use a VLM/NLP adapter. Keeping this
    deterministic baseline makes the pipeline testable without model weights.
    """

    def extract(self, text: str) -> SceneDocument:
        cleaned = " ".join(text.split())
        if not cleaned:
            raise ValueError("Input text must not be empty.")

        location = self._location(cleaned)
        mood = self._mood(cleaned)
        character_names = re.findall(r"\b(?:a|an|the)\s+([A-Z][a-z]+)\b", cleaned)
        characters = [Character(name=name) for name in dict.fromkeys(character_names)]

        scene = Scene(
            scene_id="scene_001",
            location=location,
            description=cleaned,
            characters=characters,
            mood=mood,
        )
        return SceneDocument(title="ASKV Draft", source_type="text", scenes=[scene])

    @staticmethod
    def _location(text: str) -> str:
        locations = {
            "laboratory": "laboratory",
            "forest": "forest",
            "city": "city",
            "street": "street",
            "house": "house",
            "office": "office",
            "beach": "beach",
            "school": "school",
        }
        lowered = text.lower()
        for key, value in locations.items():
            if key in lowered:
                return value
        return "unspecified"

    @staticmethod
    def _mood(text: str) -> str:
        lowered = text.lower()
        for key, mood in {
            "dark": "dark",
            "quiet": "calm",
            "peaceful": "calm",
            "tense": "tense",
            "mysterious": "mysterious",
            "joyful": "joyful",
        }.items():
            if key in lowered:
                return mood
        return "neutral"
