# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Production Article Builder Connector

Connector for ArticleRealContentBuilderEngine.
"""


class ArticleBuilderConnector:

    VERSION = "1.0.0"

    def __init__(self, builder=None):

        self.builder = builder

    def build(self, topic):

        if not self.builder:

            return {
                "status": False,
                "error": "ArticleRealContentBuilderEngine unavailable",
                "topic": topic,
            }

        article = self.builder.build(topic)

        return {
            "status": True,
            "topic": topic,
            "sections": article,
            "version": self.VERSION,
        }

    def health(self):

        return {
            "status": True,
            "version": self.VERSION,
            "builder_connected": self.builder is not None,
        }


if __name__ == "__main__":

    connector = ArticleBuilderConnector()

    print(connector.health())

    print(connector.build("مرض النيوكاسل في الدواجن"))
