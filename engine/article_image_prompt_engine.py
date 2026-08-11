# -*- coding: utf-8 -*-


class ArticleImagePromptEngine:

    def __init__(self):
        self.version = "2.0"

    def build_prompt(self, topic):
        return (
            f"Professional veterinary image of {topic}, "
            "high quality scientific illustration, "
            "poultry medicine context, realistic details, "
            "educational veterinary style"
        )

    def build_alt(self, topic):
        return f"صورة توضيحية بيطرية عن {topic}"

    def build_caption(self, topic):
        return f"صورة تعليمية توضح المعلومات البيطرية المتعلقة بـ {topic}"

    def validate(self, data):
        return bool(data.get("prompt") and data.get("alt"))

    def generate(self, topic):
        result = {
            "type": "image",
            "topic": topic,
            "prompt": self.build_prompt(topic),
            "alt": self.build_alt(topic),
            "caption": self.build_caption(topic),
            "featured_ready": True,
            "seo_ready": True,
        }

        result["valid"] = self.validate(result)

        return result

    def info(self):
        return {
            "engine": "Article Image Prompt Engine",
            "version": self.version,
            "status": "production",
        }
