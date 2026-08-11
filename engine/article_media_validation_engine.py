# -*- coding: utf-8 -*-


class ArticleMediaValidationEngine:

    def validate(self, topic):
        return {"topic": topic, "media_validated": True}

    def info(self):
        return {"engine": "Article Media Validation Engine", "version": "1.0"}
