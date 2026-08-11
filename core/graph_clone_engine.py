# -*- coding: utf-8 -*-

from copy import deepcopy

from core.graph_builder import GraphBuilder


class GraphCloneEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def clone(self):

        return deepcopy({"nodes": self.graph.nodes, "edges": self.graph.edges})

    def clone_node(self, node_id):

        if node_id not in self.graph.nodes:
            return None

        return deepcopy(self.graph.nodes[node_id])

    def info(self):

        return {
            "engine": "Graph Clone Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
