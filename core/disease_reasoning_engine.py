# -*- coding: utf-8 -*-

"""
Disease Reasoning Intelligence Engine
AR-Vet AI Writer

Stage 3.5
"""


class DiseaseReasoningEngine:

    def __init__(self, graph, similarity_engine):
        self.graph = graph
        self.similarity_engine = similarity_engine

    def get_features(self, disease_id):
        return set(self.similarity_engine._features(disease_id))

    def compare(self, disease_a, disease_b):

        features_a = self.get_features(disease_a)
        features_b = self.get_features(disease_b)

        common = features_a.intersection(features_b)

        only_a = features_a - features_b

        only_b = features_b - features_a

        return {
            "disease_a": disease_a,
            "disease_b": disease_b,
            "common_features": sorted(common),
            "unique_to_a": sorted(only_a),
            "unique_to_b": sorted(only_b),
            "common_count": len(common),
            "a_unique_count": len(only_a),
            "b_unique_count": len(only_b),
        }

    def explain_similarity(self, disease_id, limit=5):

        similar = self.similarity_engine.most_similar(disease_id)

        result = []

        for other, score in similar[:limit]:

            comparison = self.compare(disease_id, other)

            result.append(
                {
                    "disease": other,
                    "score": score,
                    "shared_features": comparison["common_features"],
                    "shared_count": comparison["common_count"],
                }
            )

        return result

    def differential_diagnosis(self, disease_id, limit=5):

        similar = self.similarity_engine.most_similar(disease_id)

        return [
            {"disease": disease, "similarity_score": score}
            for disease, score in similar[:limit]
        ]

    def info(self):

        return {
            "engine": "Disease Reasoning Intelligence Engine",
            "version": "1.0",
            "status": "active",
        }
