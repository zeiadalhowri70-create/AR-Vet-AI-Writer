# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Veterinary Explanation Engine

Stage 2.4
"""


class VeterinaryExplanationEngine:

    VERSION = "1.0.0"

    def __init__(self):

        self.name = "Veterinary Explanation Engine"

    def explain(self, calibrated_results, context=None):

        if not calibrated_results:

            return {"status": False, "message": "No diagnosis available"}

        primary = calibrated_results[0]

        alternatives = calibrated_results[1:]

        reasons = []

        if context:

            for item in context.get("reasons", []):

                reasons.append(
                    {
                        "factor": item.get("factor"),
                        "value": item.get("value"),
                        "impact": item.get("impact"),
                    }
                )

        return {
            "diagnosis": {
                "disease_id": primary.get("disease_id"),
                "confidence": primary.get("confidence"),
                "level": primary.get("confidence_level"),
            },
            "reasoning": reasons,
            "differential_diagnosis": [
                {
                    "disease_id": item.get("disease_id"),
                    "confidence": item.get("confidence"),
                }
                for item in alternatives
            ],
            "recommendation": [
                "Clinical examination",
                "Laboratory confirmation",
                "Review vaccination history",
                "Improve biosecurity",
            ],
        }

    def health(self):

        return {"status": True, "engine": self.name, "version": self.VERSION}
