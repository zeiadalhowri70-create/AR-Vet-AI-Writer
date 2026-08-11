# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticleMultiLanguageMappingEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def language_data(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        data = node.get("data", {})

        return {
            "id": node_id,
            "languages": {
                "ar": {"name": data.get("name_ar", node_id)},
                "en": {"name": data.get("name_en", node_id)},
            },
            "translation_ready": True,
        }

    def info(self):

        return {
            "engine": "Graph Article Multi Language Mapping Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
