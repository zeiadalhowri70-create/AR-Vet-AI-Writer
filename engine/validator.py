"""
Validator
AR-Vet AI Writer
"""


class Validator:

    def __init__(self, knowledge):
        self.knowledge = knowledge

    def validate_project(self, project):

        errors = []

        if not project.get("name"):
            errors.append("اسم المشروع مفقود")

        if not project.get("type"):
            errors.append("نوع المشروع مفقود")

        return errors

    def validate_animal(self, animal_id):

        animals = self.knowledge.get("animals", {}).get("animals", [])

        for animal in animals:
            if animal["id"] == animal_id:
                return True

        return False

    def validate_disease(self, disease_id):

        diseases = self.knowledge.get("diseases", {}).get("diseases", [])

        for disease in diseases:
            if disease["id"] == disease_id:
                return True

        return False

    def validate_category(self, category_id):

        categories = self.knowledge.get("categories", {}).get("categories", [])

        for category in categories:
            if category["id"] == category_id:
                return True

        return False
