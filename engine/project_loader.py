"""
Project Loader
AR-Vet AI Writer
"""

import json
import os


class ProjectLoader:

    def __init__(self):
        self.knowledge = {}

    def load_json(self, filepath):

        if not os.path.exists(filepath):
            return {}

        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)

    def load_knowledge(self):

        files = [
            "animals",
            "article_types",
            "biosecurity",
            "categories",
            "diagnostics",
            "diseases",
            "drugs",
            "glossary",
            "keywords",
            "laboratory_tests",
            "management",
            "nutrition",
            "organs",
            "pathogens",
            "references",
            "symptoms",
            "vaccines",
        ]

        self.knowledge = {}

        for file in files:
            path = f"knowledge/{file}.json"
            print(f"Loading: {path}")

            try:
                self.knowledge[file] = self.load_json(path)

            except Exception as e:
                print(f"\nERROR IN FILE: {path}")
                print(e)
                raise

        return self.knowledge

    def get(self, name):
        return self.knowledge.get(name, {})
