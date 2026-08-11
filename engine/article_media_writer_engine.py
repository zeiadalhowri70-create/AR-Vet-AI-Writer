# -*- coding: utf-8 -*-


class ArticleMediaWriterEngine:

    def write(self, topic):

        return {"section": "media", "topic": topic, "generated": True}

    def info(self):

        return {"engine": "Article Media Writer Engine", "version": "1.0"}
