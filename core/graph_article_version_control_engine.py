# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder
from datetime import datetime


class GraphArticleVersionControlEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()
        self.versions = {}

    def create_version(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        version = {
            "id": node_id,
            "version": 1,
            "created": datetime.now().isoformat(),
            "data": node.get("data", {}),
        }

        self.versions[node_id] = version

        return version

    def get_version(self, node_id):

        return self.versions.get(node_id)

    def info(self):

        return {
            "engine": "Graph Article Version Control Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
            "versions": len(self.versions),
        }
