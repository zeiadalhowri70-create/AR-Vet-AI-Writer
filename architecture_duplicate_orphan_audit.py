# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Duplicate & Orphan Architecture Audit
Stage A.3.3
"""

from pathlib import Path
import ast
import json
from collections import defaultdict

ROOT = Path(".")


def scan_python_files():
    files = []
    for f in ROOT.rglob("*.py"):
        if "backups" not in str(f):
            files.append(f)
    return files


def analyze_file(path):
    data = {"file": str(path), "imports": [], "classes": [], "functions": []}

    try:
        tree = ast.parse(path.read_text(encoding="utf-8", errors="ignore"))

        for node in ast.walk(tree):

            if isinstance(node, ast.Import):
                for x in node.names:
                    data["imports"].append(x.name)

            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    data["imports"].append(node.module)

            elif isinstance(node, ast.ClassDef):
                data["classes"].append(node.name)

            elif isinstance(node, ast.FunctionDef):
                data["functions"].append(node.name)

    except Exception as e:
        data["error"] = str(e)

    return data


def main():

    files = scan_python_files()

    reports = [analyze_file(f) for f in files]

    class_map = defaultdict(list)
    function_map = defaultdict(list)

    for item in reports:

        for c in item["classes"]:
            class_map[c].append(item["file"])

        for fn in item["functions"]:
            function_map[fn].append(item["file"])

    duplicates = {
        "classes": {k: v for k, v in class_map.items() if len(v) > 1},
        "functions": {k: v for k, v in function_map.items() if len(v) > 1},
    }

    imported = set()

    for item in reports:
        for imp in item["imports"]:
            imported.add(imp)

    orphan_candidates = []

    for item in reports:

        name = Path(item["file"]).stem

        used = False

        for imp in imported:
            if name in imp:
                used = True

        if not used:
            orphan_candidates.append(item["file"])

    result = {
        "files_scanned": len(files),
        "duplicate_classes": duplicates["classes"],
        "duplicate_functions": duplicates["functions"],
        "orphan_candidates": orphan_candidates,
    }

    output = Path("architecture_duplicate_orphan_stage_A.json")

    output.write_text(
        json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print("=" * 70)
    print("AR-VET DUPLICATE ORPHAN AUDIT A.3.3")
    print("=" * 70)
    print("FILES:", len(files))
    print("DUPLICATE CLASSES:", len(duplicates["classes"]))
    print("DUPLICATE FUNCTIONS:", len(duplicates["functions"]))
    print("ORPHAN CANDIDATES:", len(orphan_candidates))
    print("=" * 70)
    print("CREATED:", output)


if __name__ == "__main__":
    main()
