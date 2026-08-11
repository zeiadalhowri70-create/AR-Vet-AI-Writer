# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphDependencyEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def dependencies(self, node_id):

        result = []

        for edge in self.graph.edges:

            if edge["source"] == node_id:

                result.append({"node": edge["target"], "relation": edge["relation"]})

        return result

    def dependents(self, node_id):

        result = []

        for edge in self.graph.edges:

            if edge["target"] == node_id:

                result.append({"node": edge["source"], "relation": edge["relation"]})

        return result

    def info(self):

        return {
            "engine": "Graph Dependency Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
