# -*- coding: utf-8 -*-


class ArticlePlanningEngine:

    def plan(self, topic):

        return {"topic": topic, "status": "planned", "ready": True}

    def info(self):

        return {"engine": "Article Planning Engine", "version": "1.0"}
