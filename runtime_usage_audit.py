import os
import ast
from collections import defaultdict

ROOTS = [
    "engine",
    "platform_core",
    "core"
]

classes = defaultdict(list)
used = defaultdict(list)

for base in ROOTS:
    for root, dirs, files in os.walk(base):
        dirs[:] = [d for d in dirs if d != "__pycache__"]

        for f in files:
            if not f.endswith(".py"):
                continue

            path = os.path.join(root,f)

            try:
                with open(path,"r",encoding="utf-8") as fh:
                    tree = ast.parse(fh.read())

                for node in ast.walk(tree):

                    if isinstance(node, ast.ClassDef):
                        classes[node.name].append(path)

                    if isinstance(node, ast.Name):
                        used[node.id].append(path)

            except:
                pass


unused = {}

for cls, locations in classes.items():
    if len(locations)==1 and cls not in used:
        unused[cls]=locations


print("TOTAL CLASSES:",len(classes))
print("SINGLE UNUSED CANDIDATES:",len(unused))

with open(
    "runtime_unused_candidates.txt",
    "w",
    encoding="utf-8"
) as f:
    for cls,loc in unused.items():
        f.write(cls+"\n")
        for x in loc:
            f.write("  "+x+"\n")

print("REPORT: runtime_unused_candidates.txt")
