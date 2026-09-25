# ASKV — Technical Project Report

**Date:** 25 September 2026

## Abstract

ASKV is a governed multi-agent research pipeline for transforming text or image prompts into cinematic media. The system decomposes the task into typed creative stages including content extraction, narrative planning, screenplay generation, visual direction, 3D scene construction, camera planning, audio generation, editing and quality refinement. A separate safety plane evaluates inputs and intermediate artifacts, while an evolutionary critic can iteratively refine outputs.

The project is divided into an open-model systems phase and an experimental custom-model phase. The first phase prioritizes reproducible engineering and measurement. The custom-model phase is conditional on evidence that replacing individual components provides measurable benefit.

## Objectives

1. Build a reproducible end-to-end prototype.
2. Establish typed interfaces between creative agents.
3. Enforce safety checks at input, handoff and output boundaries.
4. Measure cinematic quality rather than relying on subjective claims.
5. Compare multi-agent and simpler baselines.
6. Publish reproducible methods, evaluation data and limitations where licensing permits.

## Architecture

The architecture consists of:
- orchestration layer
- agent layer
- safety/policy plane
- artifact/provenance store
- evaluation layer
- compute scheduler
- presentation layer

The safety plane is independent of the creative agents. Each artifact carries provenance metadata and must pass schema and policy validation before downstream use.

## Revised contribution claims

The project should avoid unsupported "first" claims until a systematic literature review establishes them. A safer research claim is:

> ASKV investigates a governed multi-agent architecture that combines structured cinematic planning, programmatic 3D scene generation, repeated safety evaluation and iterative quality optimization.

Novelty should be demonstrated experimentally through ablations and comparisons.

## Milestones

### Phase 1
Typed contracts, safety gate, deterministic extractor, test suite.

### Phase 2
Narrative and screenplay generation plus visual references.

### Phase 3
Blender scene construction and camera planning.

### Phase 4
Dialogue, music, foley and ambience.

### Phase 5
Editing, evaluation, critic and end-to-end demonstration.

### Phase 6
Selective fine-tuning/customization only where experiments show a meaningful gain.

## Success criteria

A successful Phase-5 prototype should demonstrate:
- one prompt produces a reproducible multi-scene artifact
- every handoff is logged and validated
- safety decisions are auditable
- failed generations can be retried without corrupting state
- quantitative evaluation exists for quality and safety
- the complete run can be reproduced from a recorded manifest
