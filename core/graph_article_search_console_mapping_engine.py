# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticleSearchConsoleMappingEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def search_console_data(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        data = node.get("data", {})

        return {
            "title": data.get("name_ar", node_id),
            "index_ready": True,
            "sitemap_ready": True,
            "url_inspection_ready": True,
            "mobile_ready": True,
            "schema_ready": True,
        }

    def info(self):

        return {
            "engine": "Graph Article Search Console Mapping Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
