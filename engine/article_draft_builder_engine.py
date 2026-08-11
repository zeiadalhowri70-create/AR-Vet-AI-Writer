# -*- coding: utf-8 -*-


class ArticleDraftBuilderEngine:

    def build(self, topic):

        return {"topic": topic, "draft_ready": True}

    def info(self):

        return {"engine": "Article Draft Builder Engine", "version": "1.0"}
