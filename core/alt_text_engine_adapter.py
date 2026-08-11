# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Production ALT Text Engine Adapter

Generates SEO friendly image alt text.
"""


class ALTTextEngineAdapter:

    VERSION = "1.0.0"

    def __init__(self, engine=None):

        self.engine = engine

    def generate(self, article):

        if not self.engine:

            return {"alt_text": (f"صورة توضيحية عن {article} " "في الطب البيطري")}

        return self.engine.generate(article)

    def health(self):

        return {
            "status": True,
            "version": self.VERSION,
            "engine_connected": self.engine is not None,
        }


if __name__ == "__main__":

    adapter = ALTTextEngineAdapter()

    print(adapter.health())

    print(adapter.generate("مرض النيوكاسل في الدواجن"))
