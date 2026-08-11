# -*- coding: utf-8 -*-


class ArticleContentCollectorEngine:

    def collect(self, topic):

        return {"topic": topic, "content_collected": True}

    def info(self):

        return {"engine": "Article Content Collector Engine", "version": "1.0"}
