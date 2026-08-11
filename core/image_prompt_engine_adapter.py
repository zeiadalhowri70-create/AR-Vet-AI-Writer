# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Production Image Prompt Engine Adapter

Creates image generation prompts.
"""


class ImagePromptEngineAdapter:

    VERSION = "1.0.0"

    def __init__(self, engine=None):

        self.engine = engine

    def generate(self, article):

        if not self.engine:

            return {
                "prompt": (
                    f"صورة علمية بيطرية احترافية عن {article}, "
                    "أسلوب طبي واقعي، جودة عالية"
                )
            }

        return self.engine.generate(article)

    def health(self):

        return {
            "status": True,
            "version": self.VERSION,
            "engine_connected": self.engine is not None,
        }


if __name__ == "__main__":

    adapter = ImagePromptEngineAdapter()

    print(adapter.health())

    print(adapter.generate("مرض النيوكاسل في الدواجن"))
