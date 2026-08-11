# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Runtime Dependency Graph Audit
Stage A.6
"""

from pathlib import Path
import ast
import json

ROOT = Path("engine")


def scan_file(path):

    data = {"file": str(path), "classes": [], "functions": [], "objects": []}

    try:

        tree = ast.parse(path.read_text(encoding="utf-8", errors="ignore"))

        for node in ast.walk(tree):

            if isinstance(node, ast.ClassDef):
                data["classes"].append(node.name)

            elif isinstance(node, ast.FunctionDef):
                data["functions"].append(node.name)

            elif isinstance(node, ast.Call):

                if isinstance(node.func, ast.Name):
                    data["objects"].append(node.func.id)

                elif isinstance(node.func, ast.Attribute):
                    data["objects"].append(node.func.attr)

    except Exception:
        pass

    return data


def main():

    result = []

    for file in ROOT.rglob("*.py"):

        result.append(scan_file(file))

    output = Path("runtime_dependency_graph_stage_A.json")

    output.write_text(
        json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print("=" * 70)
    print("AR-VET RUNTIME DEPENDENCY GRAPH A.6")
    print("=" * 70)
    print("FILES:", len(result))
    print("CREATED:", output)


if __name__ == "__main__":
    main()
