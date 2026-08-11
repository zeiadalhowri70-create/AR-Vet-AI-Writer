# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticleSocialMediaMappingEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def social_data(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        data = node.get("data", {})

        title = data.get("name_ar", node_id)

        return {
            "title": title,
            "facebook": {"text": f"تعرف على {title} | مقال بيطري علمي"},
            "whatsapp": {"message": f"معلومات علمية عن {title}"},
            "telegram": {"caption": f"{title} - مرجع بيطري"},
            "share_ready": True,
        }

    def info(self):

        return {
            "engine": "Graph Article Social Media Mapping Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
