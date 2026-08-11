# -*- coding: utf-8 -*-
"""
AR-Vet AI Writer
Article Memory Engine
"""

import json

from database.database_manager import DatabaseManager


class ArticleMemoryEngine:

    VERSION = "1.0.0"

    def __init__(self):

        self.database = DatabaseManager()

    def save_article(self, title, content):

        conn = self.database.connect()

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO articles
            (title, content)
            VALUES (?, ?)
            """,
            (title, content),
        )

        conn.commit()
        conn.close()

        return {
            "status": True,
            "action": "saved",
            "title": title,
            "version": self.VERSION,
        }

    def get_articles(self):

        conn = self.database.connect()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, title, content
            FROM articles
            """)

        rows = cursor.fetchall()

        conn.close()

        return [{"id": row[0], "title": row[1], "content": row[2]} for row in rows]

    def health(self):

        return {
            "status": True,
            "engine": "Article Memory Engine",
            "version": self.VERSION,
        }
