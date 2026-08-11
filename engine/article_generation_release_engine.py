# -*- coding: utf-8 -*-


class ArticleGenerationReleaseEngine:

    def release(self, topic):
        return {"topic": topic, "released": True}

    def info(self):
        return {"engine": "Article Generation Release Engine", "version": "1.0"}
