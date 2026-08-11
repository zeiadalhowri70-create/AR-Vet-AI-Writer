# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphDecisionEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def evaluate_node(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return {"node": node_id, "exists": False}

        relations = [
            edge
            for edge in self.graph.edges
            if edge["source"] == node_id or edge["target"] == node_id
        ]

        return {
            "node": node_id,
            "exists": True,
            "type": node.get("type"),
            "connections": len(relations),
            "important": len(relations) > 1,
        }

    def compare_nodes(self, node_a, node_b):

        result = {
            "node_a": node_a,
            "node_b": node_b,
            "same_type": False,
            "shared_relations": [],
        }

        a = self.graph.nodes.get(node_a)
        b = self.graph.nodes.get(node_b)

        if not a or not b:
            return result

        result["same_type"] = a.get("type") == b.get("type")

        a_rel = {
            edge["relation"] for edge in self.graph.edges if edge["source"] == node_a
        }

        b_rel = {
            edge["relation"] for edge in self.graph.edges if edge["source"] == node_b
        }

        result["shared_relations"] = list(a_rel.intersection(b_rel))

        return result

    def info(self):

        return {
            "engine": "Graph Decision Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
