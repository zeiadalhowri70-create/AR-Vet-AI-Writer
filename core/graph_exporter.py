# -*- coding: utf-8 -*-

import json
from pathlib import Path


class GraphExporter:

    def export(self, graph, filename="knowledge/graph_snapshot/disease_graph.json"):

        path = Path(filename)
        path.parent.mkdir(parents=True, exist_ok=True)

        data = {
            "nodes": list(graph.nodes.values()),
            "edges": graph.edges,
            "statistics": {"nodes": len(graph.nodes), "edges": len(graph.edges)},
        }

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        return str(path)
