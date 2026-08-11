# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Dependency Architecture Audit
Stage A.3.2
"""

from pathlib import Path
import ast
import json

ROOT = Path(".")


def analyze_file(path):

    result = {"file": str(path), "imports": [], "classes": [], "functions": []}

    try:
        tree = ast.parse(path.read_text(encoding="utf-8", errors="ignore"))

        for node in ast.walk(tree):

            if isinstance(node, ast.Import):
                for item in node.names:
                    result["imports"].append(item.name)

            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    result["imports"].append(node.module)

            elif isinstance(node, ast.ClassDef):
                result["classes"].append(node.name)

            elif isinstance(node, ast.FunctionDef):
                result["functions"].append(node.name)

    except Exception as e:
        result["error"] = str(e)

    return result


def main():

    report = []

    for file in ROOT.rglob("*.py"):

        if "backups" in str(file):
            continue

        report.append(analyze_file(file))

    output = Path("architecture_dependencies_stage_A.json")

    output.write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print("=" * 70)
    print("AR-VET DEPENDENCY AUDIT A.3.2")
    print("=" * 70)
    print("FILES ANALYZED:", len(report))
    print("CREATED:", output)


if __name__ == "__main__":
    main()
