# -*- coding: utf-8 -*-

"""
Project Builder
AR-Vet AI Writer

Stage 1.1.5.B
"""

from models.project import Project


class ProjectBuilder:

    def build(self, analysis):

        project = Project(
            name=analysis.get("disease", "unknown_project"),
            project_type=analysis.get("project_type", "article"),
        )

        project.animal = analysis.get("animal", "")

        project.disease = analysis.get("disease", "")

        project.category = analysis.get("category", "")

        project.keywords = analysis.get("keywords", [])

        return project
