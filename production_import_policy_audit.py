import os
import re
import json

SCAN=[
    "engine",
    "core",
    "platform_core"
]

FORBIDDEN=[
    "backups",
    "release_snapshot",
    "production_archive",
    "production_backup",
    "production_snapshots",
    "releases"
]

violations=[]

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

                for item in FORBIDDEN:

                    if re.search(
                        r"(from|import).*"+item,
                        text
                    ):
                        violations.append({
                            "file":path,
                            "match":item
                        })

            except:
                pass


report={
    "forbidden_imports":len(violations),
    "details":violations
}


with open(
"PRODUCTION_IMPORT_POLICY_AUDIT.json",
"w",
encoding="utf-8"
) as f:
    json.dump(
        report,
        f,
        indent=2,
        ensure_ascii=False
    )


print("PRODUCTION IMPORT POLICY AUDIT COMPLETE")
print("VIOLATIONS:",len(violations))
print("REPORT: PRODUCTION_IMPORT_POLICY_AUDIT.json")
