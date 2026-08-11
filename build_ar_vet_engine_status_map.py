import json
import os
from collections import defaultdict

with open(
    "engine_role_classification.json",
    encoding="utf-8"
) as f:
    roles = json.load(f)

with open(
    "production_truth_map.json",
    encoding="utf-8"
) as f:
    truth = json.load(f)


status_map = defaultdict(list)


for cls, data in roles.items():

    role = data.get("role", "UNKNOWN")

    if role == "CONNECTED":
        status = "CONNECTED_MODULE"

    elif role == "RUNTIME_CANDIDATE":
        status = "ACTIVE_CANDIDATE"

    elif role == "REVIEW":
        status = "REVIEW_REQUIRED"

    else:
        status = "UNKNOWN"


    status_map[status].append(
        {
            "class": cls,
            "file": data.get("file"),
            "used_by": data.get("used_by", [])
        }
    )


important = truth.get(
    "official_engine_candidates",
    {}
)


report = {

    "project":
        "AR-Vet-AI-Writer",

    "purpose":
        "Architecture stabilization without deletion",

    "rules":
    {
        "no_delete": True,
        "future_modules_preserved": True,
        "production_only_after_validation": True
    },

    "official_core":
        important,

    "classification":
        dict(status_map),

    "summary":
    {
        k: len(v)
        for k,v in status_map.items()
    }

}


with open(
    "AR_VET_ENGINE_STATUS_MAP.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        report,
        f,
        indent=2,
        ensure_ascii=False
    )


print("AR-VET ENGINE STATUS MAP COMPLETE")

for k,v in report["summary"].items():
    print(k, ":", v)

print(
    "REPORT: AR_VET_ENGINE_STATUS_MAP.json"
)
