# -*- coding: utf-8 -*-


class ArticleFinalizationEngine:

    def finalize(self, topic):

        return {"topic": topic, "finalized": True}

    def info(self):

        return {"engine": "Article Finalization Engine", "version": "1.0"}
