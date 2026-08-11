# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Veterinary Evidence Engine

Stage 2.5
"""


class VeterinaryEvidenceEngine:

    VERSION = "1.0.0"

    def __init__(self):

        self.name = "Veterinary Evidence Engine"

    def analyze(self, disease_profile, symptoms=None, context=None):

        evidence = []

        if not disease_profile:

            return {"status": False, "message": "Disease profile missing"}

        scientific = disease_profile.get("scientific_profile", {})

        clinical_signs = scientific.get("clinical_signs", [])

        if symptoms:

            for symptom in symptoms:

                if symptom in clinical_signs:

                    evidence.append(
                        {
                            "type": "clinical_sign",
                            "feature": symptom,
                            "support": "positive",
                        }
                    )

        if context:

            if context.get("vaccination") == "missing":

                evidence.append(
                    {
                        "type": "risk_factor",
                        "feature": "missing_vaccination",
                        "support": "positive",
                    }
                )

            if context.get("mortality") == "high":

                evidence.append(
                    {
                        "type": "severity_factor",
                        "feature": "high_mortality",
                        "support": "positive",
                    }
                )

        diagnosis = scientific.get("diagnosis", {})

        confirmation = []

        confirmation.extend(diagnosis.get("laboratory", []))

        confirmation.extend(diagnosis.get("advanced_tests", []))

        return {
            "disease": disease_profile.get("name_ar", ""),
            "evidence": evidence,
            "confirmation_tests": confirmation,
            "evidence_count": len(evidence),
        }

    def health(self):

        return {"status": True, "engine": self.name, "version": self.VERSION}
