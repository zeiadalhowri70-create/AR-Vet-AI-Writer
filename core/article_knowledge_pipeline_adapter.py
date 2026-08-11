# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Article Knowledge Pipeline Adapter

Stage 3.6.B.1
"""

from core.graph_loader import GraphLoader
from core.graph_adapter import GraphAdapter
from core.disease_knowledge_fusion_engine import DiseaseKnowledgeFusionEngine
from core.article_writer_context_adapter import ArticleWriterContextAdapter


class ArticleKnowledgePipelineAdapter:

    VERSION = "1.0.0"

    def __init__(self):

        data = GraphLoader().load("diseases.json")

        self.graph = GraphAdapter().from_dict(data)

        self.fusion = DiseaseKnowledgeFusionEngine(self.graph)

        self.context_adapter = ArticleWriterContextAdapter()

    def build_context(self, disease_id):

        knowledge = self.fusion.fuse(disease_id)

        if not knowledge.get("found"):

            return {"status": False, "disease_id": disease_id}

        context = self.context_adapter.build(knowledge)

        return {
            "status": True,
            "disease_id": disease_id,
            "knowledge": knowledge,
            "disease_profile": knowledge,
            "context": context,
        }

    def health(self):

        return {
            "status": True,
            "engine": "Article Knowledge Pipeline Adapter",
            "version": self.VERSION,
        }
