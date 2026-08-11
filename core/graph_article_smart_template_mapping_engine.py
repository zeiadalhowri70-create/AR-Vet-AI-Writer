# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticleSmartTemplateMappingEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def map_template(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        data = node.get("data", {})

        relations = [
            {"relation": e["relation"], "target": e["target"]}
            for e in self.graph.edges
            if e["source"] == node_id
        ]

        return {
            "id": node_id,
            "template": {
                "title": data.get("name_ar", node_id),
                "type": node.get("type"),
                "sections": [
                    "introduction",
                    "definition",
                    "cause",
                    "host",
                    "symptoms",
                    "diagnosis",
                    "prevention",
                ],
                "knowledge": data,
                "relations": relations,
            },
            "template_ready": True,
        }

    def info(self):

        return {
            "engine": "Graph Article Smart Template Mapping Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
