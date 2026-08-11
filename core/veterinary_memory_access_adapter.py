# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Veterinary Memory Access Adapter

Stage 2.8.1.A
"""


class VeterinaryMemoryAccessAdapter:

    VERSION = "1.0.0"

    def __init__(self, memory_engine):

        self.memory_engine = memory_engine

    def get_all(self):

        if hasattr(self.memory_engine, "cases"):
            return self.memory_engine.cases

        if hasattr(self.memory_engine, "memory"):
            return self.memory_engine.memory

        if hasattr(self.memory_engine, "get_cases"):
            return self.memory_engine.get_cases()

        return []

    def health(self):

        return {
            "status": True,
            "engine": "Veterinary Memory Access Adapter",
            "version": self.VERSION,
        }
