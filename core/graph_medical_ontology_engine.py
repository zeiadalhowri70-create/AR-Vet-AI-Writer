# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphMedicalOntologyEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def get_medical_class(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        node_type = node.get("type")

        classes = {
            "disease": "medical_disease",
            "pathogen": "infectious_agent",
            "animal": "host_species",
        }

        return {
            "node": node_id,
            "class": classes.get(node_type, "unknown"),
            "type": node_type,
        }

    def ontology_relation(self, source, target):

        relations = []

        for edge in self.graph.edges:

            if edge["source"] == source and edge["target"] == target:

                relations.append(
                    {"relation": edge["relation"], "from": source, "to": target}
                )

        return relations

    def medical_map(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        return {
            "entity": node_id,
            "medical_class": self.get_medical_class(node_id),
            "relations": self.ontology_relation(node_id, ""),
        }

    def info(self):

        return {
            "engine": "Graph Medical Ontology Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
