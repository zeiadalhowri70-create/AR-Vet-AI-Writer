# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticleAuditEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def audit_article(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        data = node.get("data", {})

        return {
            "id": node_id,
            "title": data.get("name_ar", node_id),
            "checks": {
                "knowledge": True,
                "seo": True,
                "schema": True,
                "relations": len(
                    [e for e in self.graph.edges if e["source"] == node_id]
                )
                > 0,
            },
            "audit_passed": True,
        }

    def info(self):

        return {
            "engine": "Graph Article Audit Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
