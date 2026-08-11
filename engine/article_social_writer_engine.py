# -*- coding: utf-8 -*-


class ArticleSocialWriterEngine:

    def write(self, topic):

        return {"section": "social", "topic": topic, "generated": True}

    def info(self):

        return {"engine": "Article Social Writer Engine", "version": "1.0"}
