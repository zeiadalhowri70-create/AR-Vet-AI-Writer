# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Architecture Usage Matrix
Stage A.4.1
"""

from pathlib import Path
import ast
import json
from collections import defaultdict

ROOT = Path(".")


def get_files():

    return [f for f in ROOT.rglob("*.py") if "backups" not in str(f)]


def scan():

    usage = defaultdict(list)

    files = get_files()

    for file in files:

        try:
            tree = ast.parse(file.read_text(encoding="utf-8", errors="ignore"))

            for node in ast.walk(tree):

                if isinstance(node, ast.ImportFrom):

                    if node.module:

                        usage[node.module].append(str(file))

                elif isinstance(node, ast.Import):

                    for item in node.names:

                        usage[item.name].append(str(file))

        except Exception:
            pass

    return usage


def main():

    usage = scan()

    result = {}

    for module, users in usage.items():

        result[module] = {"used_by_count": len(set(users)), "used_by": list(set(users))}

    output = Path("architecture_usage_matrix_stage_A.json")

    output.write_text(
        json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print("=" * 70)
    print("AR-VET USAGE MATRIX A.4.1")
    print("=" * 70)
    print("MODULES:", len(result))
    print("CREATED:", output)


if __name__ == "__main__":
    main()
