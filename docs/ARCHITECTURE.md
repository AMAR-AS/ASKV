# ASKV Architecture — Phase 1

## Corrected architecture

Input
→ Input Safety Gate
→ Content Extraction
→ Schema Validation
→ Output Safety Gate
→ downstream agent

The safety layer is a **policy enforcement plane**, not merely another creative agent.

## Important design corrections

1. **Gate every handoff**, not only input and final output.
2. **Use typed contracts** between agents so malformed model output cannot silently propagate.
3. **Keep model adapters replaceable.** Llama Guard, VLMs and LLMs should sit behind interfaces.
4. **Treat safety as defense in depth.** A single classifier cannot guarantee safety.
5. **Do not describe the system as "unbreakable" or perfectly safe.** Report measured false-positive and false-negative rates.
6. **Separate quality scoring from safety scoring.** Safety is a constraint/gate; cinematic quality is an optimization objective.
7. **Use immutable provenance metadata** for every artifact: prompt hash, model/version, seed, parameters, agent, timestamp and parent artifact.
8. **Do not call a generated output "3D" merely because it was edited into a 3D workflow.** The system must actually construct/render 3D scenes or explicitly label a component as 2D/video synthesis.

## Phase-1 research question

Can a typed, safety-gated multi-agent architecture reliably transform unstructured cinematic prompts into machine-valid scene specifications while preventing policy-triggering inputs and outputs from entering downstream generation?

Later experiments can test:
- schema validity rate
- gate precision/recall
- handoff failure rate
- latency
- reproducibility
- downstream scene consistency
