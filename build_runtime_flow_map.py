import os
import ast
import json
from collections import defaultdict


SCAN=[
    "engine",
    "core",
    "platform_core"
]


flows=defaultdict(set)


targets=[
    "PlatformBootstrap",
    "ArticleGenerationRuntime",
    "ArticleWriterIntegrationEngine",
    "ProviderManager",
    "ServiceRegistryEngine",
    "GraphBuilder",
    "VeterinaryBrainIntegrationEngine"
]


for base in SCAN:

    for root,dirs,files in os.walk(base):

        for file in files:

            if not file.endswith(".py"):
                continue

            path=os.path.join(root,file)

            try:

                text=open(
                    path,
                    encoding="utf-8"
                ).read()


                for t in targets:

                    if t in text:

                        flows[t].add(path)


            except:
                pass



report={
    "project":"AR-Vet-AI-Writer",
    "runtime_candidates":
        {
            k:list(v)
            for k,v in flows.items()
        }
}


with open(
    "AR_VET_RUNTIME_FLOW_MAP.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        report,
        f,
        indent=2,
        ensure_ascii=False
    )


print("RUNTIME FLOW MAP COMPLETE")

for k,v in flows.items():
    print(k,":",len(v))

print("REPORT: AR_VET_RUNTIME_FLOW_MAP.json")
