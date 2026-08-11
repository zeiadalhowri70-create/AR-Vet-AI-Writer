# -*- coding: utf-8 -*-

from pathlib import Path
import json

from core.disease_registration_engine import DiseaseRegistrationEngine


class DiseaseBatchImportEngine:

    def __init__(self, folder="knowledge/import_queue"):

        self.folder = Path(folder)
        self.registration = DiseaseRegistrationEngine()

    def import_all(self):

        results = []

        if not self.folder.exists():
            return results

        for file in self.folder.glob("*.json"):

            with open(file, "r", encoding="utf-8") as f:

                profile = json.load(f)

            result = self.registration.register(profile)

            result["source"] = str(file)

            results.append(result)

        return results
