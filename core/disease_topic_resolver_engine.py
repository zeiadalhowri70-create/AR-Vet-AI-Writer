# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Disease Topic Resolver Engine

Production Final
"""

from core.knowledge_manager import KnowledgeManager


class DiseaseTopicResolverEngine:

    VERSION = "1.1.0"

    def __init__(self):
        self.knowledge = KnowledgeManager()

        self.aliases = {
            "newcastle": "newcastle_disease",
            "nd": "newcastle_disease",
            "نيوكاسل": "newcastle_disease",
            "مرض النيوكاسل": "newcastle_disease",
            "newcastle disease": "newcastle_disease",
        }

    def normalize(self, text):

        if not text:
            return ""

        return str(text).strip().lower().replace("  ", " ")

    def resolve(self, topic):

        query = self.normalize(topic)

        if query in self.aliases:

            return {
                "status": True,
                "disease_id": self.aliases[query],
                "match_type": "alias",
            }

        for disease in self.knowledge.get_diseases():

            disease_id = self.normalize(disease.get("id", ""))

            name_ar = self.normalize(disease.get("name_ar", ""))

            name_en = self.normalize(disease.get("name_en", ""))

            if query == disease_id:

                return {"status": True, "disease_id": disease["id"], "match_type": "id"}

            if name_ar and name_ar in query:

                return {
                    "status": True,
                    "disease_id": disease["id"],
                    "match_type": "name_ar",
                }

            if name_en and name_en.lower() in query:

                return {
                    "status": True,
                    "disease_id": disease["id"],
                    "match_type": "name_en",
                }

            if disease_id and disease_id in query:

                return {
                    "status": True,
                    "disease_id": disease["id"],
                    "match_type": "partial_id",
                }

        return {"status": False, "disease_id": None, "match_type": None}

    def health(self):

        return {
            "status": True,
            "engine": "Disease Topic Resolver Engine",
            "version": self.VERSION,
        }
