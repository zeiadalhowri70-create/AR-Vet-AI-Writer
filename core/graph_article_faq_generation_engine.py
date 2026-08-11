# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticleFAQGenerationEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def generate_faq(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        data = node.get("data", {})

        name = data.get("name_ar", node_id)

        faq = []

        faq.append(
            {
                "question": f"ما هو {name}؟",
                "answer": f"{name} هو مرض من نوع {node.get('type')}",
            }
        )

        for edge in self.graph.edges:

            if edge["source"] == node_id:

                faq.append(
                    {
                        "question": f"ما العلاقة بين {name} و {
                            edge['target']}؟",
                        "answer": f"{name} {
                            edge['relation']} {
                            edge['target']}",
                    }
                )

        return faq

    def info(self):

        return {
            "engine": "Graph Article FAQ Generation Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
