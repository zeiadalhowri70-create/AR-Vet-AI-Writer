# -*- coding: utf-8 -*-


class ArticleDraftGeneratorEngine:

    def generate(self, topic):

        return {
            "title": topic,
            "sections": [
                "Introduction",
                "Definition",
                "Causes",
                "Symptoms",
                "Diagnosis",
                "Treatment",
                "Prevention",
                "Conclusion",
            ],
            "format": "Blogger Draft",
            "generated": True,
        }

    def info(self):

        return {"engine": "Article Draft Generator Engine", "version": "1.0"}
