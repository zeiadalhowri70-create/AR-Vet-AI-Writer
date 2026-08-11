# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticleAudioGenerationMappingEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def audio_script(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        data = node.get("data", {})

        title = data.get("name_ar", node_id)

        return {
            "title": title,
            "voice_type": "veterinary_educational",
            "script": f"مرحباً بكم، اليوم سنتحدث عن {title}. "
            "سنستعرض التعريف والمسبب والعلاقات المرضية "
            "والوقاية والسيطرة.",
            "audio_ready": True,
        }

    def info(self):

        return {
            "engine": "Graph Article Audio Generation Mapping Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
