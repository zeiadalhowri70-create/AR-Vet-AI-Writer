import json
import os

KNOWLEDGE_PATH = "knowledge"


class KnowledgeManager:

    def __init__(self):
        self.animals = self.load_file("animals.json")
        self.categories = self.load_file("categories.json")
        self.diseases = self.load_file("diseases.json")

    def load_file(self, filename):

        path = os.path.join(KNOWLEDGE_PATH, filename)

        if not os.path.exists(path):
            return {}

        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_animals(self):
        return self.animals.get("animals", [])

    def get_categories(self):
        return self.categories.get("categories", [])

    def get_diseases(self):
        return self.diseases.get("diseases", [])

    def find_disease(self, disease_id):

        for disease in self.get_diseases():

            if disease["id"] == disease_id:
                return disease

        return None

    def find_animal(self, animal_id):

        for animal in self.get_animals():

            if animal["id"] == animal_id:
                return animal

        return None

    def find_category(self, category_id):

        for category in self.get_categories():

            if category["id"] == category_id:
                return category

        return None
