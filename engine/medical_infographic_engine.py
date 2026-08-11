# -*- coding: utf-8 -*-


class MedicalInfographicEngine:
    """
    ينشئ مواصفات الإنفوجرافيك العلمي البيطري.
    """

    def __init__(self):
        self.version = "1.0"

    def build_sections(self, topic):
        return ["definition", "symptoms", "diagnosis", "treatment", "prevention"]

    def build_caption(self, topic):
        return f"إنفوجرافيك علمي يوضح الجوانب الأساسية لمرض {topic}"

    def build_alt(self, topic):
        return f"مخطط معلوماتي بيطري عن {topic}"

    def validate(self, data):
        return bool(data.get("topic") and data.get("sections") and data.get("caption"))

    def generate(self, topic):
        result = {
            "type": "medical_infographic",
            "topic": topic,
            "sections": self.build_sections(topic),
            "caption": self.build_caption(topic),
            "alt": self.build_alt(topic),
            "scientific_ready": True,
            "seo_ready": True,
        }

        result["valid"] = self.validate(result)

        return result

    def info(self):
        return {
            "engine": "Medical Infographic Engine",
            "version": self.version,
            "status": "production",
        }
