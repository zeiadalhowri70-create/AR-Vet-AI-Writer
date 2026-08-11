# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphValidatorAdvancedEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def check_duplicate_nodes(self):

        ids = list(self.graph.nodes.keys())

        return len(ids) != len(set(ids))

    def check_duplicate_edges(self):

        edges = [
            (edge["source"], edge["relation"], edge["target"])
            for edge in self.graph.edges
        ]

        return len(edges) != len(set(edges))

    def check_empty_nodes(self):

        return [node_id for node_id, node in self.graph.nodes.items() if not node]

    def validate(self):

        return {
            "duplicate_nodes": self.check_duplicate_nodes(),
            "duplicate_edges": self.check_duplicate_edges(),
            "empty_nodes": self.check_empty_nodes(),
            "valid": (
                not self.check_duplicate_nodes()
                and not self.check_duplicate_edges()
                and not self.check_empty_nodes()
            ),
        }

    def info(self):

        return {
            "engine": "Graph Validator Advanced Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
