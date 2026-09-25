# ASKV — Master Project Plan

**Updated:** 25 September 2026  
**Repository:** AMAR-AS/ASKV

## Vision

ASKV is a structured, multi-agent, safety-governed cinematic generation framework that transforms text or image input into controllable 3D cinematic artifacts through a persistent intermediate representation, automated evaluation, and iterative refinement.

Immediate vertical slice:

Text → Safety Gate → Planner → ASKV-IR → Story/Screenplay → Blender → Camera → Render → Critic → Final Safety → 10-second cinematic output

## 1. Core Architecture

ASKV uses a central orchestrator and modular specialized components:

1. ASKV Guard — safety policy enforcement and content transformation.
2. Planner Agent — story/world/character planning.
3. Screenplay Agent — scene structure and dialogue.
4. Visual Director — visual style, environments, characters.
5. 3D Director / Blender Agent — Blender scene construction.
6. Cinematography Agent — camera, lighting, shot composition and movement.
7. Audio Director — dialogue, music, Foley and ambience.
8. Editor — assembly, timing and export.
9. ASKV Critic — multidimensional quality evaluation and refinement.

The Content Extractor is preprocessing rather than a mandatory independent agent. Safety is cross-cutting infrastructure.

## 2. ASKV-IR

ASKV Intermediate Representation (ASKV-IR) is the canonical machine-readable representation of a movie.

It represents movie metadata, characters, locations, scenes, actions, dialogue, shots, cameras, lighting, style, audio, safety state and provenance.

Every major agent consumes and produces typed ASKV-IR/artifacts.

Every artifact records:
- artifact ID
- parent artifact ID
- agent
- model and model version
- prompt/input reference
- timestamp
- hash
- parameters
- safety decision
- status

## 3. Safety Architecture

Safety is enforced at input, during agent handoffs where required, and before final output.

Flow:

Input → Guard → Safe/Transform/Block → Agent Pipeline → Artifact Guard → Final Guard → Output

### Safe Transformation

If an input violates an ASKV policy:
1. Detect and classify the violation.
2. Explain the category briefly.
3. Preserve legitimate creative intent where possible.
4. Remove or replace restricted elements.
5. Re-check the transformed request.
6. Generate only after the transformed request passes the Guard.

ASKV describes this as safe transformation, not as a legal determination.

### Hard blocks

If transformation would preserve a harmful or exploitative objective, ASKV should refuse that generation rather than rewrite it.

### Canonical policy reference

ASKV_VIOLATIONS.md is the human-readable, version-controlled reference for safety categories and transformation rules.

Machine-readable policy files:
- safety/violation_schema.json
- safety/safe_transform_rules.json
- safety/guard_config.yaml

Every safety decision records policy and Guard versions.

## 4. Violation Reference

Initial categories:
- V001 — Sexual Content
- V002 — Child Sexual Exploitation
- V003 — Graphic Violence / Gore
- V004 — Terrorism / Extremism
- V005 — Hate / Targeted Abuse
- V006 — Dangerous Instructions
- V007 — Severe Exploitation / Abuse
- V008 — Non-Consensual Sexual Content
- V009 — Self-Harm
- V010 — Serious Criminal Facilitation / Fraud

The list is versioned and expanded only through documented policy changes.

Actions:
- BLOCK
- TRANSFORM
- ALLOW
- REVIEW where a human review path is implemented

## 5. Critic and Quality System

ASKV-Critic evaluates:
- visual quality
- prompt alignment
- temporal consistency
- character consistency
- scene/story coherence
- cinematography adherence
- audio synchronization
- technical validity
- safety compliance

A composite quality score may be represented as:

Q = wv·V + ws·S + wc·C + wa·A + we·E

Weights are experimental parameters and must be documented.

## 6. Evolutionary Refinement

Evolution is introduced only after the basic critic-refine loop works.

Version 0:
Generate → Critique → Refine

Version 1:
Generate N candidates → Score → Select best → Refine

Version 2:
Generate N candidates → Score → Select parents → Mutation/Crossover → Next generation

The project must experimentally test whether evolutionary refinement improves measurable quality.

## 7. Development Phases

### Phase 0 — Architecture
Week 1:
- Repository structure
- ASKV-IR schema
- Artifact schema
- Guard interface
- Model registry
- Experiment registry
- Initial violation policy
- Orchestrator skeleton

### Phase 1 — Minimal Vertical Slice
Weeks 2–4:
Prompt → Guard → Planner → ASKV-IR → Story → Screenplay → Blender → Camera → Render

