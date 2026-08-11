# -*- coding: utf-8 -*-

"""
Article Knowledge Intelligence Engine

AR-Vet AI Writer

Stage 3.6

Uses fused veterinary knowledge for article generation.
"""

from core.disease_knowledge_fusion_engine import DiseaseKnowledgeFusionEngine


class ArticleKnowledgeIntelligenceEngine:

    VERSION = "2.0.0"

    def __init__(self, graph, reasoning_engine):

        self.graph = graph

        self.reasoning_engine = reasoning_engine

        self.fusion = DiseaseKnowledgeFusionEngine(graph)

    def disease_summary(self, disease_id):

        return self.fusion.fuse(disease_id)

    def related_diseases(self, disease_id, limit=5):

        return self.reasoning_engine.differential_diagnosis(disease_id, limit)

    def comparison_data(self, disease_a, disease_b):

        return self.reasoning_engine.compare(disease_a, disease_b)

    def build_article_context(self, disease_id):

        knowledge = self.disease_summary(disease_id)

        return {
            "knowledge": knowledge,
            "disease": knowledge.get("basic", {}),
            "scientific_profile": knowledge.get("scientific_profile", {}),
            "differential": self.related_diseases(disease_id),
            "reasoning": self.reasoning_engine.explain_similarity(disease_id),
        }

    def info(self):

        return {
            "engine": "Article Knowledge Intelligence Engine",
            "version": self.VERSION,
            "status": "active",
        }
