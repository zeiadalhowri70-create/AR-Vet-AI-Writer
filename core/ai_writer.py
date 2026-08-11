import os
import json


class AIWriter:

    def __init__(self):

        self.project = {}

        self.series_plan = {}

    def load_project(self, project_path):

        project_file = os.path.join(project_path, "project.json")

        with open(project_file, "r", encoding="utf-8") as file:

            self.project = json.load(file)

    def load_series_plan(self, project_path):

        plan_file = os.path.join(project_path, "series_plan.json")

        with open(plan_file, "r", encoding="utf-8") as file:

            self.series_plan = json.load(file)

    def get_parts(self):

        return self.series_plan.get("parts", [])

    def create_article_structure(self, part):

        return {
            "title": part["title"],
            "seo_title": "",
            "meta_description": "",
            "keyword": "",
            "slug": "",
            "content": "",
            "references": [],
            "faq": [],
            "status": "draft",
        }
