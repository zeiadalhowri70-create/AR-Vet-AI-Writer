# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Architecture Classification Audit
Stage A.4.2
"""

from pathlib import Path
import json

ROOT = Path(".")


def classify(path):

    p = str(path)

    if "backup" in p:
        return "BACKUP"

    if "/core/" in p:
        return "CORE"

    if "/engine/" in p:
        return "ENGINE"

    if "/providers/" in p:
        return "PROVIDER"

    if "/templates/" in p:
        return "TEMPLATE"

    if "/tests/" in p:
        return "TEST"

    return "OTHER"


def main():

    result = {}

    for file in ROOT.rglob("*.py"):

        if "backups" in str(file):
            continue

        group = classify(file)

        result.setdefault(group, [])

        result[group].append(str(file))

    output = Path("architecture_classification_stage_A.json")

    output.write_text(
        json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print("=" * 70)
    print("AR-VET ARCHITECTURE CLASSIFICATION A.4.2")
    print("=" * 70)

    for k, v in result.items():

        print(k, ":", len(v))

    print("=" * 70)
    print("CREATED:", output)


if __name__ == "__main__":
    main()
