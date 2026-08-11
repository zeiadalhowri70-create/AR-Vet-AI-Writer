# -*- coding: utf-8 -*-

from datetime import datetime, timezone


class BloggerPublishStateEngine:

    VERSION = "1.0"

    STATES = [
        "CREATED",
        "VALIDATED",
        "DRAFT_CREATED",
        "REVIEW_PENDING",
        "PUBLISHED",
        "FAILED",
        "ROLLED_BACK",
    ]

    def create(self):

        return {
            "state": "CREATED",
            "history": [
                {"state": "CREATED", "time": datetime.now(timezone.utc).isoformat()}
            ],
        }

    def transition(self, record, new_state):

        if new_state not in self.STATES:
            raise ValueError(f"Invalid publishing state: {new_state}")

        record["state"] = new_state

        record.setdefault("history", []).append(
            {"state": new_state, "time": datetime.now(timezone.utc).isoformat()}
        )

        return record

    def info(self):

        return {
            "engine": "Blogger Publish State Engine",
            "version": self.VERSION,
            "states": self.STATES,
            "status": "production",
        }
