# -*- coding: utf-8 -*-

"""
Prompt Strategy Engine
AR-Vet AI Writer

Stage 1.1.4.A
"""


class PromptStrategy:

    def __init__(self):

        self.strategies = {
            "article": "article_prompt.txt",
            "series": "article_prompt.txt",
            "encyclopedia": "article_prompt.txt",
            "guide": "writer_prompt.txt",
            "review": "reviewer_prompt.txt",
            "seo": "seo_prompt.txt",
            "planner": "planner_prompt.txt",
            "master": "master_prompt.txt",
        }

    def select(self, project):

        project_type = getattr(project, "project_type", "article")

        return self.strategies.get(project_type, "article_prompt.txt")

    def name(self):

        return "Prompt Strategy Engine"

    def info(self):

        return {"name": self.name(), "strategies": self.strategies}
