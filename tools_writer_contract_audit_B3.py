# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Writer Contract Audit Engine
Stage B.3.1
"""

from pathlib import Path
import ast
import json

ROOT = Path("engine")


def analyze_writer(path):

    result = {"file": str(path), "class": None, "write_methods": [], "issues": []}

    try:
        tree = ast.parse(path.read_text(encoding="utf-8", errors="ignore"))

        for node in ast.walk(tree):

            if isinstance(node, ast.ClassDef):
                result["class"] = node.name

            if isinstance(node, ast.FunctionDef):

                if node.name in ["write", "write_section"]:

                    args = [arg.arg for arg in node.args.args]

                    method = {
                        "name": node.name,
                        "parameters": args,
                        "has_context": ("context" in args),
                        "returns": None,
                    }

                    if node.body:

                        for item in node.body:

                            if isinstance(item, ast.Return):

                                if isinstance(item.value, ast.Call):
                                    method["returns"] = "call"

                                elif isinstance(item.value, ast.Dict):
                                    method["returns"] = "dict"

                                elif isinstance(item.value, ast.Constant):
                                    method["returns"] = "constant"

                                else:
                                    method["returns"] = "unknown"

                    result["write_methods"].append(method)

        if not result["write_methods"]:
            result["issues"].append("NO_WRITER_METHOD")

    except Exception as e:

        result["issues"].append(str(e))

    return result


def main():

    report = []

    for file in ROOT.glob("*writer*engine.py"):

        report.append(analyze_writer(file))

    output = Path("writer_contract_audit_B3.json")

    output.write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    compatible = 0
    incompatible = 0

    for item in report:

        for method in item["write_methods"]:

            if method["has_context"]:
                compatible += 1
            else:
                incompatible += 1

    print("=" * 70)
    print("AR-VET WRITER CONTRACT AUDIT B.3.1")
    print("=" * 70)

    print("WRITERS:", len(report))

    print("WITH CONTEXT:", compatible)

    print("WITHOUT CONTEXT:", incompatible)

    print("=" * 70)

    print("CREATED:", output)


if __name__ == "__main__":
    main()
