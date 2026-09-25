from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


class Character(BaseModel):
    name: str
    description: str = ""


class Scene(BaseModel):
    scene_id: str
    location: str
    time_of_day: str = "unspecified"
    description: str
    characters: list[Character] = Field(default_factory=list)
    mood: str = "neutral"


class SceneDocument(BaseModel):
    title: str = "Untitled"
    source_type: Literal["text", "image"] = "text"
    scenes: list[Scene] = Field(min_length=1)


class SafetyDecision(BaseModel):
    passed: bool
    categories: list[str] = Field(default_factory=list)
    reason: str = ""
    confidence: float = Field(default=0.0, ge=0.0, le=1.0)
    policy_version: str = "askv-phase1-v1"


class GateResult(BaseModel):
    decision: SafetyDecision
    blocked_stage: str | None = None
