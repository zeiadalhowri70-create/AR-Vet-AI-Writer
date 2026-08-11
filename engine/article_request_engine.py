# -*- coding: utf-8 -*-


class ArticleRequestEngine:

    def create(self, topic):

        return {"topic": topic, "request_created": True}

    def info(self):

        return {"engine": "Article Request Engine", "version": "1.0"}
