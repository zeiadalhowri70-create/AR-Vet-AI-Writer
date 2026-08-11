import json
import os

with open(
    "AR_VET_ENGINE_STATUS_MAP.json",
    encoding="utf-8"
) as f:
    data = json.load(f)


keywords = {
    "KEEP_PLATFORM_CAPABILITY": [
        "brain",
        "doctor",
        "memory",
        "learning",
        "intelligence",
        "video",
        "image",
        "social",
        "analytics",
        "knowledge",
        "graph",
        "automation",
        "publishing"
    ],

    "KEEP_NEEDS_INTEGRATION": [
        "adapter",
        "bridge",
        "connector",
        "integration",
        "registry",
        "workflow"
    ],

    "ARCHITECTURE_SUPPORT": [
        "service",
        "runtime",
        "manager",
        "router",
        "validator",
        "pipeline"
    ]
}


result = {
    "project": "AR-Vet-AI-Writer",
    "purpose": "Safe architecture review",
    "no_delete": True,
    "categories": {
        "KEEP_PLATFORM_CAPABILITY": [],
        "KEEP_NEEDS_INTEGRATION": [],
        "ARCHITECTURE_SUPPORT": [],
        "LEGACY_CANDIDATE": []
    }
}


review_items = data["classification"].get(
    "REVIEW_REQUIRED",
    []
)


for item in review_items:

    text = (
        str(item.get("class","")) +
        " " +
        str(item.get("file",""))
    ).lower()

    category = "LEGACY_CANDIDATE"

    for key, words in keywords.items():
        if any(w in text for w in words):
            category = key
            break

    result["categories"][category].append(item)


result["summary"] = {
    k: len(v)
    for k,v in result["categories"].items()
}


with open(
    "AR_VET_REVIEW_DECISION_MAP.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        result,
        f,
        indent=2,
        ensure_ascii=False
    )


print("AR-VET REVIEW DECISION MAP COMPLETE")

for k,v in result["summary"].items():
    print(k, ":", v)

print(
    "REPORT: AR_VET_REVIEW_DECISION_MAP.json"
)
