# -*- coding: utf-8 -*-


class DiseaseProfileValidator:

    required_fields = ["id", "name_ar", "name_en", "animal", "scientific_profile"]

    def validate(self, profile):

        errors = []

        for field in self.required_fields:

            if field not in profile:
                errors.append(f"missing:{field}")

        scientific = profile.get("scientific_profile", {})

        if "pathogen" not in scientific:
            errors.append("missing:pathogen")

        if "clinical_signs" not in scientific:
            errors.append("missing:clinical_signs")

        return {"valid": len(errors) == 0, "errors": errors}
