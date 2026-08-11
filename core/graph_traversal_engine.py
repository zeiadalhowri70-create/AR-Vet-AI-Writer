# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphTraversalEngine:

    def __init__(self):
        self.graph = GraphBuilder().build()

    def children(self, node_id):

        return [
            edge["target"] for edge in self.graph.edges if edge["source"] == node_id
        ]

    def parents(self, node_id):

        return [
            edge["source"] for edge in self.graph.edges if edge["target"] == node_id
        ]

    def relations(self, node_id):

        return [
            edge
            for edge in self.graph.edges
            if edge["source"] == node_id or edge["target"] == node_id
        ]

    def info(self):

        return {
            "engine": "Graph Traversal Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
