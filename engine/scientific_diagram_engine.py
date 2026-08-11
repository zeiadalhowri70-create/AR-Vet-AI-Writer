# -*- coding: utf-8 -*-


class ScientificDiagramEngine:
    """
    ينشئ مواصفات الرسوم العلمية البيطرية.
    """

    def __init__(self):
        self.version = "1.0"

    def build_type(self, topic, diagram_type):
        return {
            "topic": topic,
            "diagram_type": diagram_type,
            "purpose": "scientific veterinary education",
        }

    def build_caption(self, topic, diagram_type):
        return f"مخطط علمي يوضح {diagram_type} المرتبط بمرض {topic}"

    def build_alt(self, topic, diagram_type):
        return f"رسم توضيحي بيطري لـ {diagram_type} في {topic}"

    def validate(self, data):
        return bool(
            data.get("topic")
            and data.get("diagram")
            and data["diagram"].get("diagram_type")
            and data.get("caption")
        )

    def generate(self, topic, diagram_type="pathogenesis"):
        result = {
            "type": "scientific_diagram",
            "topic": topic,
            "diagram": self.build_type(topic, diagram_type),
            "caption": self.build_caption(topic, diagram_type),
            "alt": self.build_alt(topic, diagram_type),
            "scientific_ready": True,
        }

        result["valid"] = self.validate(result)

        return result

    def info(self):
        return {
            "engine": "Scientific Diagram Engine",
            "version": self.version,
            "status": "production",
        }
