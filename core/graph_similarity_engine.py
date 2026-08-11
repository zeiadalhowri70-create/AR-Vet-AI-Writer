# -*- coding: utf-8 -*-


class GraphSimilarityEngine:

    def __init__(self, graph):
        self.graph = graph

    def _features(self, disease_id):

        features = set()

        for edge in self.graph.edges:

            if edge["source"] == disease_id:

                relation = edge["relation"]

                if relation in [
                    "has_symptom",
                    "diagnosed_by",
                    "treated_with",
                    "causes_lesion",
                    "prevented_by_biosecurity",
                    "caused_by",
                ]:
                    features.add(f"{relation}:{edge['target']}")

        return features

    def similarity(self, disease_a, disease_b):

        a = self._features(disease_a)
        b = self._features(disease_b)

        if not a or not b:
            return 0

        intersection = len(a & b)
        union = len(a | b)

        return round((intersection / union) * 100, 2)

    def most_similar(self, disease_id, limit=5):

        results = []

        diseases = [
            node_id
            for node_id, node in self.graph.nodes.items()
            if node["type"] == "disease" and node_id != disease_id
        ]

        for disease in diseases:

            score = self.similarity(disease_id, disease)

            results.append((disease, score))

        results.sort(key=lambda x: x[1], reverse=True)

        return results[:limit]
