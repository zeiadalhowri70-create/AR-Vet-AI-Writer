# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Veterinary Brain Memory Hook

Stage 2.7.3
"""


class VeterinaryBrainMemoryHook:

    VERSION = "1.0.0"

    def __init__(self, memory_connector):

        self.connector = memory_connector

    def save_diagnosis_result(self, result):

        if not result:

            return {"saved": False, "reason": "empty_result"}

        diagnosis = {
            "animal": result.get("animal", ""),
            "disease_id": result.get("disease_id", ""),
            "symptoms": result.get("symptoms", []),
            "confidence": result.get("confidence", 0),
        }

        count = self.connector.store_diagnosis(diagnosis)

        return {"saved": True, "stored_cases": count}

    def health(self):

        return {
            "status": True,
            "engine": "Veterinary Brain Memory Hook",
            "version": self.VERSION,
        }
