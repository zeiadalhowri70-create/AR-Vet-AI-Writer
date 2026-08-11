# -*- coding: utf-8 -*-


class ArticleComponentConnectorEngine:

    def connect(self, topic):

        return {"topic": topic, "connected": True}

    def info(self):

        return {"engine": "Article Component Connector Engine", "version": "1.0"}
