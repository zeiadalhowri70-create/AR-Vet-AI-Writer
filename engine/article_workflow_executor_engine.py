# -*- coding: utf-8 -*-


class ArticleWorkflowExecutorEngine:

    def execute(self, topic):

        return {"topic": topic, "workflow": True, "executed": True}

    def info(self):

        return {"engine": "Article Workflow Executor Engine", "version": "1.0"}
