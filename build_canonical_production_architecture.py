import json
import os


files=[
"AR_VET_CAPABILITY_DISCOVERY_MAP.json",
"AR_VET_ENGINE_STATUS_MAP.json",
"AR_VET_REVIEW_DECISION_MAP.json",
"AR_VET_LEGACY_DECISION_REPORT.json",
"AR_VET_RUNTIME_FLOW_MAP.json",
"AR_VET_RUNTIME_REACHABILITY_REPORT.json"
]


data={}

for f in files:
    if os.path.exists(f):
        with open(f,encoding="utf-8") as x:
            data[f]=json.load(x)


architecture={

"project":
    "AR-Vet-AI-Writer",

"mode":
    "Production Stabilization",

"canonical_runtime":{

"bootstrap":
"platform_core/integration/platform_bootstrap.py",

"generation_runtime":
"platform_core/runtime/article_generation_runtime.py",

"writer":
"engine/article_writer_integration_engine.py",

"provider":
"platform_core/ai/provider_manager.py",

"knowledge":
"core/graph_builder.py"

},


"preserved_capabilities":[
"Veterinary Brain",
"Knowledge Graph",
"Media Generation",
"Social Distribution",
"Publishing",
"Analytics",
"Learning Memory"
],


"source_maps":files,


"rule_set":[
"no historical imports",
"no snapshot execution",
"no duplicate runtime",
"preserve future capabilities",
"production source only"
],


"audited_data":data

}


with open(
"AR_VET_CANONICAL_PRODUCTION_ARCHITECTURE.json",
"w",
encoding="utf-8"
) as f:

    json.dump(
        architecture,
        f,
        indent=2,
        ensure_ascii=False
    )


print("CANONICAL PRODUCTION ARCHITECTURE COMPLETE")
print("REPORT: AR_VET_CANONICAL_PRODUCTION_ARCHITECTURE.json")
