# -*- coding: utf-8 -*-


class ArticleSystemValidationEngine:

    def validate(self, topic):

        return {"topic": topic, "system_valid": True}

    def info(self):

        return {"engine": "Article System Validation Engine", "version": "1.0"}
