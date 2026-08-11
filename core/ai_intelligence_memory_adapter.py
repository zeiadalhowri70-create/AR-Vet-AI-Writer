# -*- coding: utf-8 -*-
"""
AR-Vet AI Writer
AI Intelligence Memory Adapter
"""

from core.ai_intelligence_orchestrator import AIIntelligenceOrchestrator


class AIIntelligenceMemoryAdapter:

    VERSION = "1.0.0"

    def __init__(self):

        self.engine = AIIntelligenceOrchestrator()

    def save_cycle(self, report, recommendation):

        return self.engine.run_cycle(report, recommendation)

    def get_history(self):

        return self.engine.get_pipeline()

    def health(self):

        return {
            "status": True,
            "adapter": "AI Intelligence Memory Adapter",
            "version": self.VERSION,
        }
