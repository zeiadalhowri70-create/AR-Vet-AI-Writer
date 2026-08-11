import os
import ast
import json
from collections import defaultdict

ROOT = os.getcwd()

SCAN = [
    "engine",
    "platform_core",
    "core"
]

IGNORE = {
    "__pycache__",
    ".git",
    "snapshots",
    "backups",
    "archive",
    "releases",
    "production_archive"
}


classes = defaultdict(list)
imports = defaultdict(list)
generates = defaultdict(list)


def skip(path):
    return any(x in path.split(os.sep) for x in IGNORE)


for base in SCAN:

    for root, dirs, files in os.walk(base):

        dirs[:] = [
            d for d in dirs
            if d not in IGNORE
        ]

        for file in files:

            if not file.endswith(".py"):
                continue

            path = os.path.join(root,file)

            if skip(path):
                continue


            try:

                with open(path,"r",encoding="utf-8") as f:
                    tree = ast.parse(f.read())


                for node in ast.walk(tree):

                    if isinstance(node,ast.ClassDef):
                        classes[node.name].append(path)


                    elif isinstance(node,ast.Import):

                        for item in node.names:
                            imports[item.name].append(path)


                    elif isinstance(node,ast.ImportFrom):

                        if node.module:
                            imports[node.module].append(path)


                    elif isinstance(node,ast.Call):

                        if isinstance(node.func,ast.Attribute):

                            if node.func.attr == "generate":

                                generates[path].append(
                                    ast.unparse(node.func)
                                )


            except:
                pass



important = [
    "ArticleWriterIntegrationEngine",
    "ArticleGenerationRuntime",
    "PlatformBootstrap",
    "ProviderManager",
    "ServiceRegistryEngine",
    "AIWriter",
    "ProjectPlanner"
]


truth = {}

for name in important:

    paths = classes.get(name,[])

    truth[name] = {
        "count":len(paths),
        "locations":paths,
        "status":
            "UNIQUE"
            if len(paths)==1
            else
            "DUPLICATED"
            if len(paths)>1
            else
            "MISSING"
    }



duplicates = {
    k:v
    for k,v in classes.items()
    if len(v)>1
}



report = {

    "project":"AR-Vet-AI-Writer",

    "python_files_scanned":
        sum(
            len(files)
            for _,_,files in os.walk("engine")
        ),

    "official_engine_candidates":
        truth,

    "duplicate_classes":
        duplicates,

    "generate_usage_files":
        generates

}



with open(
    "production_truth_map.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        report,
        f,
        indent=2,
        ensure_ascii=False
    )


print("PRODUCTION TRUTH MAP COMPLETE")
print("REPORT: production_truth_map.json")

for k,v in truth.items():

    print(
        k,
        "=>",
        v["status"],
        v["count"]
    )

