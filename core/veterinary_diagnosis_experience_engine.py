# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Veterinary Diagnosis Experience Weight Engine

Stage 2.8.3
"""


class VeterinaryDiagnosisExperienceEngine:

    VERSION = "1.0.0"

    def __init__(self, pattern_engine):

        self.pattern_engine = pattern_engine

    def calculate_experience_weight(self, disease_id, symptoms):

        patterns = self.pattern_engine.build_patterns()

        if disease_id not in patterns:

            return {"disease": disease_id, "experience_cases": 0, "experience_score": 0}

        data = patterns[disease_id]

        total_cases = data.get("cases", 0)

        matched = 0

        for symptom in symptoms:

            if symptom in data["symptoms"]:

                matched += data["symptoms"][symptom]

        score = 0

        if total_cases:

            score = round((matched / len(symptoms)) * 100, 2)

        return {
            "disease": disease_id,
            "experience_cases": total_cases,
            "experience_score": score,
        }

    def apply_experience(self, diagnosis, symptoms):

        results = []

        for item in diagnosis:

            experience = self.calculate_experience_weight(item["disease_id"], symptoms)

            final_score = round(
                (item.get("score", 0) + experience["experience_score"] * 0.2), 2
            )

            results.append(
                {**item, "experience": experience, "final_score": final_score}
            )

        results.sort(key=lambda x: x["final_score"], reverse=True)

        return results

    def health(self):

        return {
            "status": True,
            "engine": "Veterinary Diagnosis Experience Weight Engine",
            "version": self.VERSION,
        }
