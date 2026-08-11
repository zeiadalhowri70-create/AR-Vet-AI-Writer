# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphKnowledgeExtractionEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def extract_node_facts(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        facts = {
            "id": node_id,
            "type": node.get("type"),
            "attributes": node.get("data", {}),
            "relations": [],
        }

        for edge in self.graph.edges:

            if edge["source"] == node_id:

                facts["relations"].append(
                    {"relation": edge["relation"], "target": edge["target"]}
                )

            elif edge["target"] == node_id:

                facts["relations"].append(
                    {"relation": edge["relation"], "source": edge["source"]}
                )

        return facts

    def extract_all_facts(self):

        return {
            node_id: self.extract_node_facts(node_id) for node_id in self.graph.nodes
        }

    def info(self):

        return {
            "engine": "Graph Knowledge Extraction Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
