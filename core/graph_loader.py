# -*- coding: utf-8 -*-

"""
Graph Loader
AR-Vet AI Writer

Stage 3.2.1.B.2
"""

import json
from pathlib import Path


class GraphLoader:

    def __init__(self, folder="knowledge/graph"):
        self.folder = Path(folder)

    def load(self, filename):
        path = self.folder / filename

        if not path.exists():
            return {"items": []}

        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def load_all(self):
        return {
            "diseases": self.load("diseases.json"),
            "symptoms": self.load("symptoms.json"),
            "pathogens": self.load("pathogens.json"),
            "organs": self.load("organs.json"),
            "drugs": self.load("drugs.json"),
            "vaccines": self.load("vaccines.json"),
            "relations": self.load("relations.json"),
        }

    def info(self):
        data = self.load_all()

        return {
            "engine": "Graph Loader",
            "version": "1.0",
            "files": len(data),
            "folder": str(self.folder),
        }
