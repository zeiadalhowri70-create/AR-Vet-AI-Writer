# -*- coding: utf-8 -*-

"""
Disease Knowledge Engine
AR-Vet AI Writer

Stage 1.2.2.B
"""

import json
from pathlib import Path


class DiseaseKnowledge:

    def __init__(self):

        self.folder = Path("knowledge/disease_profiles")

        self.cache = {}

        self.load_all()

    def load_all(self):

        self.cache = {}

        if not self.folder.exists():
            return {}

        for file in self.folder.glob("*.json"):

            with open(file, "r", encoding="utf-8") as f:

                data = json.load(f)

                self.cache[data["id"]] = data

        return self.cache

    def load(self, disease_id):

        return self.cache.get(disease_id)

    def exists(self, disease_id):

        return disease_id in self.cache

    def list_profiles(self):

        return sorted(self.cache.keys())

    def search(self, keyword):

        keyword = keyword.strip()

        results = []

        for disease in self.cache.values():

            if (
                keyword in disease.get("name_ar", "")
                or keyword in disease.get("name_en", "")
                or keyword == disease.get("id", "")
            ):

                results.append(disease)

        return results

    def info(self):

        return {
            "folder": str(self.folder),
            "profiles": self.list_profiles(),
            "count": len(self.cache),
        }
