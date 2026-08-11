import os
import ast
import json
from collections import defaultdict


TARGETS = [
    "ArticleWriterIntegrationEngine",
    "AIWriter",
    "ProjectPlanner"
]


locations = defaultdict(list)
usage = defaultdict(list)


for root,dirs,files in os.walk("."):

    dirs[:] = [
        d for d in dirs
        if d not in [
            "__pycache__",
            ".git"
        ]
    ]

    for file in files:

        if not file.endswith(".py"):
            continue

        path=os.path.join(root,file)

        try:

            with open(path,"r",encoding="utf-8") as f:
                tree=ast.parse(f.read())


            for node in ast.walk(tree):

                if isinstance(node,ast.ClassDef):

                    if node.name in TARGETS:
                        locations[node.name].append(path)


                if isinstance(node,ast.ImportFrom):

                    if node.module:

                        for t in TARGETS:

                            if t.lower() in node.module.lower():

                                usage[t].append(path)


        except:
            pass



report={}

for t in TARGETS:

    report[t]={
        "definitions":locations[t],
        "imported_by":usage[t],
        "usage_count":len(usage[t])
    }



with open(
    "engine_truth_analysis.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        report,
        f,
        indent=2,
        ensure_ascii=False
    )


print("ENGINE TRUTH ANALYSIS COMPLETE")

for k,v in report.items():

    print("\n",k)
    print("Definitions:")
    for x in v["definitions"]:
        print(" ",x)

    print("Imported by:",v["usage_count"])

