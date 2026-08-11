# -*- coding: utf-8 -*-

"""
Knowledge Graph Engine
AR-Vet AI Writer

Stage 3.2.1.A
"""


class KnowledgeGraph:

    def __init__(self):

        self.nodes = {}
        self.edges = []

    def add_node(self, node_id, node_type, data=None):

        self.nodes[node_id] = {"id": node_id, "type": node_type, "data": data or {}}

    def add_edge(self, source, relation, target):

        self.edges.append({"source": source, "relation": relation, "target": target})

    def get_node(self, node_id):

        return self.nodes.get(node_id)

    def get_edges(self, node_id):

        return [edge for edge in self.edges if edge["source"] == node_id]

    def info(self):

        return {
            "engine": "Knowledge Graph",
            "version": "1.0",
            "nodes": len(self.nodes),
            "edges": len(self.edges),
        }
