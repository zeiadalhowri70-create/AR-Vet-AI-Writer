# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticleAdSenseOptimizationMappingEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def adsense_data(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        data = node.get("data", {})

        return {
            "title": data.get("name_ar", node_id),
            "content_quality": True,
            "scientific_structure": True,
            "ad_ready": True,
            "placements": ["after_intro", "middle_content", "before_references"],
        }

    def info(self):

        return {
            "engine": "Graph Article AdSense Optimization Mapping Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
