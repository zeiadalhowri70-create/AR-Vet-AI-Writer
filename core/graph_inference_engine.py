# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphInferenceEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def infer(self, node_id):

        facts = []

        outgoing = [edge for edge in self.graph.edges if edge["source"] == node_id]

        for edge in outgoing:

            target = edge["target"]

            for next_edge in self.graph.edges:

                if next_edge["source"] == target:

                    facts.append(
                        {
                            "source": node_id,
                            "relation": edge["relation"],
                            "intermediate": target,
                            "result_relation": next_edge["relation"],
                            "target": next_edge["target"],
                        }
                    )

        return facts

    def can_reach(self, source, target):

        visited = set()

        def search(node):

            if node == target:
                return True

            visited.add(node)

            for edge in self.graph.edges:

                if edge["source"] == node:

                    if edge["target"] not in visited:

                        if search(edge["target"]):
                            return True

            return False

        return search(source)

    def info(self):

        return {
            "engine": "Graph Inference Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
