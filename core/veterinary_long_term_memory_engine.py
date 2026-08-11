# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Veterinary Long Term Memory Engine

Stage 2.7.4
"""

import sqlite3
from pathlib import Path
import json


class VeterinaryLongTermMemoryEngine:

    VERSION = "1.0.0"

    def __init__(self):

        self.name = "Veterinary Long Term Memory Engine"

        self.db_path = Path("database/arvet_memory.db")

        self._init_database()

    def _init_database(self):

        self.db_path.parent.mkdir(exist_ok=True)

        conn = sqlite3.connect(self.db_path)

        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS veterinary_cases (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            animal TEXT,

            disease TEXT,

            symptoms TEXT,

            confidence REAL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """)

        conn.commit()

        conn.close()

    def save_case(self, case):

        conn = sqlite3.connect(self.db_path)

        cur = conn.cursor()

        cur.execute(
            """
            INSERT INTO veterinary_cases
            (
            animal,
            disease,
            symptoms,
            confidence
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                case.get("animal", ""),
                case.get("disease", ""),
                json.dumps(case.get("symptoms", []), ensure_ascii=False),
                case.get("confidence", 0),
            ),
        )

        conn.commit()

        conn.close()

        return True

    def count_cases(self):

        conn = sqlite3.connect(self.db_path)

        cur = conn.cursor()

        cur.execute("SELECT COUNT(*) FROM veterinary_cases")

        result = cur.fetchone()[0]

        conn.close()

        return result

    def latest_case(self):

        conn = sqlite3.connect(self.db_path)

        cur = conn.cursor()

        cur.execute("""
            SELECT animal,disease,symptoms,confidence
            FROM veterinary_cases
            ORDER BY id DESC
            LIMIT 1
            """)

        row = cur.fetchone()

        conn.close()

        if not row:
            return None

        return {
            "animal": row[0],
            "disease": row[1],
            "symptoms": json.loads(row[2]),
            "confidence": row[3],
        }

    def health(self):

        return {
            "status": True,
            "engine": self.name,
            "version": self.VERSION,
            "database": str(self.db_path),
        }
