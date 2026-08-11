# -*- coding: utf-8 -*-

from collections import Counter

from core.graph_builder import GraphBuilder


class GraphAnalyzerEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def most_connected_nodes(self):

        counter = Counter()

        for edge in self.graph.edges:

            counter[edge["source"]] += 1
            counter[edge["target"]] += 1

        return dict(counter.most_common())

    def node_degree(self, node_id):

        degree = 0

        for edge in self.graph.edges:

            if edge["source"] == node_id:
                degree += 1

            if edge["target"] == node_id:
                degree += 1

        return degree

    def graph_density(self):

        nodes = len(self.graph.nodes)

        if nodes <= 1:
            return 0

        possible_edges = nodes * (nodes - 1)

        return round(len(self.graph.edges) / possible_edges, 4)

    def info(self):

        return {
            "engine": "Graph Analyzer Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
