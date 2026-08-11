# -*- coding: utf-8 -*-


class ArticleWriterValidationEngine:

    def validate(self, topic):

        return {"topic": topic, "valid": True}

    def info(self):

        return {"engine": "Article Writer Validation Engine", "version": "1.0"}
