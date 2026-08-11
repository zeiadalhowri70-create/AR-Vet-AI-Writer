# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder
from datetime import datetime


class GraphArticleUpdateManagementEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()
        self.updates = {}

    def update_article(self, node_id):

        node = self.graph.nodes.get(node_id)

        if not node:
            return None

        update = {
            "id": node_id,
            "updated": datetime.now().isoformat(),
            "title": node.get("data", {}).get("name_ar", node_id),
            "status": "updated",
            "auto_update_ready": True,
        }

        self.updates[node_id] = update

        return update

    def get_update(self, node_id):

        return self.updates.get(node_id)

    def info(self):

        return {
            "engine": "Graph Article Update Management Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
            "updates": len(self.updates),
        }
