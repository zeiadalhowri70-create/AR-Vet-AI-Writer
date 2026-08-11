# -*- coding: utf-8 -*-


class ArticleOutputEngine:

    def generate(self, topic):

        return {"topic": topic, "output": True}

    def info(self):

        return {"engine": "Article Output Engine", "version": "1.0"}
