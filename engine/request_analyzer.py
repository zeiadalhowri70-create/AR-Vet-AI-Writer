# -*- coding: utf-8 -*-

"""
Request Analyzer
AR-Vet AI Writer

Stage 1.1.5.C
"""


class RequestAnalyzer:

    def __init__(self, knowledge):

        self.knowledge = knowledge

    def analyze(self, text):

        result = {
            "project_type": "article",
            "animal": "",
            "disease": "",
            "category": "",
            "keywords": [],
        }

        text = text.strip()

        # تحديد نوع المشروع

        if "موسوعة" in text:

            result["project_type"] = "encyclopedia"

        elif "سلسلة" in text:

            result["project_type"] = "series"

        elif "دليل" in text:

            result["project_type"] = "guide"

        # البحث عن الحيوان

        animals_data = self.knowledge.get("animals", {}).get("animals", [])

        for animal in animals_data:

            if animal.get("name_ar") in text:

                result["animal"] = animal.get("id", "")

                break

        # البحث عن المرض

        diseases_data = self.knowledge.get("diseases", {}).get("diseases", [])

        for disease in diseases_data:

            if disease.get("name_ar") in text:

                result["disease"] = disease.get("id", "")

                result["category"] = disease.get("category", "")

                result["keywords"] = [disease.get("name_ar", "")]

                break

        return result
