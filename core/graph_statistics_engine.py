# -*- coding: utf-8 -*-


class GraphStatisticsEngine:

    def analyze(self, graph):

        node_types = {}
        relations = {}

        for node in graph.nodes.values():
            node_type = node.get("type", "unknown")
            node_types[node_type] = node_types.get(node_type, 0) + 1

        for edge in graph.edges:
            relation = edge.get("relation")
            relations[relation] = relations.get(relation, 0) + 1

        connected = {}

        for edge in graph.edges:
            source = edge["source"]
            connected[source] = connected.get(source, 0) + 1

        top_diseases = sorted(connected.items(), key=lambda x: x[1], reverse=True)[:10]

        return {
            "nodes": len(graph.nodes),
            "edges": len(graph.edges),
            "node_types": node_types,
            "relations": relations,
            "top_connected_diseases": top_diseases,
        }
