# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Production Integration Engine Connector

Connector for ArticleWriterIntegrationEngine.
"""


class IntegrationEngineConnector:

    VERSION = "1.0.0"

    def __init__(self, engine=None):

        self.engine = engine

    def generate(self, topic):

        if not self.engine:

            return {
                "status": False,
                "error": "ArticleWriterIntegrationEngine unavailable",
                "topic": topic,
            }

        result = self.engine.generate(topic)

        return {
            "status": True,
            "topic": topic,
            "output": result,
            "version": self.VERSION,
        }

    def health(self):

        return {
            "status": True,
            "version": self.VERSION,
            "engine_connected": self.engine is not None,
        }


if __name__ == "__main__":

    connector = IntegrationEngineConnector()

    print(connector.health())

    print(connector.generate("مرض النيوكاسل في الدواجن"))
