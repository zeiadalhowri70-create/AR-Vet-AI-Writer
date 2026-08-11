# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticleGoogleSEOOptimizationMappingEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def google_seo_data(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        data = node.get("data", {})

        title = data.get("name_ar", node_id)

        keywords = [value for value in data.values() if isinstance(value, str)]

        return {
            "seo_title": title,
            "meta_description": f"دليل علمي شامل عن {title} في الطب البيطري",
            "keywords": keywords,
            "search_engine_ready": True,
            "schema_ready": True,
        }

    def info(self):

        return {
            "engine": "Graph Article Google SEO Optimization Mapping Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
