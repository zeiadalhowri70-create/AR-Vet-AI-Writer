# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticleAnalyticsEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def analyze_article(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        relations = [e for e in self.graph.edges if e["source"] == node_id]

        return {
            "id": node_id,
            "title": node.get("data", {}).get("name_ar", node_id),
            "metrics": {
                "knowledge_score": 100,
                "seo_score": 100,
                "relation_count": len(relations),
                "content_ready": True,
            },
            "analytics_ready": True,
        }

    def info(self):

        return {
            "engine": "Graph Article Analytics Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
