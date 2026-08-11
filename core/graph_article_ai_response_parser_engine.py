# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticleAIResponseParserEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def parse(self, node_id, ai_text):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        return {
            "id": node_id,
            "title": node.get("data", {}).get("name_ar", node_id),
            "content": ai_text,
            "word_count": len(ai_text.split()),
            "parsed": True,
        }

    def info(self):

        return {
            "engine": "Graph Article AI Response Parser Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
