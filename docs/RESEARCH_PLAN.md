# ASKV Research Plan

## Core hypothesis

Explicit typed handoffs plus repeated safety evaluation and iterative quality feedback can improve reliability of an AI cinematic-generation pipeline compared with a single-agent baseline.

## Baselines

A. Single LLM → video prompt  
B. Multi-agent pipeline without repeated gates  
C. Multi-agent pipeline with repeated gates  
D. Multi-agent pipeline + critic/refinement

## Ablations

- remove input gate
- remove intermediate gates
- remove critic
- replace structured JSON with free-form text
- change critic threshold
- change number of refinement generations

## Metrics

### Reliability
- schema-valid outputs (%)
- successful end-to-end runs (%)
- agent handoff failures/run
- reproducibility across repeated seeds

### Safety
- precision, recall, F1 by hazard category
- false-positive rate on benign cinematic content
- false-negative rate on a held-out adversarial benchmark
- blocked-at-stage distribution

### Cinematic quality
- human preference / rubric score
- CLIP-style text-image alignment
- temporal consistency
- character consistency
- audio-video synchronization error

## Reproducibility

Every experiment should record:
- git commit
- model identifier/version
- model license
- prompt hash
- random seeds
- generation parameters
- hardware
- software environment
- safety policy version
- critic version
- artifact hashes
