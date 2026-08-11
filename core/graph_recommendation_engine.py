# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphRecommendationEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def recommend(self, node_id):

        recommendations = []

        connected = set()

        for edge in self.graph.edges:

            if edge["source"] == node_id:

                connected.add(edge["target"])

            elif edge["target"] == node_id:

                connected.add(edge["source"])

        for node in connected:

            recommendations.append({"node": node, "reason": "direct_relation"})

        return recommendations

    def recommend_by_type(self, node_id, node_type):

        results = []

        for item in self.recommend(node_id):

            node = self.graph.nodes.get(item["node"])

            if node and node.get("type") == node_type:

                results.append(item)

        return results

    def info(self):

        return {
            "engine": "Graph Recommendation Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
