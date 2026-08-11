# -*- coding: utf-8 -*-

"""
Series Generator
AR-Vet AI Writer
Stage 6.3.1
"""

import json

from models.project import Project
from models.section import Section
from engine.integration_engine import IntegrationEngine

PROJECT_FILE = "projects/newcastle_disease.json"


def load_project():

    with open(PROJECT_FILE, "r", encoding="utf-8") as f:

        data = json.load(f)

    project = Project(
        name=data["name"],
        project_type=data["project_type"],
        animal=data["animal"],
        disease=data["disease"],
        category=data["category"],
        language=data["language"],
        status=data["status"],
        keywords=data.get("keywords", []),
        references=data.get("references", []),
    )

    return project, data["parts"]


def main():

    project, parts = load_project()

    engine = IntegrationEngine()

    for item in parts:

        section = Section(
            number=item["part"],
            title=item["title"],
            description=f"شرح {item['title']} من مرض {project.disease}",
        )

        print(f"جاري إنشاء الجزء {section.number}: {section.title}")

        result = engine.generate_article(project, section)

        print(f"تم الحفظ: {result['file']}")


if __name__ == "__main__":

    main()
