# -*- coding: utf-8 -*-


class ScientificFigureIntegrationEngine:
    """
    يربط الرسوم العلمية بأقسام المقال والمراجع.
    """

    def __init__(self):
        self.version = "1.0"

    def build_reference(self, figure_type, references=None):
        return {"figure_type": figure_type, "references": references or []}

    def build_caption(self, topic, figure_type):
        return f"شكل علمي يوضح {figure_type} الخاص بـ {topic}"

    def build_alt(self, topic, figure_type):
        return f"رسم علمي بيطري يوضح {figure_type} في {topic}"

    def validate(self, data):
        return bool(
            data.get("topic") and data.get("figure_type") and data.get("caption")
        )

    def integrate(self, topic, figure_type="scientific_diagram", references=None):
        result = {
            "type": "scientific_figure",
            "topic": topic,
            "figure_type": figure_type,
            "caption": self.build_caption(topic, figure_type),
            "alt": self.build_alt(topic, figure_type),
            "reference_data": self.build_reference(figure_type, references),
            "article_ready": True,
        }

        result["valid"] = self.validate(result)

        return result

    def info(self):
        return {
            "engine": "Scientific Figure Integration Engine",
            "version": self.version,
            "status": "production",
        }
