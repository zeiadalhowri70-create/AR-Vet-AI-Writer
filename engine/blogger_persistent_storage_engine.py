# -*- coding: utf-8 -*-

import json
from pathlib import Path
from datetime import datetime, timezone


class BloggerPersistentStorageEngine:

    VERSION = "1.0"

    def __init__(self):

        self.path = Path("data/blogger_publish_state.json")

        self.path.parent.mkdir(parents=True, exist_ok=True)

    def load(self):

        if not self.path.exists():

            return []

        with open(self.path, "r", encoding="utf-8") as f:

            return json.load(f)

    def save(self, records):

        with open(self.path, "w", encoding="utf-8") as f:

            json.dump(records, f, ensure_ascii=False, indent=2)

    def add(self, record):

        records = self.load()

        record["stored_at"] = datetime.now(timezone.utc).isoformat()

        records.append(record)

        self.save(records)

        return record

    def info(self):

        return {
            "engine": "Blogger Persistent Storage Engine",
            "version": self.VERSION,
            "status": "production",
        }
