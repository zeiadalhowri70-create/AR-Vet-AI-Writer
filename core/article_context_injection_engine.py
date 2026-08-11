# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Article Context Injection Engine

Stage 3.6.B.2
"""

from core.article_knowledge_pipeline_adapter import ArticleKnowledgePipelineAdapter


class ArticleContextInjectionEngine:

    VERSION = "1.0.0"

    def __init__(self):

        self.knowledge_pipeline = ArticleKnowledgePipelineAdapter()

    def inject(self, disease_id):

        result = self.knowledge_pipeline.build_context(disease_id)

        if not result.get("status"):

            return {"status": False, "disease_id": disease_id, "context": ""}

        return {
            "status": True,
            "disease_id": disease_id,
            "context": result.get("context", ""),
            "knowledge": result.get("knowledge", {}),
        }

    def health(self):

        return {
            "status": True,
            "engine": "Article Context Injection Engine",
            "version": self.VERSION,
        }
