from __future__ import annotations

import argparse
import json

from .pipeline import ASKVPhase1


def main() -> None:
    parser = argparse.ArgumentParser(description="ASKV Phase 1")
    parser.add_argument("prompt", help="Text input to ASKV")
    args = parser.parse_args()

    result, scene_document = ASKVPhase1().run(args.prompt)
    print(json.dumps({
        "gate": result.model_dump(),
        "scene_document": scene_document.model_dump() if scene_document else None,
    }, indent=2))
