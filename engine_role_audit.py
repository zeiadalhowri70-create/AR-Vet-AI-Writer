import os
import ast
import json
from collections import defaultdict

ROOTS=[
    "engine",
    "core",
    "platform_core"
]

classes={}
imports=defaultdict(list)
files=[]

for base in ROOTS:
    for root,dirs,fs in os.walk(base):

        dirs[:]=[
            d for d in dirs
            if d not in [
                "__pycache__",
                "_project_history"
            ]
        ]

        for f in fs:
            if not f.endswith(".py"):
                continue

            path=os.path.join(root,f)
            files.append(path)

            try:
                tree=ast.parse(
                    open(path,encoding="utf-8").read()
                )

                for n in ast.walk(tree):

                    if isinstance(n,ast.ClassDef):
                        classes[n.name]=path

                    if isinstance(n,ast.ImportFrom):
                        if n.module:
                            imports[path].append(n.module)

            except:
                pass


result={}

for cls,path in classes.items():

    used_by=[]

    for f,mods in imports.items():
        if path.replace("/","." ).replace(".py","") in mods:
            used_by.append(f)

    if used_by:
        role="CONNECTED"

    elif any(x in path.lower() for x in [
        "production",
        "runtime",
        "pipeline",
        "integration"
    ]):
        role="RUNTIME_CANDIDATE"

    else:
        role="REVIEW"


    result[cls]={
        "file":path,
        "role":role,
        "used_by":used_by[:10]
    }


with open(
    "engine_role_classification.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        result,
        f,
        indent=2,
        ensure_ascii=False
    )


print("ENGINE ROLE AUDIT COMPLETE")
print("CLASSES:",len(result))

from collections import Counter
print(Counter(
    x["role"] for x in result.values()
))
