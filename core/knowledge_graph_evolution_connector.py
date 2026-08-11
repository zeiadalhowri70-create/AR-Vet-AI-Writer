# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Knowledge Graph Evolution Connector

Stage 2.9.1
"""


class KnowledgeGraphEvolutionConnector:

    VERSION = "1.0.0"

    def __init__(self, graph, knowledge_manager):

        self.graph = graph
        self.knowledge_manager = knowledge_manager
        self.changes = []

    def evolve_disease(self, disease_id, pattern):

        result = {"disease": disease_id, "pattern": pattern, "updated": False}

        exists = False

        for edge in self.graph.edges:

            if (
                edge["source"] == disease_id
                and edge["relation"] == "has_pattern"
                and edge["target"] == pattern
            ):

                exists = True
                break

        if not exists:

            self.graph.add_edge(disease_id, "has_pattern", pattern)

            result["updated"] = True

        self.changes.append(result)

        return result

    def evolution_history(self):

        return self.changes

    def health(self):

        return {
            "status": True,
            "engine": "Knowledge Graph Evolution Connector",
            "version": self.VERSION,
        }
