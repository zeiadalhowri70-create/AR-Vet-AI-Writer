# -*- coding: utf-8 -*-


class VeterinaryReasoningEngine:

    def __init__(self, graph):
        self.graph = graph

    def find_diseases_by_symptoms(self, symptoms):

        scores = {}

        for edge in self.graph.edges:

            if edge["relation"] == "has_symptom":

                disease = edge["source"]
                symptom = edge["target"]

                if symptom in symptoms:

                    scores[disease] = scores.get(disease, 0) + 1

        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        return ranked

    def differential_analysis(self, disease_id):

        results = []

        for edge in self.graph.edges:

            if edge["source"] == disease_id and edge["relation"] == "differential_with":
                results.append(edge["target"])

        return results
