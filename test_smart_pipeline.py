# -*- coding: utf-8 -*-

from engine.request_analyzer import RequestAnalyzer
from engine.project_builder import ProjectBuilder
from engine.project_planner import ProjectPlanner
from models.project import Project

knowledge = {
    "animals": {"animals": [{"id": "poultry", "name_ar": "الدواجن"}]},
    "diseases": {
        "diseases": [
            {"id": "newcastle", "name_ar": "النيوكاسل", "category": "أمراض فيروسية"}
        ]
    },
}


request = "أريد موسوعة علمية عن مرض النيوكاسل في الدواجن"


print("=" * 50)
print("AR-Vet AI Smart Pipeline Test")
print("=" * 50)


analyzer = RequestAnalyzer(knowledge)

analysis = analyzer.analyze(request)

print("\n1- Analysis:")
print(analysis)


builder = ProjectBuilder()

project = builder.build(analysis)


print("\n2- Project:")
print(project)


planner = ProjectPlanner()

project = planner.create_plan(project)


print("\n3- Plan parts:")
for part in project.parts:

    print(part.number, part.title)


print("\nSUCCESS")
