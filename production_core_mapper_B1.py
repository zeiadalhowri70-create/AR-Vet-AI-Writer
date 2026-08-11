# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Production Core Mapper
Stage B.1
"""

from pathlib import Path
import ast
import json

TARGET = Path("engine/article_writer_integration_engine.py")


def analyze():

    result = {
        "file": str(TARGET),
        "imports": [],
        "classes": [],
        "attributes": [],
        "calls": [],
    }

    tree = ast.parse(TARGET.read_text(encoding="utf-8", errors="ignore"))

    for node in ast.walk(tree):

        if isinstance(node, ast.ImportFrom):

            if node.module:
                result["imports"].append(node.module)

        elif isinstance(node, ast.ClassDef):

            result["classes"].append(node.name)

        elif isinstance(node, ast.Attribute):

            result["attributes"].append(node.attr)

        elif isinstance(node, ast.Call):

            if isinstance(node.func, ast.Attribute):
                result["calls"].append(node.func.attr)

    return result


def main():

    data = analyze()

    Path("production_core_map_B1.json").write_text(
        json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print("=" * 70)
    print("AR-VET PRODUCTION CORE MAP B.1")
    print("=" * 70)
    print("IMPORTS:", len(data["imports"]))
    print("CALLS:", len(data["calls"]))
    print("ATTRIBUTES:", len(data["attributes"]))
    print("CREATED: production_core_map_B1.json")


if __name__ == "__main__":
    main()
