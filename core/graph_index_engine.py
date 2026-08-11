# -*- coding: utf-8 -*-

from collections import defaultdict

from core.graph_builder import GraphBuilder


class GraphIndexEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()
        self.index = self.build_index()

    def build_index(self):

        index = defaultdict(list)

        for node_id, node in self.graph.nodes.items():

            node_type = node.get("type", "unknown")

            index[node_type].append(node_id)

        return dict(index)

    def get_by_type(self, node_type):

        return self.index.get(node_type, [])

    def all_indexes(self):

        return self.index

    def info(self):

        return {
            "engine": "Graph Index Engine",
            "version": "1.0",
            "indexes": len(self.index),
            "nodes": len(self.graph.nodes),
        }
