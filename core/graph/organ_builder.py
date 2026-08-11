# -*- coding: utf-8 -*-


class OrganBuilder:

    def build(self, graph, disease_id, profile):

        organs = profile.get("scientific_profile", {}).get("affected_organs", [])

        for organ in organs:

            organ_id = organ.lower().replace(" ", "_")

            graph.add_node(organ_id, "organ", {"name": organ})

            graph.add_edge(disease_id, "affects_organ", organ_id)

        return graph
