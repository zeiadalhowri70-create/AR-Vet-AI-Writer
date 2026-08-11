# -*- coding: utf-8 -*-


class PathogenBuilder:

    def build(self, graph, disease_id, profile):

        pathogen = (
            profile.get("scientific_profile", {}).get("pathogen", {}).get("name", "")
        )

        if not pathogen:
            return graph

        pathogen_id = "pathogen_" + pathogen.lower().replace(" ", "_")

        graph.add_node(pathogen_id, "pathogen", {"name": pathogen})

        graph.add_edge(disease_id, "caused_by", pathogen_id)

        return graph
