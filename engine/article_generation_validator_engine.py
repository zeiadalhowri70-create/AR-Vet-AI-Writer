# -*- coding: utf-8 -*-


class ArticleGenerationValidatorEngine:

    def validate(self, topic):

        return {"topic": topic, "generation_valid": True}

    def info(self):

        return {"engine": "Article Generation Validator Engine", "version": "1.0"}
