# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Graph Adapter Engine

Converts JSON graph data into KnowledgeGraph object.
"""

from core.knowledge_graph import KnowledgeGraph


class GraphAdapter:

    VERSION = "1.0.0"

    def from_dict(self, data):

        graph = KnowledgeGraph()

        for node in data.get("nodes", []):

            graph.add_node(node.get("id"), node.get("type"), node.get("data", {}))

        for edge in data.get("edges", []):

            graph.add_edge(edge.get("source"), edge.get("relation"), edge.get("target"))

        return graph

    def health(self):

        return {
            "status": True,
            "engine": "Graph Adapter Engine",
            "version": self.VERSION,
        }
