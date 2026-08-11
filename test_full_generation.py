# -*- coding: utf-8 -*-

from models.project import Project
from models.section import Section
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


part = Section(
    number=1,
    title="التعريف",
    description="تعريف مرض النيوكاسل وأهميته في صناعة الدواجن",
)


engine = IntegrationEngine()

result = engine.generate_article(project, part)

print("تم إنشاء المقال:")
print(result["file"])
