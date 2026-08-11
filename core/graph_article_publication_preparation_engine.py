# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticlePublicationPreparationEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def prepare_article(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        data = node.get("data", {})

        return {
            "id": node_id,
            "title": data.get("name_ar", node_id),
            "type": node.get("type"),
            "status": "ready",
            "seo_ready": True,
            "graph_ready": True,
        }

    def info(self):

        return {
            "engine": "Graph Article Publication Preparation Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
