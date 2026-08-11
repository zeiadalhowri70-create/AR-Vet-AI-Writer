# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticleMobileOptimizationMappingEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def mobile_data(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        data = node.get("data", {})

        return {
            "title": data.get("name_ar", node_id),
            "responsive": True,
            "mobile_friendly": True,
            "reading_mode": "optimized",
            "amp_ready": True,
        }

    def info(self):

        return {
            "engine": "Graph Article Mobile Optimization Mapping Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
