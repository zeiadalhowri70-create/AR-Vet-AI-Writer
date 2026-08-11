# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticleAIPromptMappingEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def generate_prompt(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        data = node.get("data", {})

        relations = [
            f"{e['relation']} -> {e['target']}"
            for e in self.graph.edges
            if e["source"] == node_id
        ]

        prompt = f"""
اكتب مقالاً علمياً احترافياً عن:

العنوان:
{data.get("name_ar", node_id)}

النوع:
{node.get("type")}

المعلومات:
{data}

العلاقات:
{relations}

يجب أن يكون المقال:
- علمياً.
- متوافقاً مع SEO.
- مناسباً للنشر في Blogger.
- شاملاً ومنظماً.
"""

        return {
            "title": data.get("name_ar", node_id),
            "prompt": prompt.strip(),
            "ai_ready": True,
        }

    def info(self):

        return {
            "engine": "Graph Article AI Prompt Mapping Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
