# -*- coding: utf-8 -*-


class LesionBuilder:

    def build(self, graph, disease_id, profile):

        lesions = profile.get("scientific_profile", {}).get("lesions", [])

        for lesion in lesions:

            lesion_id = lesion.lower().replace(" ", "_")

            graph.add_node(lesion_id, "lesion", {"name": lesion})

            graph.add_edge(disease_id, "causes_lesion", lesion_id)

        return graph
