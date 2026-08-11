# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticleStructuredDataMappingEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def structured_data(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        data = node.get("data", {})

        return {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": data.get("name_ar", node_id),
            "about": {
                "@type": "MedicalCondition",
                "name": data.get("name_ar", node_id),
            },
            "keywords": [value for value in data.values() if isinstance(value, str)],
            "schema_ready": True,
        }

    def info(self):

        return {
            "engine": "Graph Article Structured Data Mapping Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
