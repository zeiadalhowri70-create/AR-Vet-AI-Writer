# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticleImageGenerationMappingEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def image_prompt(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        data = node.get("data", {})

        title = data.get("name_ar", node_id)

        animal = data.get("animal", "")

        category = data.get("category", "")

        return {
            "subject": title,
            "prompt": f"صورة علمية بيطرية احترافية عن {title} "
            f"في {animal}، تصنيف المرض {category}, "
            "أسلوب طبي واقعي مناسب لمقال علمي",
            "type": "medical_cover",
            "ready_for_generation": True,
        }

    def info(self):

        return {
            "engine": "Graph Article Image Generation Mapping Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
