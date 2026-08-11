# -*- coding: utf-8 -*-


class ArticleCompletionEngine:

    def complete(self, topic):

        return {"topic": topic, "completed": True}

    def info(self):

        return {"engine": "Article Completion Engine", "version": "1.0"}
