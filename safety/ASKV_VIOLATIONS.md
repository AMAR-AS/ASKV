# ASKV — Violation Reference

**Policy version:** 1.0  
**Updated:** 25 September 2026

This document is the human-readable, version-controlled reference for ASKV content-safety categories and safe-transformation behavior.

## Core principle

ASKV should preserve legitimate creative intent when possible while removing restricted content. A transformed request must pass the Guard again before generation.

ASKV does not make a universal legal determination. It enforces its defined safety policy.

## Actions

- ALLOW — generation may proceed.
- TRANSFORM — remove or replace restricted elements, then re-check.
- BLOCK — do not generate or preserve the prohibited objective.
- REVIEW — optional human-review path for borderline cases.

## V001 — Sexual Content

**Description:** Explicit sexual or pornographic content.

**Default action:** TRANSFORM or BLOCK depending on context.

**Transformation:** Preserve non-explicit narrative context where possible while removing explicit sexual elements.

## V002 — Child Sexual Exploitation

**Description:** Sexualization, exploitation, or sexual abuse involving minors.

**Default action:** HARD BLOCK.

**Transformation:** Do not preserve or transform the exploitative objective. A completely unrelated safe alternative may be offered.

## V003 — Graphic Violence / Gore

**Description:** Extremely graphic depiction of injury, mutilation, or gore.

**Default action:** TRANSFORM.

**Transformation:** Preserve dramatic context while replacing graphic depiction with non-graphic cinematic implication.

## V004 — Terrorism / Extremism

**Description:** Content that promotes, recruits for, or meaningfully facilitates terrorist or extremist activity.

**Default action:** BLOCK or TRANSFORM depending on context.

**Transformation:** Legitimate historical, documentary, educational, or fictional context may be preserved where appropriate while removing promotion, recruitment, or facilitation.

## V005 — Hate / Targeted Abuse

**Description:** Content targeting protected groups with hateful or abusive material.

**Default action:** TRANSFORM or BLOCK.

**Transformation:** Preserve legitimate narrative context while removing targeted hateful content.

## V006 — Dangerous Instructions

**Description:** Actionable instructions that meaningfully facilitate serious physical harm.

**Default action:** BLOCK or TRANSFORM.

**Transformation:** Replace actionable instructions with non-operational narrative treatment.

## V007 — Severe Exploitation / Abuse

**Description:** Severe exploitation or abuse presented in a way that meaningfully facilitates or glorifies harmful conduct.

**Default action:** BLOCK or TRANSFORM.

**Transformation:** Remove facilitation or exploitative detail while preserving safe narrative context where appropriate.

## V008 — Non-Consensual Sexual Content

**Description:** Sexual content involving lack of consent or sexual exploitation.

**Default action:** HARD BLOCK or TRANSFORM.

**Transformation:** Remove the sexualized non-consensual content; do not preserve an exploitative objective.

## V009 — Self-Harm

**Description:** Content that meaningfully facilitates or encourages self-harm.

**Default action:** BLOCK or TRANSFORM.

**Transformation:** Remove actionable methods or encouragement and redirect to a non-instructional narrative treatment.

## V010 — Serious Criminal Facilitation / Fraud

**Description:** Actionable assistance that meaningfully facilitates serious criminal activity or fraud.

**Default action:** BLOCK or TRANSFORM.

**Transformation:** Preserve legitimate fictional or educational context while removing operational instructions.

## Safety Decision Record

Each Guard decision should record:

- policy version
- Guard version
- artifact ID
- decision
- violation IDs
- confidence
- transformation applied
- re-check result
- timestamp

## Policy Governance

Changes to this file must be version-controlled and documented. Models must not silently rewrite the policy reference.

The machine-readable counterparts should be maintained under:

- safety/violation_schema.json
- safety/safe_transform_rules.json
- safety/guard_config.yaml
