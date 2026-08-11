# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticleSchemaMappingEngine:

    def __init__(self):
        self.graph = GraphBuilder().build()

    def generate_schema(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        return {
            "@context": "https://schema.org",
            "@type": "MedicalCondition",
            "name": node.get("name_ar"),
            "alternateName": node.get("name_en"),
            "category": node.get("category"),
            "associatedAnatomy": node.get("animal"),
        }

    def info(self):

        return {
            "engine": "Graph Article Schema Mapping Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
