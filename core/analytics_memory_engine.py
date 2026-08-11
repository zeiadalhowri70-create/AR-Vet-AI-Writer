# -*- coding: utf-8 -*-
"""
AR-Vet AI Writer
Analytics Memory Engine
"""

from database.database_manager import DatabaseManager


class AnalyticsMemoryEngine:

    VERSION = "1.0.0"

    def __init__(self):

        self.database = DatabaseManager()

    def save_metric(self, metric, value, source="system"):

        conn = self.database.connect()

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO analytics
            (metric, value, source)
            VALUES (?, ?, ?)
            """,
            (metric, str(value), source),
        )

        conn.commit()
        conn.close()

        return {
            "status": True,
            "metric": metric,
            "source": source,
            "version": self.VERSION,
        }

    def get_metrics(self):

        conn = self.database.connect()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, metric, value, source
            FROM analytics
            """)

        rows = cursor.fetchall()

        conn.close()

        return [
            {"id": row[0], "metric": row[1], "value": row[2], "source": row[3]}
            for row in rows
        ]

    def health(self):

        return {
            "status": True,
            "engine": "Analytics Memory Engine",
            "version": self.VERSION,
        }
