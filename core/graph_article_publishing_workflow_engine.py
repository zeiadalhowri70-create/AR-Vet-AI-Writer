# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticlePublishingWorkflowEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def workflow(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        data = node.get("data", {})

        return {
            "id": node_id,
            "title": data.get("name_ar", node_id),
            "stages": {
                "draft": True,
                "review": True,
                "seo_check": True,
                "publication": True,
            },
            "blogger_ready": True,
            "workflow_ready": True,
        }

    def info(self):

        return {
            "engine": "Graph Article Publishing Workflow Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
