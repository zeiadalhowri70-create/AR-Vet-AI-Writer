# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Veterinary Report Input Adapter

Stage 2.7.6.A
"""


class VeterinaryReportInputAdapter:

    VERSION = "1.0.0"

    def adapt(self, decision):

        return {
            "diagnosis": {
                "disease_id": decision.get("disease_id", ""),
                "confidence": decision.get("confidence", 0),
            },
            "animal": decision.get("animal", ""),
            "symptoms": decision.get("symptoms", []),
        }

    def health(self):

        return {
            "status": True,
            "engine": "Veterinary Report Input Adapter",
            "version": self.VERSION,
        }
