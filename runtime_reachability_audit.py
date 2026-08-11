import ast
import os
import json
from collections import defaultdict


ROOTS=[
    "platform_core/integration/platform_bootstrap.py",
    "platform_core/runtime/article_generation_runtime.py",
    "engine/article_writer_integration_engine.py"
]


visited=set()
graph=defaultdict(set)


def scan(path):

    if path in visited:
        return

    visited.add(path)

    try:
        with open(path,encoding="utf-8") as f:
            tree=ast.parse(f.read())

    except:
        return


    for node in ast.walk(tree):

        if isinstance(node,ast.ImportFrom):

            if node.module:

                graph[path].add(node.module)


        elif isinstance(node,ast.Import):

            for x in node.names:
                graph[path].add(x.name)



    for dep in list(graph[path]):

        candidate=dep.replace(".","/")+".py"

        if os.path.exists(candidate):
            scan(candidate)



for root in ROOTS:
    if os.path.exists(root):
        scan(root)



report={

"entry_points":ROOTS,

"reachable_files":len(visited),

"reachable_modules":list(visited),

"dependency_edges":
{
k:list(v)
for k,v in graph.items()
}

}


with open(
"AR_VET_RUNTIME_REACHABILITY_REPORT.json",
"w",
encoding="utf-8"
) as f:

    json.dump(
        report,
        f,
        indent=2,
        ensure_ascii=False
    )


print("RUNTIME REACHABILITY COMPLETE")
print("FILES:",len(visited))
print("REPORT: AR_VET_RUNTIME_REACHABILITY_REPORT.json")
