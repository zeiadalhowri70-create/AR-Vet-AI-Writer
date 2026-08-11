# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticleExportMappingEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def export_data(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        data = node.get("data", {})

        return {
            "id": node_id,
            "title": data.get("name_ar", node_id),
            "formats": {"html": True, "markdown": True, "json": True},
            "export_ready": True,
        }

    def info(self):

        return {
            "engine": "Graph Article Export Mapping Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
