# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticleVideoGenerationMappingEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def video_prompt(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        data = node.get("data", {})

        title = data.get("name_ar", node_id)

        animal = data.get("animal", "")

        return {
            "title": title,
            "video_type": "educational_veterinary",
            "prompt": f"فيديو تعليمي بيطري عن {title} "
            f"في {animal} يشرح التعريف والمسبب "
            "والأعراض والتشخيص والوقاية بأسلوب علمي",
            "youtube_ready": True,
            "social_ready": True,
        }

    def info(self):

        return {
            "engine": "Graph Article Video Generation Mapping Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
