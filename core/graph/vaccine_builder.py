# -*- coding: utf-8 -*-


class VaccineBuilder:

    def build(self, graph, disease_id, profile):

        vaccines = (
            profile.get("scientific_profile", {})
            .get("prevention", {})
            .get("vaccination", [])
        )

        for vaccine in vaccines:

            vaccine_id = vaccine.lower().replace(" ", "_")

            graph.add_node(vaccine_id, "vaccine", {"name": vaccine})

            graph.add_edge(disease_id, "prevented_by", vaccine_id)

        return graph
