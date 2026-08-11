# -*- coding: utf-8 -*-

from core.graph_builder import GraphBuilder


class GraphRankingEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()

    def node_rank(self, node_id):

        score = 0

        for edge in self.graph.edges:

            if edge["source"] == node_id:
                score += 1

            if edge["target"] == node_id:
                score += 1

        return {"node": node_id, "rank": score}

    def rank_all(self):

        ranking = {}

        for node_id in self.graph.nodes:

            ranking[node_id] = self.node_rank(node_id)["rank"]

        return dict(sorted(ranking.items(), key=lambda x: x[1], reverse=True))

    def top_nodes(self, limit=3):

        return list(self.rank_all().items())[:limit]

    def info(self):

        return {
            "engine": "Graph Ranking Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
