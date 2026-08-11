# -*- coding: utf-8 -*-

from datetime import datetime, timezone


class BloggerRollbackEngine:

    VERSION = "1.0"

    def rollback(self, draft):

        return {
            "status": "rollback_requested",
            "draft_id": draft.get("id"),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "engine": "Blogger Rollback Engine",
            "version": self.VERSION,
        }

    def info(self):

        return {
            "engine": "Blogger Rollback Engine",
            "version": self.VERSION,
            "status": "production",
        }
