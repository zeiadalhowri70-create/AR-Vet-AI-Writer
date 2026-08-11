import ast
import json
import os

TARGETS=[
"engine/article_writer_integration_engine.py",
"platform_core/runtime/article_generation_runtime.py",
"platform_core/ai/provider_manager.py",
"core/graph_builder.py",
"platform_core/services/registry/service_registry_engine.py"
]

report={}

for file in TARGETS:

    info={
        "exists":False,
        "classes":[],
        "methods":[]
    }

    if os.path.exists(file):

        info["exists"]=True

        tree=ast.parse(
            open(file,encoding="utf-8").read()
        )

        for node in ast.walk(tree):

            if isinstance(node,ast.ClassDef):
                info["classes"].append(node.name)

            if isinstance(node,ast.FunctionDef):
                info["methods"].append(node.name)

    report[file]=info


with open(
"AR_VET_RUNTIME_CONTRACT_AUDIT.json",
"w",
encoding="utf-8"
) as f:
    json.dump(
        report,
        f,
        indent=2,
        ensure_ascii=False
    )


print("RUNTIME CONTRACT AUDIT COMPLETE")
print("REPORT: AR_VET_RUNTIME_CONTRACT_AUDIT.json")
