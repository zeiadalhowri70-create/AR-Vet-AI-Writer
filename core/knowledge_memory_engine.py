# -*- coding: utf-8 -*-
"""
AR-Vet AI Writer
Knowledge Memory Engine
"""

from database.database_manager import DatabaseManager


class KnowledgeMemoryEngine:

    VERSION = "1.0.0"

    def __init__(self):

        self.database = DatabaseManager()

    def save_node(self, node_type, title, data):

        conn = self.database.connect()

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO knowledge
            (node_type, title, data)
            VALUES (?, ?, ?)
            """,
            (node_type, title, str(data)),
        )

        conn.commit()
        conn.close()

        return {
            "status": True,
            "action": "saved",
            "node_type": node_type,
            "title": title,
            "version": self.VERSION,
        }

    def get_nodes(self):

        conn = self.database.connect()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, node_type, title, data
            FROM knowledge
            """)

        rows = cursor.fetchall()

        conn.close()

        return [
            {"id": row[0], "node_type": row[1], "title": row[2], "data": row[3]}
            for row in rows
        ]

    def health(self):

        return {
            "status": True,
            "engine": "Knowledge Memory Engine",
            "version": self.VERSION,
        }
