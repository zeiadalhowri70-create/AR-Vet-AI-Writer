# -*- coding: utf-8 -*-


class GraphQueryEngine:

    def __init__(self, graph):
        self.graph = graph

    def relations(self, disease_id, relation=None):

        results = []

        for edge in self.graph.edges:

            if edge["source"] == disease_id:

                if relation is None or edge["relation"] == relation:
                    results.append(edge["target"])

        return results

    def caused_by(self, disease_id):
        return self.relations(disease_id, "caused_by")

    def symptoms(self, disease_id):
        return self.relations(disease_id, "has_symptom")

    def diagnosis(self, disease_id):
        return self.relations(disease_id, "diagnosed_by")

    def treatment(self, disease_id):
        return self.relations(disease_id, "treated_with")

    def prevention(self, disease_id):
        return self.relations(disease_id, "prevented_by")

    def differential(self, disease_id):
        return self.relations(disease_id, "differential_with")
