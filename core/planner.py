from core.knowledge_manager import KnowledgeManager
from datetime import datetime
import json
import os
import google.generativeai as genai

from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


class ProjectPlanner:

    def __init__(self):

        self.knowledge = KnowledgeManager()

        self.project_path = ""
        self.project = {}

    def load_project(self, project_path):

        self.project_path = project_path

        project_file = os.path.join(project_path, "project.json")

        if not os.path.exists(project_file):
            raise FileNotFoundError("لم يتم العثور على project.json")

        with open(project_file, "r", encoding="utf-8") as file:

            self.project = json.load(file)

        return self.project

    def save_project(self):

        project_file = os.path.join(self.project_path, "project.json")

        with open(project_file, "w", encoding="utf-8") as file:

            json.dump(self.project, file, ensure_ascii=False, indent=4)

    def get_title(self):

        return self.project.get("title", "")

    def analyze_topic(self):

        title = self.get_title()

        result = {
            "title": title,
            "animal": None,
            "category": None,
            "disease": None,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        animals = self.knowledge.get_animals()

        for animal in animals:

            animal_name = animal.get("name_ar", "")

            if animal_name in title:

                result["animal"] = animal

                break

        diseases = self.knowledge.get_diseases()

        for disease in diseases:

            disease_name = disease.get("name_ar", "")

            if disease_name in title:

                result["disease"] = disease

                result["category"] = self.knowledge.find_category(disease["category"])

                break

        return result

    def build_series_plan(self):

        analysis = self.analyze_topic()

        title = analysis["title"]

        disease = analysis["disease"]
        animal = analysis["animal"]
        category = analysis["category"]

        plan = {
            "title": title,
            "animal": animal,
            "category": category,
            "disease": disease,
            "created": analysis["created"],
            "status": "planned",
            "parts": [],
        }

        if disease:

            disease_name = disease["name_ar"]

            plan["parts"] = [
                {"part": 1, "title": f"مقدمة شاملة عن {disease_name}"},
                {"part": 2, "title": f"المسبب المرضي وآلية الإصابة في {disease_name}"},
                {"part": 3, "title": f"الأعراض السريرية والتشخيص"},
                {"part": 4, "title": f"الوقاية وبرامج الأمن الحيوي"},
                {"part": 5, "title": f"العلاج والسيطرة والتحصين"},
                {"part": 6, "title": f"الدليل المرجعي الكامل حول {disease_name}"},
            ]

        else:

            plan["parts"] = [{"part": 1, "title": title}]

        return plan

    def save_series_plan(self):

        plan = self.build_series_plan()

        file_path = os.path.join(self.project_path, "series_plan.json")

        with open(file_path, "w", encoding="utf-8") as file:

            json.dump(plan, file, ensure_ascii=False, indent=4)

        return plan


def build_prompt(self):

    analysis = self.analyze_topic()

    disease = analysis["disease"]
    animal = analysis["animal"]
    category = analysis["category"]

    title = analysis["title"]

    animal_name = ""
    disease_name = ""
    category_name = ""

    if animal:
        animal_name = animal["name_ar"]

    if disease:
        disease_name = disease["name_ar"]

    if category:
        category_name = category["name_ar"]

    prompt = f"""
أنت خبير في الطب البيطري وSEO.

أنشئ خطة علمية احترافية لموسوعة بيطرية.

عنوان المشروع:
{title}

الحيوان:
{animal_name}

المرض:
{disease_name}

التصنيف:
{category_name}

المطلوب:

- حدد عدد الأجزاء المناسب.
- لكل جزء أنشئ:
    title
    seo_title
    meta_description
    slug
    keyword
    summary

أعد النتيجة بصيغة JSON فقط.
"""

    return prompt


def generate_series_plan(self):

    prompt = self.build_prompt()

    print("\nجارٍ إنشاء الخطة العلمية...")

    response = model.generate_content(prompt)

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "", 1)

    if text.startswith("```"):
        text = text.replace("```", "", 1)

    if text.endswith("```"):
        text = text[:-3]

    text = text.strip()

    return text


def parse_series_plan(self):

    text = self.generate_series_plan()

    try:

        plan = json.loads(text)

        return plan

    except Exception as error:

        print("\nفشل تحليل JSON")

        print(error)

        return None
