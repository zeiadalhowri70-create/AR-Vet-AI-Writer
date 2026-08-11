# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphExplanationEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def explain_relation(self, source, target):

        explanations = []

        for edge in self.graph.edges:

            if edge["source"] == source and edge["target"] == target:

                explanations.append(
                    {
                        "from": source,
                        "to": target,
                        "relation": edge["relation"],
                        "explanation": f"{source} {edge['relation']} {target}",
                    }
                )

        return explanations

    def explain_node(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        return {
            "node": node_id,
            "type": node.get("type"),
            "description": node.get("data"),
            "relations": [
                edge
                for edge in self.graph.edges
                if edge["source"] == node_id or edge["target"] == node_id
            ],
        }

    def info(self):

        return {
            "engine": "Graph Explanation Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
