# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphKnowledgeEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def get_knowledge(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        return {
            "id": node_id,
            "type": node.get("type"),
            "data": node.get("data"),
            "relations": [
                edge
                for edge in self.graph.edges
                if edge["source"] == node_id or edge["target"] == node_id
            ],
        }

    def find_knowledge(self, keyword):

        keyword = keyword.lower()

        result = {}

        for node_id, node in self.graph.nodes.items():

            text = str(node).lower()

            if keyword in node_id.lower() or keyword in text:
                result[node_id] = node

        return result

    def knowledge_count(self):

        return len(self.graph.nodes)

    def info(self):

        return {
            "engine": "Graph Knowledge Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
