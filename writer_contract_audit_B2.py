# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Writer Contract Audit
Stage B.2
"""

from pathlib import Path
import ast
import json

ROOT = Path("engine")


def analyze(path):

    result = {
        "file": str(path),
        "classes": [],
        "write_methods": [],
        "info": False,
        "health": False,
    }

    try:

        tree = ast.parse(path.read_text(encoding="utf-8", errors="ignore"))

        for node in ast.walk(tree):

            if isinstance(node, ast.ClassDef):

                result["classes"].append(node.name)

                for item in node.body:

                    if isinstance(item, ast.FunctionDef):

                        if item.name == "write":

                            result["write_methods"].append(
                                {"args": [a.arg for a in item.args.args]}
                            )

                        if item.name == "info":
                            result["info"] = True

                        if item.name == "health":
                            result["health"] = True

    except Exception as e:

        result["error"] = str(e)

    return result


def main():

    report = []

    for file in ROOT.rglob("*writer*engine.py"):

        report.append(analyze(file))

    output = Path("writer_contract_audit_B2.json")

    output.write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print("=" * 70)
    print("AR-VET WRITER CONTRACT AUDIT B.2")
    print("=" * 70)
    print("WRITERS:", len(report))

    print("CREATED:", output)


if __name__ == "__main__":
    main()
