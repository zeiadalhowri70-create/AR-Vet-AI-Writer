# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticleContentStructureEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def generate_structure(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        data = node.get("data", {})

        sections = []

        if node.get("type") == "disease":

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
            "title": data.get("name_ar", node_id),
            "type": node.get("type"),
            "sections": sections,
            "knowledge_source": node_id,
        }

    def info(self):

        return {
            "engine": "Graph Article Content Structure Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
