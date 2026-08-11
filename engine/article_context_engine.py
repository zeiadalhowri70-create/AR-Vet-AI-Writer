# -*- coding: utf-8 -*-


class ArticleContextEngine:

    def build(self, topic):

        return {"topic": topic, "context_ready": True}

    def info(self):

        return {"engine": "Article Context Engine", "version": "1.0"}
