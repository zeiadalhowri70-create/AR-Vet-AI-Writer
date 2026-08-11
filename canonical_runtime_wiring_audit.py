import ast
import os
import json

TARGETS = [
    "platform_core/integration/platform_bootstrap.py",
    "platform_core/runtime/article_generation_runtime.py",
    "platform_core/ai/provider_manager.py",
    "core/graph_builder.py",
    "core/veterinary_brain_integration_engine.py",
    "core/social_pipeline_manager.py",
    "engine/blogger_publisher.py"
]

result={}

for file in TARGETS:
    info={
        "exists":False,
        "imports":[],
        "classes":[],
        "calls":[]
    }

    if os.path.exists(file):
        info["exists"]=True

        tree=ast.parse(
            open(file,encoding="utf-8").read()
        )

        for node in ast.walk(tree):

            if isinstance(node,ast.ClassDef):
                info["classes"].append(node.name)

            elif isinstance(node,ast.ImportFrom):
                if node.module:
                    info["imports"].append(node.module)

            elif isinstance(node,ast.Call):
                if isinstance(node.func,ast.Name):
                    info["calls"].append(node.func.id)

                elif isinstance(node.func,ast.Attribute):
                    info["calls"].append(node.func.attr)

    result[file]=info


with open(
"AR_VET_CANONICAL_RUNTIME_WIRING_AUDIT.json",
"w",
encoding="utf-8"
) as f:

    json.dump(
        result,
        f,
        indent=2,
        ensure_ascii=False
    )


print("CANONICAL RUNTIME WIRING AUDIT COMPLETE")
print("REPORT: AR_VET_CANONICAL_RUNTIME_WIRING_AUDIT.json")
