# -*- coding: utf-8 -*-


class DifferentialBuilder:

    def build(self, graph, disease_id, profile):

        diseases = profile.get("scientific_profile", {}).get(
            "differential_diagnosis", []
        )

        for disease in diseases:

            disease_key = disease.lower().replace(" ", "_")

            graph.add_node(disease_key, "disease", {"name": disease})

            graph.add_edge(disease_id, "differential_with", disease_key)

        return graph
