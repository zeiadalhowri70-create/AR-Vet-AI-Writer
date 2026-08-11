# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Production Video Metadata Engine Adapter

Generates video metadata package.
"""


class VideoMetadataEngineAdapter:

    VERSION = "1.0.0"

    def __init__(self, engine=None):

        self.engine = engine

    def generate(self, article):

        if not self.engine:

            return {
                "title": f"{article} - شرح بيطري شامل",
                "description": (
                    f"فيديو علمي يشرح {article} " "وأهم المعلومات البيطرية."
                ),
                "tags": ["طب بيطري", "دواجن", article],
            }

        return self.engine.generate(article)

    def health(self):

        return {
            "status": True,
            "version": self.VERSION,
            "engine_connected": self.engine is not None,
        }


if __name__ == "__main__":

    adapter = VideoMetadataEngineAdapter()

    print(adapter.health())

    print(adapter.generate("مرض النيوكاسل في الدواجن"))
