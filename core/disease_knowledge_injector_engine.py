# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Disease Knowledge Injector Engine

Stage 3.3
"""


class DiseaseKnowledgeInjectorEngine:

    VERSION = "1.0.0"

    def __init__(self, graph):

        self.graph = graph

    def inject(self, disease_id):

        disease_data = None

        for node in self.graph.nodes.values():

            if isinstance(node, dict) and node.get("id") == disease_id:

                disease_data = node
                break

        if not disease_data:

            return {"found": False, "disease_id": disease_id}

        data = disease_data.get("data", disease_data)

        return {
            "found": True,
            "disease_id": disease_id,
            "knowledge": {
                "name_ar": data.get("name_ar", ""),
                "name_en": data.get("name_en", ""),
                "category": data.get("category", ""),
                "pathogen": data.get("scientific_profile", {}).get("pathogen", {}),
                "clinical_signs": data.get("scientific_profile", {}).get(
                    "clinical_signs", []
                ),
                "diagnosis": data.get("scientific_profile", {}).get("diagnosis", {}),
                "prevention": data.get("scientific_profile", {}).get("prevention", {}),
                "references": data.get("references", []),
            },
        }

    def health(self):

        return {
            "status": True,
            "engine": "Disease Knowledge Injector Engine",
            "version": self.VERSION,
        }
