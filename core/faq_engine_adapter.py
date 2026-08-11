# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Production FAQ Engine Adapter

Connector for FAQ generation.
"""


class FAQEngineAdapter:

    VERSION = "1.0.0"

    def __init__(self, engine=None):

        self.engine = engine

    def generate(self, article):

        if not self.engine:

            return {
                "faq": [
                    {"question": f"ما هو {article}؟", "answer": "معلومات علمية بيطرية."}
                ]
            }

        return self.engine.generate(article)

    def health(self):

        return {
            "status": True,
            "version": self.VERSION,
            "engine_connected": self.engine is not None,
        }


if __name__ == "__main__":

    adapter = FAQEngineAdapter()

    print(adapter.health())

    print(adapter.generate("مرض النيوكاسل في الدواجن"))
