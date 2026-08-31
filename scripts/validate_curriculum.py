#!/usr/bin/env python3
"""Validate the 52-week curriculum layout without third-party dependencies."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
WEEK_RE = re.compile(r"w(?P<week>\d{2})-[a-z0-9-]+\.md$")


def main() -> int:
    files = sorted((ROOT / "curriculum").glob("phase-*/w??-*.md"))
    found: dict[int, Path] = {}
    errors: list[str] = []

    for path in files:
        match = WEEK_RE.fullmatch(path.name)
        if not match:
            errors.append(f"invalid week filename: {path.relative_to(ROOT)}")
            continue

        week = int(match.group("week"))
        if week in found:
            errors.append(
                f"duplicate week {week:02d}: "
                f"{found[week].relative_to(ROOT)} and {path.relative_to(ROOT)}"
            )
        found[week] = path

        text = path.read_text(encoding="utf-8")
        required = (f"week: {week}", "status:", "## 本周目标", "## 验收标准")
        for marker in required:
            if marker not in text:
                errors.append(f"{path.relative_to(ROOT)} missing {marker!r}")

    expected = set(range(1, 53))
    missing = sorted(expected - set(found))
    unexpected = sorted(set(found) - expected)
    if missing:
        errors.append("missing weeks: " + ", ".join(f"{w:02d}" for w in missing))
    if unexpected:
        errors.append("unexpected weeks: " + ", ".join(f"{w:02d}" for w in unexpected))

    if errors:
        print("curriculum validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"curriculum validation passed: {len(files)} week files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

