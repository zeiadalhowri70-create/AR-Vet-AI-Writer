# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Writer Context Bridge

Stage 3.6.B.3
"""

from core.article_context_injection_engine import ArticleContextInjectionEngine


class WriterContextBridge:

    VERSION = "1.0.0"

    def __init__(self):

        self.context_engine = ArticleContextInjectionEngine()
        self.context = {}

    def prepare(self, disease_id):
        result = self.context_engine.inject(disease_id)

        if isinstance(result, dict):
            result["disease_profile"] = result.get("knowledge", {})
            result["disease_id"] = disease_id

        self.context = result
        return result

    def get_context(self):

        return self.context

    def health(self):

        return {
            "status": True,
            "engine": "Writer Context Bridge",
            "version": self.VERSION,
        }
