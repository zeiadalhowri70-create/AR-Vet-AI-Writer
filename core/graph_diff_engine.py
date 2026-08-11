# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphDiffEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def compare(self, graph_a, graph_b):

        nodes_a = set(graph_a.get("nodes", {}).keys())
        nodes_b = set(graph_b.get("nodes", {}).keys())

        edges_a = set(str(edge) for edge in graph_a.get("edges", []))

        edges_b = set(str(edge) for edge in graph_b.get("edges", []))

        return {
            "added_nodes": list(nodes_b - nodes_a),
            "removed_nodes": list(nodes_a - nodes_b),
            "added_edges": list(edges_b - edges_a),
            "removed_edges": list(edges_a - edges_b),
        }

    def current_snapshot(self):

        return {"nodes": self.graph.nodes, "edges": self.graph.edges}

    def info(self):

        return {
            "engine": "Graph Diff Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
