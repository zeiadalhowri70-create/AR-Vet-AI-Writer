# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphSEOKnowledgeEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def seo_data(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        data = node.get("data", {})

        keywords = []

        for value in data.values():

            if isinstance(value, str):

                keywords.append(value)

        return {
            "title": data.get("name_ar", node_id),
            "keywords": keywords,
            "category": data.get("category", ""),
            "type": node.get("type"),
        }

    def related_keywords(self, node_id):

        result = []

        for edge in self.graph.edges:

            if edge["source"] == node_id:

                target = self.graph.nodes.get(edge["target"])

                if target:

                    result.extend([str(v) for v in target.get("data", {}).values()])

        return result

    def info(self):

        return {
            "engine": "Graph SEO Knowledge Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
