# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphPatternEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def find_pattern(self, relation):

        matches = []

        for edge in self.graph.edges:

            if edge["relation"] == relation:

                matches.append(
                    {
                        "source": edge["source"],
                        "target": edge["target"],
                        "relation": edge["relation"],
                    }
                )

        return matches

    def node_pattern(self, node_id):

        patterns = []

        for edge in self.graph.edges:

            if edge["source"] == node_id:

                patterns.append(
                    {
                        "direction": "outgoing",
                        "relation": edge["relation"],
                        "target": edge["target"],
                    }
                )

            elif edge["target"] == node_id:

                patterns.append(
                    {
                        "direction": "incoming",
                        "relation": edge["relation"],
                        "source": edge["source"],
                    }
                )

        return patterns

    def info(self):

        return {
            "engine": "Graph Pattern Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
