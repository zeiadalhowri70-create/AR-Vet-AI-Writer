# -*- coding: utf-8 -*-


class ArticleResultEngine:

    def result(self, topic):

        return {"topic": topic, "result": True}

    def info(self):

        return {"engine": "Article Result Engine", "version": "1.0"}
