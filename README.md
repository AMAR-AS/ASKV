# ASKV

ASKV is a research prototype for text/image-to-cinematic generation using governed multi-agent orchestration.

## Phase 1 — Foundation and Ethics Gate

Current milestone:

> Text input → Ethics Gate → structured Scene JSON

The architecture intentionally separates policy enforcement from creative generation. Model adapters are interfaces first; heavyweight model dependencies are optional so the core pipeline can be tested without a GPU.

### Phase 1 components

- **Orchestrator** — coordinates deterministic handoffs.
- **Content Extractor** — converts text into validated Scene JSON; image support is an adapter boundary.
- **Ethics Gate** — policy decision interface with an offline deterministic baseline and a pluggable Llama Guard adapter.
- **Audit Logger** — records gate decisions without storing raw sensitive content by default.
- **Schemas** — Pydantic contracts between agents.

### Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
python -m askv.cli "A scientist enters a quiet laboratory at dawn."
```

### Design principle

Do not make the full movie pipeline depend on a single framework. CrewAI can be used as an orchestration implementation, while ASKV keeps agent contracts and safety gates framework-independent.

## Research note

Phase 1 is an engineering foundation, not evidence of cinematic quality. Later experiments must establish baselines, ablations, reproducibility, and quantitative evaluation.
