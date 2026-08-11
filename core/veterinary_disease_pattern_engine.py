# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Veterinary Disease Pattern Memory Engine

Stage 2.8.2
"""


class VeterinaryDiseasePatternEngine:

    VERSION = "1.0.0"

    def __init__(self, memory_engine):

        self.memory_engine = memory_engine

    def build_patterns(self):

        patterns = {}

        cases = self.memory_engine.get_all()

        for case in cases:

            disease = case.get("disease", "")

            symptoms = case.get("symptoms", [])

            if not disease:
                continue

            if disease not in patterns:

                patterns[disease] = {"disease": disease, "cases": 0, "symptoms": {}}

            patterns[disease]["cases"] += 1

            for symptom in symptoms:

                patterns[disease]["symptoms"][symptom] = (
                    patterns[disease]["symptoms"].get(symptom, 0) + 1
                )

        return patterns

    def analyze_case(self, symptoms):

        patterns = self.build_patterns()

        results = []

        for disease, data in patterns.items():

            score = 0

            for symptom in symptoms:

                if symptom in data["symptoms"]:

                    score += data["symptoms"][symptom]

            if score > 0:

                results.append({"disease": disease, "pattern_score": score})

        results.sort(key=lambda x: x["pattern_score"], reverse=True)

        return results

    def health(self):

        return {
            "status": True,
            "engine": "Veterinary Disease Pattern Memory Engine",
            "version": self.VERSION,
        }
