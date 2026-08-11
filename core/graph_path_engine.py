# -*- coding: utf-8 -*-

from collections import deque

from core.graph_builder import GraphBuilder


class GraphPathEngine:

    def __init__(self):
        self.graph = GraphBuilder().build()

    def shortest_path(self, start, end):

        if start == end:
            return [start]

        visited = set([start])
        queue = deque([(start, [start])])

        while queue:

            node, path = queue.popleft()

            for edge in self.graph.edges:

                if edge["source"] != node:
                    continue

                neighbor = edge["target"]

                if neighbor == end:
                    return path + [neighbor]

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return []

    def exists(self, start, end):

        return len(self.shortest_path(start, end)) > 0

    def info(self):

        return {
            "engine": "Graph Path Engine",
            "version": "1.0",
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
        }
