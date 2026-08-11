# -*- coding: utf-8 -*-

"""
Disease Graph Builder
AR-Vet AI Writer

Stage 3.2.2.D
"""


class DiseaseBuilder:

    def build(self, graph, disease_id, profile):

        graph.add_node(
            disease_id,
            "disease",
            {
                "name_ar": profile.get("name_ar", ""),
                "name_en": profile.get("name_en", ""),
                "category": profile.get("category", ""),
                "animal": profile.get("animal", ""),
            },
        )

        return graph
