import json

with open(
    "AR_VET_LEGACY_RUNTIME_CHECK.json",
    encoding="utf-8"
) as f:
    data=json.load(f)


report={
    "project":"AR-Vet-AI-Writer",
    "no_delete":True,
    "categories":{
        "HISTORICAL_SAFE":[],
        "SOURCE_REVIEW_REQUIRED":[],
        "POTENTIAL_DUPLICATE":[],
        "FUTURE_CAPABILITY_REVIEW":[]
    }
}


future_words=[
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
    "automation"
]


for item in data["items"]:

    path=item["file"].lower()
    cls=item["class"].lower()

    text=path+" "+cls

    if item["location"]=="HISTORICAL":
        report["categories"]["HISTORICAL_SAFE"].append(item)

    elif any(x in text for x in future_words):
        report["categories"]["FUTURE_CAPABILITY_REVIEW"].append(item)

    elif "adapter" in text or "bridge" in text or "connector" in text:
        report["categories"]["POTENTIAL_DUPLICATE"].append(item)

    else:
        report["categories"]["SOURCE_REVIEW_REQUIRED"].append(item)


report["summary"]={
    k:len(v)
    for k,v in report["categories"].items()
}


with open(
    "AR_VET_LEGACY_DECISION_REPORT.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        report,
        f,
        indent=2,
        ensure_ascii=False
    )


print("LEGACY DECISION REPORT COMPLETE")

for k,v in report["summary"].items():
    print(k,":",v)

print("REPORT: AR_VET_LEGACY_DECISION_REPORT.json")
