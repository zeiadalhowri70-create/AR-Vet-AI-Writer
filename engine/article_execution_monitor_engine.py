# -*- coding: utf-8 -*-


class ArticleExecutionMonitorEngine:

    def monitor(self, topic):

        return {"topic": topic, "execution_monitor": True}

    def info(self):

        return {"engine": "Article Execution Monitor Engine", "version": "1.0"}
