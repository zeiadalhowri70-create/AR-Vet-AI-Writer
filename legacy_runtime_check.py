import json
import os

with open(
    "AR_VET_REVIEW_DECISION_MAP.json",
    encoding="utf-8"
) as f:
    data=json.load(f)


legacy=data["categories"]["LEGACY_CANDIDATE"]


result=[]


for item in legacy:

    path=item.get("file","")
    cls=item.get("class","")

    exists=os.path.exists(path)

    location="SOURCE"

    for x in [
        "backup",
        "snapshot",
        "archive",
        "release",
        "production_backup"
    ]:
        if x in path.lower():
            location="HISTORICAL"
            break


    result.append(
        {
            "class":cls,
            "file":path,
            "exists":exists,
            "location":location
        }
    )


report={
    "project":"AR-Vet-AI-Writer",
    "legacy_count":len(result),
    "items":result
}


with open(
    "AR_VET_LEGACY_RUNTIME_CHECK.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        report,
        f,
        indent=2,
        ensure_ascii=False
    )


print("LEGACY RUNTIME CHECK COMPLETE")
print("ITEMS:",len(result))
print("REPORT: AR_VET_LEGACY_RUNTIME_CHECK.json")
