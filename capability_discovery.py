import os
import ast
import json


SCAN=[
    "engine",
    "core",
    "platform_core"
]


keywords={
"VETERINARY_BRAIN":[
    "brain",
    "diagnosis",
    "clinical",
    "case",
    "reasoning"
],

"KNOWLEDGE_GRAPH":[
    "graph",
    "knowledge",
    "ontology",
    "disease"
],

"CONTENT_PRODUCTION":[
    "writer",
    "article",
    "content",
    "section"
],

"MEDIA_GENERATION":[
    "image",
    "video",
    "media"
],

"SOCIAL_DISTRIBUTION":[
    "social",
    "linkedin",
    "facebook",
    "telegram",
    "pinterest"
],

"PUBLISHING":[
    "blogger",
    "publish",
    "deployment"
],

"ANALYTICS":[
    "analytics",
    "metric",
    "ranking"
],

"LEARNING_MEMORY":[
    "memory",
    "learning",
    "feedback",
    "optimization"
]
}


result={k:[] for k in keywords}


for base in SCAN:
    for root,dirs,files in os.walk(base):

        for f in files:
            if not f.endswith(".py"):
                continue

            path=os.path.join(root,f)

            try:
                text=open(
                    path,
                    encoding="utf-8"
                ).read().lower()

                for cap,words in keywords.items():
                    if any(w in text for w in words):
                        result[cap].append(path)

            except:
                pass


for k in result:
    result[k]=sorted(set(result[k]))


with open(
    "AR_VET_CAPABILITY_DISCOVERY_MAP.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        result,
        f,
        indent=2,
        ensure_ascii=False
    )


print("CAPABILITY DISCOVERY COMPLETE")

for k,v in result.items():
    print(k,":",len(v))

print("REPORT: AR_VET_CAPABILITY_DISCOVERY_MAP.json")
