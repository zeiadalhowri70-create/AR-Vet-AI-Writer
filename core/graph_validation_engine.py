# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphValidationEngine:

    def __init__(self):
        self.graph = GraphBuilder().build()

    def missing_nodes(self):

        missing = []

        node_ids = set(self.graph.nodes.keys())

        for edge in self.graph.edges:

            if edge["source"] not in node_ids:
                missing.append(edge["source"])

            if edge["target"] not in node_ids:
                missing.append(edge["target"])

        return sorted(set(missing))

    def is_valid(self):

        return len(self.missing_nodes()) == 0

    def validation_report(self):

        return {
            "valid": self.is_valid(),
            "missing_nodes": self.missing_nodes(),
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }

    def info(self):

        return {
            "engine": "Graph Validation Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
