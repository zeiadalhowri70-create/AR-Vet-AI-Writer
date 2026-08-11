# -*- coding: utf-8 -*-

from collections import defaultdict

from core.graph_builder import GraphBuilder


class GraphClassificationEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def classify_by_type(self):

        result = defaultdict(list)

        for node_id, node in self.graph.nodes.items():

            result[node.get("type", "unknown")].append(node_id)

        return dict(result)

    def classify_by_attribute(self, key):

        result = defaultdict(list)

        for node_id, node in self.graph.nodes.items():

            value = node.get("data", {}).get(key)

            if value:

                result[value].append(node_id)

        return dict(result)

    def node_class(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        return {
            "id": node_id,
            "type": node.get("type"),
            "class": node.get("data", {}).get("category"),
        }

    def info(self):

        return {
            "engine": "Graph Classification Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
