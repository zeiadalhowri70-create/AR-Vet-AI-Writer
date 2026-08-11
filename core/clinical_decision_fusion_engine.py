# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Clinical Decision Fusion Engine

Stage 2.3.2
"""


class ClinicalDecisionFusionEngine:

    VERSION = "1.0.0"

    def __init__(self):

        self.name = "Clinical Decision Fusion Engine"

    def combine(self, reasoning_results, context_result, disease_profiles=None):

        results = []

        context_score = context_result.get("context_score", 0)

        for item in reasoning_results:

            disease_id = item.get("disease_id")

            reasoning_score = item.get("score", 0)

            final_score = reasoning_score + context_score

            results.append(
                {
                    "disease_id": disease_id,
                    "reasoning_score": reasoning_score,
                    "context_score": context_score,
                    "final_score": final_score,
                    "confidence": round(
                        final_score / max(1, reasoning_score + context_score) * 100, 2
                    ),
                }
            )

        results.sort(key=lambda x: x["final_score"], reverse=True)

        return {"engine": self.name, "version": self.VERSION, "results": results}

    def health(self):

        return {"status": True, "engine": self.name, "version": self.VERSION}
