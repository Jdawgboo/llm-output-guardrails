"""Apply simple deterministic checks to model output text."""
from __future__ import annotations

import json
from typing import Iterable


def check_output(text: str, forbidden: Iterable[str] = (), max_characters: int = 4_000, require_json: bool = False) -> list[str]:
    """Return policy violations without altering the supplied output."""
    violations: list[str] = []
    if len(text) > max_characters:
        violations.append("max_characters")
    lowered = text.lower()
    violations.extend(f"forbidden:{term}" for term in forbidden if term.lower() in lowered)
    if require_json:
        try:
            json.loads(text)
        except json.JSONDecodeError:
            violations.append("invalid_json")
    return violations
