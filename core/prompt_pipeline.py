# -*- coding: utf-8 -*-

"""
Prompt Pipeline
AR-Vet AI Writer

Stage 3.1.4.C
"""

from core.prompt_context_engine import PromptContextEngine


class PromptPipeline:

    def __init__(self):

        self.context_engine = PromptContextEngine()

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

        return self.context_engine.build(
            knowledge=knowledge,
            rag_context=rag_context,
            references=references,
            image_context=image_context,
            audio_context=audio_context,
            graph_context=graph_context,
            seo_context=seo_context,
        )

    def info(self):

        return {"engine": "Prompt Pipeline", "version": "1.0"}
