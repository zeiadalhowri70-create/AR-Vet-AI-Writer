import ast
import os
import json

TARGETS = [
    "run_production.py",
    "platform_core/integration/platform_bootstrap.py",
    "platform_core/runtime/article_generation_runtime.py",
    "platform_core/ai/generation_integration.py",
    "platform_core/ai/provider_manager.py",
    "engine/article_writer_integration_engine.py",
    "platform_core/services/publishing/publishing_service.py",
    "engine/blogger_publisher.py"
]

report = {}

for file in TARGETS:
    info = {
        "exists": False,
        "imports": [],
        "classes": [],
        "calls": []
    }

    if os.path.exists(file):
        info["exists"] = True

        tree = ast.parse(
            open(file, encoding="utf-8").read()
        )

        for node in ast.walk(tree):

            if isinstance(node, ast.Import):
                for n in node.names:
                    info["imports"].append(n.name)

            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    info["imports"].append(node.module)

            elif isinstance(node, ast.ClassDef):
                info["classes"].append(node.name)

            elif isinstance(node, ast.Call):

                if isinstance(node.func, ast.Name):
                    info["calls"].append(node.func.id)

                elif isinstance(node.func, ast.Attribute):
                    info["calls"].append(node.func.attr)

    report[file] = info


with open(
    "AR_VET_PRODUCTION_RUNTIME_EXECUTION_TRACE.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        report,
        f,
        indent=2,
        ensure_ascii=False
    )

print("PRODUCTION RUNTIME EXECUTION TRACE COMPLETE")
print("REPORT: AR_VET_PRODUCTION_RUNTIME_EXECUTION_TRACE.json")
