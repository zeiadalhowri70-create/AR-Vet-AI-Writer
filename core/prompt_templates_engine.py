# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Production Prompt Templates Engine

Central storage and rendering engine for AI prompt templates.
"""

from datetime import datetime, UTC


class PromptTemplatesEngine:

    VERSION = "1.0.0"

    def __init__(self):
        self.templates = {}
        self._load_templates()

    def _load_templates(self):

        self.templates = {
            "veterinary_article": {
                "category": "medical",
                "template": (
                    "اكتب مقالاً بيطرياً علمياً احترافياً عن:\n"
                    "{topic}\n\n"
                    "المطلوب:\n"
                    "- مقدمة علمية\n"
                    "- تعريف المرض\n"
                    "- الأسباب\n"
                    "- الأعراض\n"
                    "- التشخيص\n"
                    "- العلاج\n"
                    "- الوقاية\n"
                    "- المراجع العلمية"
                ),
            },
            "seo_article": {
                "category": "seo",
                "template": (
                    "حسن المقال التالي لمحركات البحث:\n"
                    "{content}\n\n"
                    "أضف الكلمات المفتاحية والعناوين المناسبة."
                ),
            },
            "faq_medical": {
                "category": "faq",
                "template": ("أنشئ أسئلة وأجوبة طبية شائعة عن:\n" "{topic}"),
            },
            "image_generation": {
                "category": "media",
                "template": ("أنشئ وصف صورة طبية احترافية لموضوع:\n" "{topic}"),
            },
        }

    def register_template(self, name, category, template):

        self.templates[name] = {"category": category, "template": template}

    def get_template(self, name):

        if name not in self.templates:
            raise KeyError(f"Template not found: {name}")

        return self.templates[name]

    def render(self, name, **kwargs):

        item = self.get_template(name)

        return {
            "name": name,
            "category": item["category"],
            "prompt": item["template"].format(**kwargs),
            "version": self.VERSION,
            "created_at": datetime.now(UTC).isoformat(),
        }

    def list_templates(self):

        return list(self.templates.keys())

    def health(self):

        return {
            "status": True,
            "version": self.VERSION,
            "templates": len(self.templates),
        }


if __name__ == "__main__":

    engine = PromptTemplatesEngine()

    print(engine.health())

    print(engine.render("veterinary_article", topic="مرض النيوكاسل في الدواجن"))
