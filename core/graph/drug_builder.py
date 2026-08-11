# -*- coding: utf-8 -*-


class DrugBuilder:

    def build(self, graph, disease_id, profile):

        drugs = (
            profile.get("scientific_profile", {})
            .get("treatment", {})
            .get("supportive", [])
        )

        for drug in drugs:

            drug_id = drug.lower().replace(" ", "_")

            graph.add_node(drug_id, "drug", {"name": drug})

            graph.add_edge(disease_id, "treated_with", drug_id)

        return graph
