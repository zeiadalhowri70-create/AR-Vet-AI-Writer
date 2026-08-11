import ast
import os
import json

ROOTS = [
    "run_production.py",
    "platform_core",
    "engine",
    "core"
]

report = {}

files = []

for root in ROOTS:
    if os.path.isfile(root):
        files.append(root)
    else:
        for path, dirs, names in os.walk(root):
            for name in names:
                if name.endswith(".py") and "test" not in name:
                    files.append(os.path.join(path,name))


for file in files:
    try:
        tree = ast.parse(
            open(file,encoding="utf-8").read()
        )

        imports=[]
        classes=[]

        for node in ast.walk(tree):

            if isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.append(node.module)

            elif isinstance(node, ast.Import):
                for x in node.names:
                    imports.append(x.name)

            elif isinstance(node, ast.ClassDef):
                classes.append(node.name)

        report[file]={
            "imports":imports,
            "classes":classes
        }

    except Exception:
        pass


with open(
    "AR_VET_PRODUCTION_DEPENDENCY_MAP.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        report,
        f,
        indent=2,
        ensure_ascii=False
    )

print("PRODUCTION DEPENDENCY MAP COMPLETE")
print("REPORT: AR_VET_PRODUCTION_DEPENDENCY_MAP.json")
