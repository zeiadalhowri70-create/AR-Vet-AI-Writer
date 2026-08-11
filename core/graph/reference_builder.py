# -*- coding: utf-8 -*-


class ReferenceBuilder:

    def build(self, graph, disease_id, profile):

        references = profile.get("references", [])

        for i, ref in enumerate(references, start=1):

            ref_id = f"{disease_id}_ref_{i}"

            graph.add_node(ref_id, "reference", {"citation": ref})

            graph.add_edge(disease_id, "referenced_by", ref_id)

        return graph
