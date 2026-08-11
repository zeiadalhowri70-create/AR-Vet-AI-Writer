# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticleKnowledgeFusionEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def fuse_article_knowledge(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        data = node.get("data", {})

        relations = []

        for edge in self.graph.edges:

            if edge["source"] == node_id:

                relations.append(
                    {"relation": edge["relation"], "target": edge["target"]}
                )

        return {
            "id": node_id,
            "title": data.get("name_ar", node_id),
            "type": node.get("type"),
            "knowledge": data,
            "relations": relations,
            "fusion_ready": True,
        }

    def info(self):

        return {
            "engine": "Graph Article Knowledge Fusion Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
