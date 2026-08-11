# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticleReferenceMappingEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def generate_references(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        data = node.get("data", {})

        references = []

        references.append(
            {
                "topic": data.get("name_ar", node_id),
                "type": node.get("type"),
                "category": data.get("category", ""),
            }
        )

        for edge in self.graph.edges:

            if edge["source"] == node_id:

                references.append(
                    {"related": edge["target"], "relation": edge["relation"]}
                )

        return references

    def info(self):

        return {
            "engine": "Graph Article Reference Mapping Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
