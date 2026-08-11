# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphKnowledgeLinkingEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def generate_links(self, node_id):

        links = []

        for edge in self.graph.edges:

            if edge["source"] == node_id:

                links.append(
                    {
                        "from": node_id,
                        "to": edge["target"],
                        "relation": edge["relation"],
                    }
                )

            elif edge["target"] == node_id:

                links.append(
                    {
                        "from": node_id,
                        "to": edge["source"],
                        "relation": edge["relation"],
                    }
                )

        return links

    def related_content(self, node_id):

        results = []

        for link in self.generate_links(node_id):

            node = self.graph.nodes.get(link["to"])

            if node:

                results.append(
                    {
                        "node": link["to"],
                        "type": node.get("type"),
                        "relation": link["relation"],
                    }
                )

        return results

    def info(self):

        return {
            "engine": "Graph Knowledge Linking Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
