# -*- coding: utf-8 -*-


class BiosecurityBuilder:

    def build(self, graph, disease_id, profile):

        measures = (
            profile.get("scientific_profile", {})
            .get("prevention", {})
            .get("biosecurity", [])
        )

        for measure in measures:

            measure_id = measure.lower().replace(" ", "_")

            graph.add_node(measure_id, "biosecurity", {"name": measure})

            graph.add_edge(disease_id, "prevented_by_biosecurity", measure_id)

        return graph
