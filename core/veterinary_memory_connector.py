# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Veterinary Memory Connector

Stage 2.7.2
"""


class VeterinaryMemoryConnector:

    VERSION = "1.0.0"

    def __init__(self, memory_engine):

        self.memory = memory_engine

    def store_diagnosis(self, diagnosis):

        case = {
            "animal": diagnosis.get("animal", ""),
            "disease": diagnosis.get("disease_id", ""),
            "symptoms": diagnosis.get("symptoms", []),
            "confidence": diagnosis.get("confidence", 0),
        }

        return self.memory.add_case(case)

    def health(self):

        return {
            "status": True,
            "engine": "Veterinary Memory Connector",
            "version": self.VERSION,
        }
