import os
import re

ENGINE_DIR = "engine"

for file in sorted(os.listdir(ENGINE_DIR)):
    if not file.endswith(".py"):
        continue

    path = os.path.join(ENGINE_DIR, file)

    try:
        text = open(path, encoding="utf-8").read()
    except Exception:
        continue

    imports = re.findall(r"from\s+engine\.([A-Za-z0-9_]+)\s+import", text)

    if imports:
        print("=" * 70)
        print(file)
        for imp in imports:
            print("  ->", imp + ".py")
