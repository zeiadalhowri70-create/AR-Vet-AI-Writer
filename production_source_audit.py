import os
import ast
import json
from collections import defaultdict

ROOT = os.getcwd()

SCAN_DIRS = [
    "engine",
    "platform_core",
    "core"
]

IGNORE = {
    "__pycache__",
    "snapshots",
    "backups",
    "archive",
    "production_archive",
    "release_snapshot",
    "releases"
}

files = []
imports = defaultdict(list)
classes = defaultdict(list)

def ignored(path):
    parts = path.split(os.sep)
    return any(x in IGNORE for x in parts)

for base in SCAN_DIRS:
    for root, dirs, filenames in os.walk(base):
        dirs[:] = [d for d in dirs if d not in IGNORE]

        for f in filenames:
            if f.endswith(".py"):
                path = os.path.join(root, f)

                if ignored(path):
                    continue

                files.append(path)

                try:
                    with open(path, "r", encoding="utf-8") as fh:
                        tree = ast.parse(fh.read())

                    for node in ast.walk(tree):

                        if isinstance(node, ast.Import):
                            for item in node.names:
                                imports[item.name].append(path)

                        elif isinstance(node, ast.ImportFrom):
                            if node.module:
                                imports[node.module].append(path)

                        elif isinstance(node, ast.ClassDef):
                            classes[node.name].append(path)

                except Exception as e:
                    pass


duplicate_classes = {
    k:v for k,v in classes.items()
    if len(v) > 1
}

important = {}

for name in [
    "ArticleWriterIntegrationEngine",
    "ArticleGenerationRuntime",
    "PlatformBootstrap",
    "ProviderManager",
    "ServiceRegistryEngine"
]:
    important[name] = classes.get(name, [])


report = {
    "total_python_files": len(files),
    "important_engines": important,
    "duplicate_classes": duplicate_classes,
    "imports_count": len(imports)
}


with open(
    "production_source_audit_report.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        report,
        f,
        indent=2,
        ensure_ascii=False
    )


print("AUDIT COMPLETE")
print("PYTHON FILES:", len(files))
print("DUPLICATE CLASSES:", len(duplicate_classes))
print("REPORT: production_source_audit_report.json")
