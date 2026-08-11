# -*- coding: utf-8 -*-


class ArticleServiceLayerEngine:

    def run(self, topic):

        return {"topic": topic, "service_ready": True}

    def info(self):

        return {"engine": "Article Service Layer Engine", "version": "1.0"}
