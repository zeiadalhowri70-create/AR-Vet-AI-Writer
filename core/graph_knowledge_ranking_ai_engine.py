# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphKnowledgeRankingAIEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def calculate_score(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return 0

        score = 0

        node_type = node.get("type")

        if node_type == "disease":
            score += 5

        elif node_type == "pathogen":
            score += 3

        elif node_type == "animal":
            score += 2

        for edge in self.graph.edges:

            if edge["source"] == node_id or edge["target"] == node_id:
                score += 1

        return score

    def rank(self):

        result = {}

        for node_id in self.graph.nodes:

            result[node_id] = self.calculate_score(node_id)

        return dict(sorted(result.items(), key=lambda x: x[1], reverse=True))

    def top(self, limit=3):

        return list(self.rank().items())[:limit]

    def info(self):

        return {
            "engine": "Graph Knowledge Ranking AI Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
