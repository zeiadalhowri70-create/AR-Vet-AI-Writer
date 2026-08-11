# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticleBloggerMappingEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def blogger_data(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        data = node.get("data", {})

        return {
            "title": data.get("name_ar", node_id),
            "labels": [data.get("category", ""), node.get("type", "")],
            "description": f"مقال بيطري علمي عن {
                data.get(
                    'name_ar', node_id)}",
            "publish_ready": True,
        }

    def info(self):

        return {
            "engine": "Graph Article Blogger Mapping Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
