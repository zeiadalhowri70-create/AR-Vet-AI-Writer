# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticleAutomationOrchestrationEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def build_pipeline(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        data = node.get("data", {})

        return {
            "id": node_id,
            "title": data.get("name_ar", node_id),
            "pipeline": [
                "knowledge",
                "content_structure",
                "seo",
                "schema",
                "html",
                "quality_check",
                "publication",
            ],
            "automation_ready": True,
        }

    def info(self):

        return {
            "engine": "Graph Article Automation Orchestration Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
