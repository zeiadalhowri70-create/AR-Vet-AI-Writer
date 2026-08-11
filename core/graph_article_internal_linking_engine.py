# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphArticleInternalLinkingEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def generate_links(self, node_id):

        links = []

        for edge in self.graph.edges:

            if edge["source"] == node_id:

                target = self.graph.nodes.get(edge["target"])

                if target:

                    links.append(
                        {
                            "from": node_id,
                            "to": edge["target"],
                            "relation": edge["relation"],
                            "anchor": target.get("data", {}).get(
                                "name", edge["target"]
                            ),
                        }
                    )

        return links

    def related_articles(self, node_id):

        result = []

        for edge in self.graph.edges:

            if edge["source"] == node_id or edge["target"] == node_id:

                result.append(
                    {
                        "node": (
                            edge["target"]
                            if edge["source"] == node_id
                            else edge["source"]
                        ),
                        "relation": edge["relation"],
                    }
                )

        return result

    def info(self):

        return {
            "engine": "Graph Article Internal Linking Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
