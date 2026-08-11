# -*- coding: utf-8 -*-

from models.project import Project
from models.part import Part

from engine.integration_engine import IntegrationEngine

project = Project(
    name="newcastle_disease",
    project_type="encyclopedia",
    animal="poultry",
    disease="مرض النيوكاسل",
    category="أمراض فيروسية",
    language="ar",
    keywords=["مرض النيوكاسل", "أمراض الدواجن", "فيروس النيوكاسل"],
)

project.parts = [1]

part = Part(
    number=1,
    title="التعريف",
    description="تعريف مرض النيوكاسل وأهميته في صناعة الدواجن",
)

engine = IntegrationEngine()

result = engine.generate_article(project, part)

print("=" * 60)
print("تم إنشاء المقال بنجاح")
print("الملف:", result["file"])
print("=" * 60)
