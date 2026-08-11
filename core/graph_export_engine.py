# -*- coding: utf-8 -*-

import json

from core.graph_builder import GraphBuilder


class GraphExportEngine:

    def __init__(self):
        self.graph = GraphBuilder().build()

    def to_dict(self):

        return {"nodes": self.graph.nodes, "edges": self.graph.edges}

    def to_json(self, indent=2):

        return json.dumps(self.to_dict(), ensure_ascii=False, indent=indent)

    def save_json(self, filepath):

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(self.to_json())

        return filepath

    def info(self):

        return {
            "engine": "Graph Export Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
