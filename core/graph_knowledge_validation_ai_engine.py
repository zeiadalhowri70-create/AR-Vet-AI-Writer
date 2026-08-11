# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphKnowledgeValidationAIEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def validate_node(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return {"valid": False, "reason": "node_not_found"}

        missing = []

        if not node.get("type"):
            missing.append("type")

        if not node.get("data"):
            missing.append("data")

        return {"node": node_id, "valid": len(missing) == 0, "missing": missing}

    def validate_relation(self, source, target):

        for edge in self.graph.edges:

            if edge["source"] == source and edge["target"] == target:
                return {"valid": True, "relation": edge["relation"]}

        return {"valid": False, "relation": None}

    def validate_all(self):

        return {node_id: self.validate_node(node_id) for node_id in self.graph.nodes}

    def info(self):

        return {
            "engine": "Graph Knowledge Validation AI Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
