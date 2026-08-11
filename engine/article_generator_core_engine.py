# -*- coding: utf-8 -*-


class ArticleGeneratorCoreEngine:

    def generate(self, topic):

        return {"topic": topic, "core": True, "generated": True}

    def info(self):

        return {"engine": "Article Generator Core Engine", "version": "1.0"}
