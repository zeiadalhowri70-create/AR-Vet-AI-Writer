# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticleQualityScoringEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def score_article(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        score = 0

        data = node.get("data", {})

        if data:
            score += 3

        relations = [edge for edge in self.graph.edges if edge["source"] == node_id]

        if relations:
            score += len(relations)

        if node.get("type"):
            score += 2

        return {
            "node": node_id,
            "score": score,
            "quality": "high" if score >= 5 else "medium",
        }

    def info(self):

        return {
            "engine": "Graph Article Quality Scoring Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
