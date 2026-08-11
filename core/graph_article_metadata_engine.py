# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticleMetadataEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def generate_metadata(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        data = node.get("data", {})

        return {
            "title": data.get("name_ar", node_id),
            "description": f"معلومات علمية عن {data.get('name_ar', node_id)}",
            "keywords": [str(v) for v in data.values() if isinstance(v, str)],
            "category": data.get("category", ""),
            "type": node.get("type"),
        }

    def info(self):

        return {
            "engine": "Graph Article Metadata Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
