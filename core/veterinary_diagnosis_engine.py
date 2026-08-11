# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Veterinary Diagnosis Engine

Stage 2.1
"""


class VeterinaryDiagnosisEngine:

    VERSION = "1.0.0"

    def __init__(self, graph, reasoning_engine):

        self.graph = graph
        self.reasoning = reasoning_engine

    def diagnose(self, symptoms, animal=None):

        results = []

        matches = self.reasoning.find_diseases_by_symptoms(symptoms)

        for disease_id, score in matches:

            node = self.graph.get_node(disease_id)

            results.append(
                {
                    "disease_id": disease_id,
                    "disease": (
                        node.get("data", {}).get("name_ar", disease_id)
                        if node
                        else disease_id
                    ),
                    "animal": animal,
                    "score": score,
                    "matched_symptoms": [s for s in symptoms],
                }
            )

        results.sort(key=lambda x: x["score"], reverse=True)

        return {
            "engine": "Veterinary Diagnosis Engine",
            "version": self.VERSION,
            "input": {"symptoms": symptoms, "animal": animal},
            "results": results,
        }

    def health(self):

        return {
            "status": True,
            "engine": "Veterinary Diagnosis Engine",
            "version": self.VERSION,
        }