Milestone: one 10-second cinematic scene.

### Phase 2 — Character and Scene Consistency
Weeks 5–7:
- character registry
- environment registry
- visual references
- identity consistency
- scene memory

Milestone: 3 connected scenes.

### Phase 3 — Cinematography
Weeks 8–10:
- shot type
- lens
- camera position
- target
- camera movement
- lighting
- composition
- depth of field

Milestone: 30-second cinematic sequence.

### Phase 4 — Audio
Weeks 11–13:
- dialogue
- music
- Foley
- ambience
- audio mixing
- synchronization

Milestone: 30–45 second complete film.

### Phase 5 — Critic
Weeks 14–17:
- multidimensional critic
- automated evaluation
- feedback generation
- refinement loop
- measurable improvement experiments

Milestone: demonstrable improvement between generations.

### Phase 6 — Evolution
Weeks 18–21:
- candidate generation
- selection
- mutation
- optional crossover
- generation tracking
- ablation studies

Milestone: evidence for or against evolutionary improvement.

### Phase 7 — Custom ASKV Models
Weeks 22–28:

Do not pre-commit to a particular custom architecture. Analyze Phase 1–6 bottlenecks first, then select components that benefit from fine-tuning, distillation, reward modeling, domain-specific training or purpose-built models.

Potential candidates:
- ASKV-Story
- ASKV-Guard
- ASKV-Critic
- ASKV-Consistency
- ASKV-Director

## 8. Research Experiments

Required ablations:
1. Single-model baseline
2. Multi-agent pipeline
3. Multi-agent + ASKV-IR
4. Multi-agent + Critic
5. Multi-agent + Critic + Safety
6. Evolutionary refinement

Measure:
- narrative coherence
- scene consistency
- character consistency
- visual quality
- prompt alignment
- temporal consistency
- cinematography adherence
- audio synchronization
- safety violation rate
- pipeline reliability
- GPU-hours per film
- quality improvement per generation

## 9. Infrastructure

Use SLURM for GPU-heavy jobs.

Execution model:

ASKV Orchestrator → SLURM → GPU Worker → Artifact Store → ASKV-IR/Lineage

Parallelize independent scenes/jobs rather than assuming Blender tile rendering is the only useful parallelization mechanism.

Artifact tree:

askv_project/
├── project.json
├── input/
├── planning/
├── screenplay/
├── characters/
├── environments/
├── scenes/
├── blender/
├── renders/
├── audio/
├── video/
├── evaluations/
├── safety/
└── experiments/

## 10. Licensing and Reproducibility

Do not use a blanket statement that every component is unrestricted open source.

Maintain a dependency matrix covering:
- code license
- model license
- dataset license
- commercial-use restrictions
- attribution requirements
- redistribution requirements

Record exact model versions in the model registry.

Distinguish:
software license ≠ model license ≠ dataset license ≠ output rights

## 11. Release Roadmap

- v0.1 — Foundation
- v0.2 — Story + screenplay
- v0.3 — 3D generation
- v0.4 — Audio
- v0.5 — Critic
- v1.0 — Full cinematic pipeline
- v2.0 — Evolutionary generation
- Research releases — Custom ASKV models

## 12. Research Paper Direction

Working title:

ASKV: A Multi-Agent Evolutionary Pipeline for Ethical AI-Driven 3D Cinematic Generation

Core research question:

Can structured multi-agent planning, persistent scene representation, embedded safety governance, and evolutionary quality optimization measurably improve the coherence, consistency, and cinematic quality of AI-generated 3D films?

Suggested sections:
1. Abstract
2. Introduction
3. Related Work
4. Problem Definition
5. ASKV Architecture
6. ASKV-IR
7. Safety Architecture
8. Evolutionary Optimization
9. Implementation
10. Experimental Setup
11. Results
12. Ablation Studies
13. Safety Evaluation
14. Limitations
15. Ethical Considerations
16. Conclusion

Avoid unsupported novelty claims unless established by a literature review.

## 13. Immediate Build Order

1. Freeze ASKV-IR.
2. Create safety policy files.
3. Create Guard interface.
4. Create Planner interface.
5. Create artifact/provenance schemas.
6. Build minimal orchestrator skeleton.
7. Implement text → ASKV-IR.
8. Implement ASKV-IR → Blender scene.
9. Implement camera generation.
10. Render a 10-second scene.
11. Add Critic.
12. Add final Safety Gate.
13. Begin evaluation/ablation framework.

Primary milestone: a reproducible 10-second text-to-3D cinematic vertical slice.
