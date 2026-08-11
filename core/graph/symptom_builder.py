# -*- coding: utf-8 -*-


class SymptomBuilder:

    def build(self, graph, disease_id, profile):

        symptoms = profile.get("scientific_profile", {}).get("clinical_signs", [])

        for symptom in symptoms:

            symptom_id = symptom.lower().replace(" ", "_")

            graph.add_node(symptom_id, "symptom", {"name": symptom})

            graph.add_edge(disease_id, "has_symptom", symptom_id)

        return graph
