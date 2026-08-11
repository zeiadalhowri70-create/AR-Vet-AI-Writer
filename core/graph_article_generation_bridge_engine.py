# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticleGenerationBridgeEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def get_article_data(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        article_data = {
            "title": node.get("data", {}).get("name_ar", node_id),
            "type": node.get("type"),
            "information": node.get("data", {}),
            "relations": [],
        }

        for edge in self.graph.edges:

            if edge["source"] == node_id:

                article_data["relations"].append(
                    {"relation": edge["relation"], "target": edge["target"]}
                )

        return article_data

    def generate_outline(self, node_id):

        data = self.get_article_data(node_id)

        if not data:
            return None

        return {
            "title": data["title"],
            "sections": [
                "التعريف بالمرض",
                "المسبب",
                "العائل",
                "العلاقات المرضية",
                "الوقاية والسيطرة",
            ],
            "knowledge": data,
        }

    def info(self):

        return {
            "engine": "Graph Article Generation Bridge Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
