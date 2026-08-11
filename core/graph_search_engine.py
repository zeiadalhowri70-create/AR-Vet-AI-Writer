# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphSearchEngine:

    def __init__(self):
        self.graph = GraphBuilder().build()

    def find_node(self, node_id):

        return self.graph.nodes.get(node_id)

    def find_by_type(self, node_type):

        return {k: v for k, v in self.graph.nodes.items() if v.get("type") == node_type}

    def search(self, keyword):

        keyword = keyword.lower()

        result = {}

        for node_id, node in self.graph.nodes.items():

            name = str(node.get("name", "")).lower()

            if keyword in node_id.lower() or keyword in name:
                result[node_id] = node

        return result

    def info(self):

        return {
            "engine": "Graph Search Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
        }
