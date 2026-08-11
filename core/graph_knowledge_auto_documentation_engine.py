# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphKnowledgeAutoDocumentationEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def document_node(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        lines = []

        lines.append(f"# {node_id}")

        lines.append(f"Type: {node.get('type')}")

        lines.append("## Information")

        for key, value in node.get("data", {}).items():

            lines.append(f"- {key}: {value}")

        lines.append("## Relations")

        for edge in self.graph.edges:

            if edge["source"] == node_id:

                lines.append(f"- {edge['relation']} → {edge['target']}")

            elif edge["target"] == node_id:

                lines.append(f"- {edge['relation']} ← {edge['source']}")

        return "\n".join(lines)

    def document_all(self):

        return {node_id: self.document_node(node_id) for node_id in self.graph.nodes}

    def info(self):

        return {
            "engine": "Graph Knowledge Auto Documentation Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
