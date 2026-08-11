# -*- coding: utf-8 -*-
"""
AR-Vet AI Writer
Optimization Memory Adapter
"""

from core.optimization_loop_engine import OptimizationLoopEngine


class OptimizationMemoryAdapter:

    VERSION = "1.0.0"

    def __init__(self):

        self.engine = OptimizationLoopEngine()

    def save_optimization_plan(self, analysis, recommendation):

        return self.engine.create_optimization_plan(analysis, recommendation)

    def get_optimization_history(self):

        return self.engine.get_actions()

    def health(self):

        return {
            "status": True,
            "adapter": "Optimization Memory Adapter",
            "version": self.VERSION,
        }
