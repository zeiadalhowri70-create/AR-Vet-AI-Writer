# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Production Writer Engine Adapter

Unified interface for writer engines.
"""


class WriterEngineAdapter:

    VERSION = "1.0.0"

    def __init__(self, writer_engine=None):

        self.writer_engine = writer_engine

    def build(self, topic):

        if not self.writer_engine:

            return {
                "status": False,
                "error": "Writer engine unavailable",
                "topic": topic,
            }

        result = self.writer_engine.build(topic)

        return {
            "status": True,
            "topic": topic,
            "content": result,
            "version": self.VERSION,
        }

    def health(self):

        return {
            "status": True,
            "version": self.VERSION,
            "writer_engine": self.writer_engine is not None,
        }


if __name__ == "__main__":

    adapter = WriterEngineAdapter()

    print(adapter.health())

    print(adapter.build("مرض النيوكاسل في الدواجن"))
