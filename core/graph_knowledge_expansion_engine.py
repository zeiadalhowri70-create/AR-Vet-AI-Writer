# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphKnowledgeExpansionEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def add_knowledge_node(self, node_id, node_data):

        if node_id in self.graph.nodes:
            return False

        self.graph.nodes[node_id] = node_data

        return True

    def add_knowledge_relation(self, source, relation, target):

        edge = {"source": source, "relation": relation, "target": target}

        if edge in self.graph.edges:
            return False

        self.graph.edges.append(edge)

        return True

    def knowledge_size(self):

        return {"nodes": len(self.graph.nodes), "edges": len(self.graph.edges)}

    def info(self):

        return {
            "engine": "Graph Knowledge Expansion Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
