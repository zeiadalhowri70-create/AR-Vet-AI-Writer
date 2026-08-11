# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Dead Code Risk Audit
Stage A.7
"""

from pathlib import Path
import ast
import json

ROOT = Path(".")


definitions = {}
usages = {}


def scan(path):

    try:

        tree = ast.parse(path.read_text(encoding="utf-8", errors="ignore"))

        for node in ast.walk(tree):

            if isinstance(node, ast.ClassDef):

                definitions[node.name] = str(path)

            elif isinstance(node, ast.FunctionDef):

                definitions[node.name] = str(path)

            elif isinstance(node, ast.Name):

                usages[node.id] = usages.get(node.id, 0) + 1

    except Exception:
        pass


def main():

    for file in ROOT.rglob("*.py"):

        if "backups" in str(file):
            continue

        scan(file)

    candidates = []

    for name, file in definitions.items():

        if usages.get(name, 0) == 0:

            candidates.append({"name": name, "file": file})

    report = {
        "definitions": len(definitions),
        "unused_candidates": len(candidates),
        "candidates": candidates,
    }

    output = Path("dead_code_risk_stage_A.json")

    output.write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print("=" * 70)
    print("AR-VET DEAD CODE RISK AUDIT A.7")
    print("=" * 70)
    print("DEFINITIONS:", report["definitions"])
    print("UNUSED CANDIDATES:", report["unused_candidates"])
    print("CREATED:", output)


if __name__ == "__main__":
    main()
