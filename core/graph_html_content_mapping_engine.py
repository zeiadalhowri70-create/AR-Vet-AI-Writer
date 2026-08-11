# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphHTMLContentMappingEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def generate_html_block(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        data = node.get("data", {})

        html = []

        html.append(f"<h1>{data.get('name_ar', node_id)}</h1>")

        html.append(f"<p>النوع: {node.get('type')}</p>")

        html.append("<h2>المعلومات</h2>")

        html.append("<ul>")

        for key, value in data.items():

            html.append(f"<li>{key}: {value}</li>")

        html.append("</ul>")

        html.append("<h2>العلاقات</h2>")

        html.append("<ul>")

        for edge in self.graph.edges:

            if edge["source"] == node_id:

                html.append(f"<li>{edge['relation']} → {edge['target']}</li>")

        html.append("</ul>")

        return "\n".join(html)

    def info(self):

        return {
            "engine": "Graph HTML Content Mapping Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
