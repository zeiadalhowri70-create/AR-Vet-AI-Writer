# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticleContentPersonalizationMappingEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def personalization_data(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        data = node.get("data", {})

        title = data.get("name_ar", node_id)

        return {
            "title": title,
            "audiences": ["veterinarian", "farmer", "student", "researcher"],
            "adaptable_content": True,
            "smart_article_ready": True,
        }

    def info(self):

        return {
            "engine": "Graph Article Content Personalization Mapping Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
