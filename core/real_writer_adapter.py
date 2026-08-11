# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Production Real Writer Adapter

Connects real article builder engines.
"""


class RealWriterAdapter:

    VERSION = "1.0.0"

    def __init__(self, builder=None):

        self.builder = builder

    def generate(self, topic):

        if not self.builder:

            return {
                "status": False,
                "error": "Article builder unavailable",
                "topic": topic,
            }

        result = self.builder.build(topic)

        return {
            "status": True,
            "topic": topic,
            "article": result,
            "version": self.VERSION,
        }

    def health(self):

        return {
            "status": True,
            "version": self.VERSION,
            "builder": self.builder is not None,
        }


if __name__ == "__main__":

    adapter = RealWriterAdapter()

    print(adapter.health())

    print(adapter.generate("مرض النيوكاسل في الدواجن"))
