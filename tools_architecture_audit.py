# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Architecture Audit Scanner
Stage A.3.1
"""

from pathlib import Path
import json

ROOT = Path(".")


def scan_folder(folder):
    path = ROOT / folder

    if not path.exists():
        return {"exists": False, "files_count": 0, "files": []}

    files = list(path.rglob("*.py"))

    return {"exists": True, "files_count": len(files), "files": [str(f) for f in files]}


def main():

    folders = [
        "core",
        "engine",
        "providers",
        "knowledge",
        "templates",
        "tests",
        "data",
    ]

    report = {"project": str(ROOT.resolve()), "folders": {}}

    for folder in folders:
        report["folders"][folder] = scan_folder(folder)

    report["total_python_files"] = len(list(ROOT.rglob("*.py")))

    output = Path("architecture_audit_stage_A.json")

    output.write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print("=" * 70)
    print("AR-VET ARCHITECTURE AUDIT STAGE A.3.1")
    print("=" * 70)

    print("TOTAL PYTHON FILES:", report["total_python_files"])

    for name, data in report["folders"].items():
        print(name, ":", data["files_count"])

    print("=" * 70)
    print("CREATED:", output)


if __name__ == "__main__":
    main()
