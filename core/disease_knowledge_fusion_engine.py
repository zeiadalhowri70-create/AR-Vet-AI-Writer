# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Disease Knowledge Fusion Engine

Combines disease profile data with knowledge graph intelligence.
"""

from core.disease_knowledge import DiseaseKnowledge


class DiseaseKnowledgeFusionEngine:

    VERSION = "1.0.0"

    def __init__(self, graph):

        self.graph = graph
        self.knowledge = DiseaseKnowledge()

    def fuse(self, disease_id):

        profile = self.knowledge.load(disease_id)

        if not profile:

            return {"found": False, "disease_id": disease_id}

        node = self.graph.get_node(disease_id)

        graph_data = {}

        if node:

            graph_data = {"type": node.get("type"), "data": node.get("data", {})}

        return {
            "found": True,
            "disease_id": disease_id,
            "basic": {
                "name_ar": profile.get("name_ar", ""),
                "name_en": profile.get("name_en", ""),
                "category": profile.get("category", ""),
                "animal": profile.get("animal", ""),
            },
            "scientific_profile": profile.get("scientific_profile", {}),
            "graph": graph_data,
            "references": profile.get("references", []),
            "seo": profile.get("seo", {}),
        }

    def health(self):

        return {
            "status": True,
            "engine": "Disease Knowledge Fusion Engine",
            "version": self.VERSION,
        }
