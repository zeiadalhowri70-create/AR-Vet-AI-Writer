# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticleAIPostProcessingEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def process(self, node_id, content):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        cleaned = " ".join(content.split())

        return {
            "id": node_id,
            "title": node.get("data", {}).get("name_ar", node_id),
            "content": cleaned,
            "processed": True,
            "publication_ready": True,
        }

    def info(self):

        return {
            "engine": "Graph Article AI Post Processing Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
