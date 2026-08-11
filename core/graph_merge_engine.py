# -*- coding: utf-8 -*-

from copy import deepcopy

from core.graph_builder import GraphBuilder


class GraphMergeEngine:

    def __init__(self):
        self.graph = GraphBuilder().build()

    def merge(self, nodes=None, edges=None):

        graph = deepcopy(self.graph)

        nodes = nodes or {}
        edges = edges or []

        for node_id, node in nodes.items():
            graph.nodes[node_id] = node

        for edge in edges:
            if edge not in graph.edges:
                graph.edges.append(edge)

        return graph

    def info(self):

        return {
            "engine": "Graph Merge Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
