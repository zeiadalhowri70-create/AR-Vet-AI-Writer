# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticleRecommendationIntelligenceEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def recommend_articles(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        recommendations = []

        for edge in self.graph.edges:

            if edge["source"] == node_id:

                target = self.graph.nodes.get(edge["target"])

                if target:

                    recommendations.append(
                        {"node": edge["target"], "reason": edge["relation"]}
                    )

        return {
            "source": node_id,
            "recommendations": recommendations,
            "smart_recommendation_ready": True,
        }

    def info(self):

        return {
            "engine": "Graph Article Recommendation Intelligence Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
