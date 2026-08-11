# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphReasoningEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def infer_relations(self, node_id):

        results = []

        direct = []

        for edge in self.graph.edges:

            if edge["source"] == node_id:
                direct.append(edge["target"])

        for first in direct:

            for edge in self.graph.edges:

                if edge["source"] == first:
                    results.append(
                        {
                            "from": node_id,
                            "via": first,
                            "to": edge["target"],
                            "relation": edge["relation"],
                        }
                    )

        return results

    def related_by_type(self, node_id, node_type):

        results = []

        for edge in self.graph.edges:

            target = edge["target"]

            if edge["source"] == node_id:

                node = self.graph.nodes.get(target, {})

                if node.get("type") == node_type:
                    results.append(target)

        return results

    def reasoning_summary(self, node_id):

        return {
            "node": node_id,
            "direct_relations": [
                edge
                for edge in self.graph.edges
                if edge["source"] == node_id or edge["target"] == node_id
            ],
            "inferred_relations": self.infer_relations(node_id),
        }

    def info(self):

        return {
            "engine": "Graph Reasoning Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
