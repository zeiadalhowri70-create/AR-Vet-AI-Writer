# -*- coding: utf-8 -*-

from copy import deepcopy

from core.graph_builder import GraphBuilder


class GraphUpdateEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def update_node(self, node_id, data):

        if node_id not in self.graph.nodes:
            return False

        self.graph.nodes[node_id].update(data)

        return True

    def add_node(self, node_id, node_data):

        if node_id in self.graph.nodes:
            return False

        self.graph.nodes[node_id] = node_data

        return True

    def add_edge(self, edge):

        if edge in self.graph.edges:
            return False

        self.graph.edges.append(edge)

        return True

    def remove_node(self, node_id):

        if node_id not in self.graph.nodes:
            return False

        del self.graph.nodes[node_id]

        self.graph.edges = [
            edge
            for edge in self.graph.edges
            if edge["source"] != node_id and edge["target"] != node_id
        ]

        return True

    def snapshot(self):

        return deepcopy({"nodes": self.graph.nodes, "edges": self.graph.edges})

    def info(self):

        return {
            "engine": "Graph Update Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
