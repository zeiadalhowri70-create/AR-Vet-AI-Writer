# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphMonitorEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def node_count(self):

        return len(self.graph.nodes)

    def edge_count(self):

        return len(self.graph.edges)

    def health(self):

        return {
            "status": "healthy",
            "nodes": self.node_count(),
            "edges": self.edge_count(),
        }

    def detect_isolated_nodes(self):

        connected = set()

        for edge in self.graph.edges:

            connected.add(edge["source"])
            connected.add(edge["target"])

        return [node_id for node_id in self.graph.nodes if node_id not in connected]

    def info(self):

        return {
            "engine": "Graph Monitor Engine",
            "version": "1.0",
            "nodes": self.node_count(),
            "edges": self.edge_count(),
        }
