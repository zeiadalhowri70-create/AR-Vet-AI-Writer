# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Brain To Article Knowledge Adapter

Stage 3.1
"""


class BrainToArticleKnowledgeAdapter:

    VERSION = "1.0.0"

    def __init__(self, brain_pipeline=None):

        self.brain_pipeline = brain_pipeline

    def adapt(self, brain_result):

        case = brain_result.get("case", {})

        analysis = brain_result.get("stages", {}).get("brain_analysis", {})

        return {
            "source": "Veterinary Brain",
            "animal": case.get("animal", ""),
            "symptoms": case.get("symptoms", []),
            "brain_status": analysis.get("brain_status", ""),
            "article_context": {
                "topic": case.get("disease", ""),
                "clinical_basis": case.get("symptoms", []),
                "knowledge_source": "AR-Vet Veterinary Brain",
            },
        }

    def health(self):

        return {
            "status": True,
            "engine": "Brain To Article Knowledge Adapter",
            "version": self.VERSION,
        }
