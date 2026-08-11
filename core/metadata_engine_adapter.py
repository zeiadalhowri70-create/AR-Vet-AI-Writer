# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Production Metadata Engine Adapter

Connector for SEO metadata generation.
"""


class MetadataEngineAdapter:

    VERSION = "1.0.0"

    def __init__(self, engine=None):

        self.engine = engine

    def generate(self, article):

        if not self.engine:

            return {"title": article, "description": "", "keywords": []}

        return self.engine.generate(article)

    def health(self):

        return {
            "status": True,
            "version": self.VERSION,
            "engine_connected": self.engine is not None,
        }


if __name__ == "__main__":

    adapter = MetadataEngineAdapter()

    print(adapter.health())

    print(adapter.generate("مرض النيوكاسل في الدواجن"))
