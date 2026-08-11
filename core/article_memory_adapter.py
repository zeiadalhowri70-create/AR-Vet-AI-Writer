# -*- coding: utf-8 -*-
"""
AR-Vet AI Writer
Article Memory Integration Adapter
"""

from core.article_memory_engine import ArticleMemoryEngine


class ArticleMemoryAdapter:

    VERSION = "1.0.0"

    def __init__(self):

        self.memory = ArticleMemoryEngine()

    def store_article(self, article):

        title = article.get("title", "Untitled")

        content = article.get("content", "")

        result = self.memory.save_article(title, content)

        return {
            "status": result["status"],
            "adapter": "Article Memory Adapter",
            "title": title,
            "version": self.VERSION,
        }

    def health(self):

        return {
            "status": True,
            "adapter": "Article Memory Adapter",
            "version": self.VERSION,
        }
