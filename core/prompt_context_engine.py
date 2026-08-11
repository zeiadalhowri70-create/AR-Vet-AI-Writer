# -*- coding: utf-8 -*-

"""
Prompt Context Engine
AR-Vet AI Writer

Stage 3.1.4.A
"""


class PromptContextEngine:

    def build(
        self,
        knowledge=None,
        rag_context="",
        references=None,
        image_context="",
        audio_context="",
        graph_context="",
        seo_context="",
    ):

        context = {
            "knowledge": knowledge,
            "rag_context": rag_context,
            "references": references or [],
            "image_context": image_context,
            "audio_context": audio_context,
            "graph_context": graph_context,
            "seo_context": seo_context,
        }

        return context

    def info(self):

        return {
            "engine": "Prompt Context Engine",
            "version": "1.0",
            "supported_sources": [
                "knowledge",
                "rag_context",
                "references",
                "image_context",
                "audio_context",
                "graph_context",
                "seo_context",
            ],
        }
