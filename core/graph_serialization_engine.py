# -*- coding: utf-8 -*-

import json

from core.graph_builder import GraphBuilder


class GraphSerializationEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def serialize(self):

        return json.dumps(
            {"nodes": self.graph.nodes, "edges": self.graph.edges}, ensure_ascii=False
        )

    def deserialize(self, data):

        return json.loads(data)

    def size(self):

        return len(self.serialize())

    def info(self):

        return {
            "engine": "Graph Serialization Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
