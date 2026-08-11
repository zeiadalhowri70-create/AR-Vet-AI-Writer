# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Weighted Veterinary Reasoning Engine

Stage 2.2
"""


class WeightedVeterinaryReasoningEngine:

    VERSION = "1.0.0"

    def __init__(self, graph):

        self.graph = graph

        self.symptom_weights = {
            "high_mortality": 5,
            "nervous_signs": 5,
            "green_diarrhea": 4,
            "drop_in_egg_production": 3,
            "respiratory_signs": 3,
            "coughing": 2,
            "sneezing": 2,
        }

    def analyze(self, symptoms):

        scores = {}

        for edge in self.graph.edges:

            if edge["relation"] != "has_symptom":

                continue

            disease = edge["source"]

            symptom = edge["target"]

            if symptom in symptoms:

                weight = self.symptom_weights.get(symptom, 1)

                scores[disease] = scores.get(disease, 0) + weight

        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        results = []

        max_score = ranked[0][1] if ranked else 1

        for disease, score in ranked:

            results.append(
                {
                    "disease_id": disease,
                    "score": score,
                    "confidence": round((score / max_score) * 100, 2),
                }
            )

        return results

    def health(self):

        return {
            "status": True,
            "engine": "Weighted Veterinary Reasoning Engine",
            "version": self.VERSION,
        }
