# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Veterinary Report Memory Bridge

Stage 2.7.6
"""


class VeterinaryReportMemoryBridge:

    VERSION = "1.0.0"

    def __init__(self, report_engine, memory_sync):

        self.report_engine = report_engine

        self.memory_sync = memory_sync

    def generate_and_store(self, decision, evidence, explanation):

        report = self.report_engine.generate(decision, evidence, explanation)

        diagnosis_data = decision.get("diagnosis", decision)

        case = {
            "animal": decision.get("animal", ""),
            "disease": diagnosis_data.get("disease_id", ""),
            "symptoms": decision.get("symptoms", []),
            "confidence": diagnosis_data.get("confidence", 0),
        }

        memory_result = self.memory_sync.sync_case(case)

        return {"report": report, "memory": memory_result}

    def health(self):

        return {
            "status": True,
            "engine": "Veterinary Report Memory Bridge",
            "version": self.VERSION,
        }
