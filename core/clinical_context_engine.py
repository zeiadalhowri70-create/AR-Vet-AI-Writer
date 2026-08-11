# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Clinical Context Intelligence Engine

Stage 2.3
"""


class ClinicalContextEngine:

    VERSION = "1.0.0"

    def __init__(self):

        self.weights = {
            "age": {"chick": 2, "grower": 1, "adult": 1},
            "production": {"broiler": 1, "layer": 2, "breeder": 2},
            "vaccination": {"missing": 3, "partial": 2, "complete": 0},
            "mortality": {"high": 3, "medium": 2, "low": 0},
        }

    def analyze(self, context):

        score = 0

        reasons = []

        for group, value in context.items():

            if group in self.weights:

                if value in self.weights[group]:

                    points = self.weights[group][value]

                    score += points

                    if points > 0:

                        reasons.append(
                            {"factor": group, "value": value, "impact": points}
                        )

        return {"context_score": score, "reasons": reasons}

    def health(self):

        return {
            "status": True,
            "engine": "Clinical Context Intelligence Engine",
            "version": self.VERSION,
        }
