# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphContextEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def context(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        context = {
            "node": node_id,
            "type": node.get("type"),
            "data": node.get("data"),
            "neighbors": [],
        }

        for edge in self.graph.edges:

            if edge["source"] == node_id:

                context["neighbors"].append(
                    {"node": edge["target"], "relation": edge["relation"]}
                )

            elif edge["target"] == node_id:

                context["neighbors"].append(
                    {"node": edge["source"], "relation": edge["relation"]}
                )

        return context

    def contexts(self, node_ids):

        return {node_id: self.context(node_id) for node_id in node_ids}

    def info(self):

        return {
            "engine": "Graph Context Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
