# -*- coding: utf-8 -*-


class AnimalBuilder:

    def build(self, graph, disease_id, profile):

        animal = profile.get("animal", "")

        if not animal:
            return graph

        graph.add_node(animal, "animal", {"name": animal})

        graph.add_edge(disease_id, "affects", animal)

        return graph
