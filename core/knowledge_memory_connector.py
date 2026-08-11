# -*- coding: utf-8 -*-
"""
AR-Vet AI Writer
Knowledge Memory Connector
"""

from core.knowledge_memory_engine import KnowledgeMemoryEngine


class KnowledgeMemoryConnector:

    VERSION = "1.0.0"

    def __init__(self):

        self.memory = KnowledgeMemoryEngine()

    def store_node(self, node):

        node_type = node.get("node_type", "Unknown")

        title = node.get("title", "Untitled")

        data = node.get("relationships", {})

        result = self.memory.save_node(node_type, title, data)

        return {
            "status": result["status"],
            "connector": "Knowledge Memory Connector",
            "node_type": node_type,
            "title": title,
            "version": self.VERSION,
        }

    def health(self):

        return {
            "status": True,
            "connector": "Knowledge Memory Connector",
            "version": self.VERSION,
        }
