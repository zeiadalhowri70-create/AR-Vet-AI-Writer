# -*- coding: utf-8 -*-
"""
AR-Vet AI Writer
Article Evolution Memory Adapter
"""

from core.article_evolution_engine import ArticleEvolutionEngine


class ArticleEvolutionMemoryAdapter:

    VERSION = "1.0.0"

    def __init__(self):

        self.engine = ArticleEvolutionEngine()

    def save_article_version(self, article, version):

        return self.engine.create_version(article, version)

    def get_history(self):

        return self.engine.get_versions()

    def health(self):

        return {
            "status": True,
            "adapter": "Article Evolution Memory Adapter",
            "version": self.VERSION,
        }
