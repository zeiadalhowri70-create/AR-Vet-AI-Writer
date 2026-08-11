# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Production Schema Engine Adapter

Connector for Schema.org generation.
"""


class SchemaEngineAdapter:

    VERSION = "1.0.0"

    def __init__(self, engine=None):

        self.engine = engine

    def generate(self, article):

        if not self.engine:

            return {
                "@context": "https://schema.org",
                "@type": "Article",
                "headline": article,
            }

        return self.engine.generate(article)

    def health(self):

        return {
            "status": True,
            "version": self.VERSION,
            "engine_connected": self.engine is not None,
        }


if __name__ == "__main__":

    adapter = SchemaEngineAdapter()

    print(adapter.health())

    print(adapter.generate("مرض النيوكاسل في الدواجن"))
