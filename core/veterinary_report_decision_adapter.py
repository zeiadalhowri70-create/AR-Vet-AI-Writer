# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Veterinary Report Decision Adapter

Stage 2.7.6.B
"""


class VeterinaryReportDecisionAdapter:

    VERSION = "1.0.0"

    def adapt(self, decision):

        if "results" in decision:
            return decision

        return {
            "results": [
                {
                    "disease_id": decision.get(
                        "disease_id",
                        decision.get("diagnosis", {}).get("disease_id", ""),
                    ),
                    "confidence": decision.get(
                        "confidence", decision.get("diagnosis", {}).get("confidence", 0)
                    ),
                }
            ]
        }

    def health(self):

        return {
            "status": True,
            "engine": "Veterinary Report Decision Adapter",
            "version": self.VERSION,
        }
