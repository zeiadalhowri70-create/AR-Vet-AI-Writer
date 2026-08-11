# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Production Pipeline Trace
Stage A.5
"""

from pathlib import Path
import ast
import json

TARGET = Path("engine/article_writer_integration_engine.py")


def analyze():

    result = {
        "file": str(TARGET),
        "imports": [],
        "calls": [],
        "classes": [],
        "functions": [],
    }

    tree = ast.parse(TARGET.read_text(encoding="utf-8", errors="ignore"))

    for node in ast.walk(tree):

        if isinstance(node, ast.ImportFrom):

            if node.module:
                result["imports"].append(node.module)

        elif isinstance(node, ast.Call):

            if isinstance(node.func, ast.Attribute):
                result["calls"].append(node.func.attr)

            elif isinstance(node.func, ast.Name):
                result["calls"].append(node.func.id)

        elif isinstance(node, ast.ClassDef):

            result["classes"].append(node.name)

        elif isinstance(node, ast.FunctionDef):

            result["functions"].append(node.name)

    return result


def main():

    data = analyze()

    out = Path("production_pipeline_trace_stage_A.json")

    out.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

    print("=" * 70)
    print("AR-VET PRODUCTION PIPELINE TRACE A.5")
    print("=" * 70)
    print("IMPORTS:", len(data["imports"]))
    print("CALLS:", len(data["calls"]))
    print("FUNCTIONS:", data["functions"])
    print("=" * 70)
    print("CREATED:", out)


if __name__ == "__main__":
    main()
