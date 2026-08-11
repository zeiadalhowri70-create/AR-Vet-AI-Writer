import json

SOURCE="AR_VET_PRODUCTION_DEPENDENCY_MAP.json"

TARGETS=[
"PlatformBootstrap",
"ArticleGenerationRuntime",
"ProviderManager",
"ServiceRegistryEngine",
"GraphBuilder",
"VeterinaryBrainIntegrationEngine",
"ArticleWriterIntegrationEngine",
"PublishingService",
"SocialPipelineManager",
"Media",
"Video",
"Image",
]

data=json.load(open(SOURCE,encoding="utf-8"))

result={}

for file,info in data.items():

    text=str(info)

    if any(x in text for x in TARGETS):
        result[file]=info


with open(
    "AR_VET_CANONICAL_RUNTIME_NODES.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        result,
        f,
        indent=2,
        ensure_ascii=False
    )

print("CANONICAL RUNTIME NODES COMPLETE")
print("FILES:",len(result))
print("REPORT: AR_VET_CANONICAL_RUNTIME_NODES.json")
