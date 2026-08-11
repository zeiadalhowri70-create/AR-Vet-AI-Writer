# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticleContentValidationIntelligenceEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def validate_content(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        data = node.get("data", {})

        relations = [e for e in self.graph.edges if e["source"] == node_id]

        checks = {
            "title_exists": bool(data.get("name_ar")),
            "knowledge_exists": bool(data),
            "relations_exists": len(relations) > 0,
        }

        return {
            "id": node_id,
            "checks": checks,
            "valid": all(checks.values()),
            "content_validation_ready": True,
        }

    def info(self):

        return {
            "engine": "Graph Article Content Validation Intelligence Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
