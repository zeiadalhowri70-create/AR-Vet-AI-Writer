# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Encyclopedia Article Builder Engine
Production Final v1.0
"""

from engine.project_planner import ProjectPlanner


class EncyclopediaArticleBuilderEngine:
    """
    مسؤول عن بناء هيكل المقالة الموسوعية البيطرية.

    الوظائف:
    - إدارة أقسام الموسوعة.
    - ترتيب المحتوى.
    - ضمان وجود الأقسام العلمية.
    - تجهيز المقال للدمج مع Pipeline.
    """

    VERSION = "1.0.0"

    def __init__(self):
        self.planner = ProjectPlanner()

    def build_structure(self, project):

        project.project_type = "encyclopedia"

        planned = self.planner.create_plan(project)

        sections = []

        for part in planned.parts:
            sections.append(
                {
                    "number": part.number,
                    "title": part.title,
                    "description": part.description,
                    "evidence_required": True,
                    "validation_required": True,
                }
            )

        return {
            "engine": "EncyclopediaArticleBuilderEngine",
            "version": self.VERSION,
            "type": "Encyclopedia Scientific Builder",
            "sections_count": len(sections),
            "sections": sections,
        }

    def info(self):
        return {
            "engine": "Encyclopedia Article Builder Engine",
            "version": self.VERSION,
            "type": "Production Final",
        }
