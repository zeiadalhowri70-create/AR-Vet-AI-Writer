# -*- coding: utf-8 -*-

from copy import deepcopy

from core.graph_builder import GraphBuilder


class GraphTransactionEngine:

    def __init__(self):

        self.graph = GraphBuilder().build()
        self.transactions = []

    def begin(self):

        snapshot = deepcopy({"nodes": self.graph.nodes, "edges": self.graph.edges})

        self.transactions.append(snapshot)

        return True

    def rollback(self):

        if not self.transactions:
            return False

        snapshot = self.transactions.pop()

        self.graph.nodes = snapshot["nodes"]
        self.graph.edges = snapshot["edges"]

        return True

    def commit(self):

        if not self.transactions:
            return False

        self.transactions.pop()

        return True

    def transaction_count(self):

        return len(self.transactions)

    def info(self):

        return {
            "engine": "Graph Transaction Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
            "transactions": len(self.transactions),
        }
