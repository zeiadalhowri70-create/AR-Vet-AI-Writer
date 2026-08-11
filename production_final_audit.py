from pathlib import Path
import ast

root = Path("platform/production")

targets = [
    "security",
    "reliability",
    "operational",
    "decision",
    "autonomous_management",
    "autonomous_execution",
    "control",
    "intelligence",
    "knowledge",
    "cognitive",
    "learning",
]

print("=" * 70)
print("AR-VET AI WRITER PRODUCTION FINAL AUDIT")
print("=" * 70)

files = list(root.glob("*.py"))

for name in targets:
    matched = [f for f in files if name in f.name.lower()]

    print("\nLAYER:", name)
    print("FILES:", len(matched))

    for f in matched:
        try:
            tree = ast.parse(f.read_text(encoding="utf-8"))

            classes = [n.name for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]

            functions = [
                n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)
            ]

            content = f.read_text(encoding="utf-8")

            checks = {
                "version": "VERSION" in content,
                "health": "health" in functions,
                "integration": "Integration" in f.name
                or "integration" in content.lower(),
                "report": "report" in functions,
                "class": len(classes) > 0,
            }

            print("-" * 50)
            print(f.name)
            print(checks)

        except Exception as e:
            print(f.name, "ERROR:", e)

print("\n" + "=" * 70)
print("AUDIT COMPLETE")
print("=" * 70)
