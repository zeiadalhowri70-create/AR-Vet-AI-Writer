# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphSemanticEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def semantic_search(self, keyword):

        keyword = keyword.lower()

        results = {}

        for node_id, node in self.graph.nodes.items():

            data = node.get("data", {})

            text = " ".join(str(value) for value in data.values()).lower()

            if (
                keyword in node_id.lower()
                or keyword in text
                or keyword in str(node.get("type", "")).lower()
            ):

                results[node_id] = node

        return results

    def node_meaning(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        return {
            "id": node_id,
            "concept": node.get("type"),
            "attributes": node.get("data", {}),
        }

    def info(self):

        return {
            "engine": "Graph Semantic Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
