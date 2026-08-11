# -*- coding: utf-8 -*-


class ArticlePublishWriterEngine:

    def write(self, topic):

        return {"section": "publish", "topic": topic, "generated": True}

    def info(self):

        return {"engine": "Article Publish Writer Engine", "version": "1.0"}
