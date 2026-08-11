# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticleFinalAssemblyEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def assemble(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        data = node.get("data", {})

        sections = [
            "التعريف بالمرض",
            "المسبب",
            "العائل",
            "العلاقات المرضية",
            "الأعراض والعلامات",
            "التشخيص",
            "الوقاية والسيطرة",
        ]

        return {
            "id": node_id,
            "title": data.get("name_ar", node_id),
            "type": node.get("type"),
            "sections": sections,
            "knowledge_ready": True,
            "seo_ready": True,
            "schema_ready": True,
            "publication_ready": True,
        }

    def info(self):

        return {
            "engine": "Graph Article Final Assembly Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
