# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Veterinary Case Similarity Engine

Stage 2.8.1 Fixed
"""

from core.veterinary_memory_access_adapter import VeterinaryMemoryAccessAdapter


class VeterinaryCaseSimilarityEngine:

    VERSION = "1.0.1"

    def __init__(self, memory_engine):

        self.memory_engine = VeterinaryMemoryAccessAdapter(memory_engine)

    def similarity(self, symptoms_a, symptoms_b):

        if not symptoms_a or not symptoms_b:
            return 0

        set_a = set(symptoms_a)
        set_b = set(symptoms_b)

        union = set_a.union(set_b)

        if not union:
            return 0

        intersection = set_a.intersection(set_b)

        return round(len(intersection) / len(union) * 100, 2)

    def find_similar_cases(self, symptoms, limit=5):

        results = []

        cases = self.memory_engine.get_all()

        for case in cases:

            score = self.similarity(symptoms, case.get("symptoms", []))

            if score > 0:

                results.append({"case": case, "similarity": score})

        results.sort(key=lambda x: x["similarity"], reverse=True)

        return results[:limit]

    def health(self):

        return {
            "status": True,
            "engine": "Veterinary Case Similarity Engine",
            "version": self.VERSION,
        }
