# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticleContentScoringIntelligenceEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def score_content(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        data = node.get("data", {})

        relations = [e for e in self.graph.edges if e["source"] == node_id]

        scientific = 100 if data.get("category") else 80
        seo = 100 if data.get("name_ar") and data.get("name_en") else 85
        structure = 100 if len(relations) > 0 else 80
        completeness = 100 if len(data) >= 4 else 85
        readability = 95

        overall = round((scientific + seo + structure + completeness + readability) / 5)

        if overall >= 95:
            status = "excellent"
        elif overall >= 85:
            status = "good"
        elif overall >= 70:
            status = "acceptable"
        else:
            status = "needs_improvement"

        return {
            "id": node_id,
            "scores": {
                "scientific": scientific,
                "seo": seo,
                "structure": structure,
                "completeness": completeness,
                "readability": readability,
            },
            "overall_score": overall,
            "status": status,
        }

    def info(self):

        return {
            "engine": "Graph Article Content Scoring Intelligence Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
