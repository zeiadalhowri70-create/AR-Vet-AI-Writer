# -*- coding: utf-8 -*-


class ArticleVideoMetadataEngine:

    def __init__(self):
        self.version = "2.0"

    def build_title(self, topic):
        return f"شرح بيطري شامل: {topic}"

    def build_description(self, topic):
        return (
            f"فيديو تعليمي بيطري يشرح {topic} "
            "من حيث الأسباب والأعراض والتشخيص والوقاية."
        )

    def build_tags(self, topic):
        return [
            topic,
            "الطب البيطري",
            "الدواجن",
            "أمراض الدواجن",
            "Veterinary Medicine",
        ]

    def validate(self, data):
        return bool(data.get("title") and data.get("description"))

    def generate(self, topic):
        result = {
            "type": "video",
            "topic": topic,
            "title": self.build_title(topic),
            "description": self.build_description(topic),
            "tags": self.build_tags(topic),
            "youtube_ready": True,
        }

        result["valid"] = self.validate(result)

        return result

    def info(self):
        return {
            "engine": "Article Video Metadata Engine",
            "version": self.version,
            "status": "production",
        }
