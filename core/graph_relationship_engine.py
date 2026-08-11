# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphRelationshipEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def relationships(self, node_id):

        result = []

        for edge in self.graph.edges:

            if edge["source"] == node_id or edge["target"] == node_id:

                result.append(edge)

        return result

    def related_nodes(self, node_id):

        nodes = []

        for edge in self.graph.edges:

            if edge["source"] == node_id:
                nodes.append(edge["target"])

            elif edge["target"] == node_id:
                nodes.append(edge["source"])

        return list(set(nodes))

    def relation_exists(self, source, target, relation=None):

        for edge in self.graph.edges:

            if edge["source"] == source and edge["target"] == target:

                if relation is None or edge["relation"] == relation:
                    return True

        return False

    def info(self):

        return {
            "engine": "Graph Relationship Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
