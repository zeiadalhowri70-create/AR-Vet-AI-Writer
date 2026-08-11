# -*- coding: utf-8 -*-


class ArticleEntityPlanningEngine:

    def entities(self, topic):

        return {"topic": topic, "entities": [topic, "poultry", "viral_diseases"]}

    def info(self):

        return {"engine": "Article Entity Planning Engine", "version": "1.0"}
