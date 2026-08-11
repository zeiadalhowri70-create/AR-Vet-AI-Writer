# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Article Builder Adapter Audit

Stage B.3.3.1

Audit writer usage inside ArticleRealContentBuilderEngine
"""

from pathlib import Path
import ast
import json

TARGET = Path("engine/article_real_content_builder_engine.py")


def analyze():

    report = {"file": str(TARGET), "writers": [], "calls": [], "imports": []}

    if not TARGET.exists():

        report["error"] = "file_not_found"
        return report

    text = TARGET.read_text(encoding="utf-8", errors="ignore")

    tree = ast.parse(text)

    for node in ast.walk(tree):

        if isinstance(node, ast.Import):

            for item in node.names:

                report["imports"].append(item.name)

        elif isinstance(node, ast.ImportFrom):

            if node.module:

                report["imports"].append(node.module)

        elif isinstance(node, ast.Attribute):

            if node.attr in ["write", "write_section"]:

                report["calls"].append(node.attr)

        elif isinstance(node, ast.Call):

            if isinstance(node.func, ast.Attribute):

                if node.func.attr in ["write", "write_section"]:

                    report["writers"].append(
                        {"method": node.func.attr, "line": node.lineno}
                    )

    return report


def main():

    report = analyze()

    output = Path("article_builder_adapter_audit_B33.json")

    output.write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print("=" * 70)
    print("AR-VET ARTICLE BUILDER ADAPTER AUDIT B.3.3.1")
    print("=" * 70)

    print("WRITE CALLS:", len(report["writers"]))

    print("IMPORTS:", len(report["imports"]))

    print("CREATED:", output)


if __name__ == "__main__":
    main()
