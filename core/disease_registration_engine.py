# -*- coding: utf-8 -*-

import json
from pathlib import Path

from core.disease_profile_validator import DiseaseProfileValidator


class DiseaseRegistrationEngine:

    def __init__(self, folder="knowledge/disease_profiles"):

        self.folder = Path(folder)
        self.validator = DiseaseProfileValidator()

    def register(self, profile):

        validation = self.validator.validate(profile)

        if not validation["valid"]:
            return {"registered": False, "errors": validation["errors"]}

        disease_id = profile["id"]

        file = self.folder / f"{disease_id}.json"

        if file.exists():

            return {"registered": False, "error": "disease_exists"}

        self.folder.mkdir(parents=True, exist_ok=True)

        with open(file, "w", encoding="utf-8") as f:

            json.dump(profile, f, ensure_ascii=False, indent=2)

        return {"registered": True, "file": str(file)}
