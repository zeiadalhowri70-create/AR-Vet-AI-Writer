# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphKnowledgeSummaryEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def summarize(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        relations = []

        for edge in self.graph.edges:

            if edge["source"] == node_id:

                relations.append(f"{edge['relation']} -> {edge['target']}")

            elif edge["target"] == node_id:

                relations.append(f"{edge['relation']} <- {edge['source']}")

        return {
            "title": node_id,
            "type": node.get("type"),
            "summary": node.get("data", {}),
            "relations": relations,
        }

    def summarize_all(self):

        return {node_id: self.summarize(node_id) for node_id in self.graph.nodes}

    def info(self):

        return {
            "engine": "Graph Knowledge Summary Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
