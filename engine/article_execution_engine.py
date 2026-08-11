# -*- coding: utf-8 -*-


class ArticleExecutionEngine:

    def execute(self, topic):

        return {"topic": topic, "executed": True}

    def info(self):

        return {"engine": "Article Execution Engine", "version": "1.0"}
