# -*- coding: utf-8 -*-

import uuid
from datetime import datetime, timezone


class BloggerRealFlowAdapter:

    VERSION = "1.0"

    def prepare(self, article):

        production_id = str(uuid.uuid4())

        return {
            "production_id": production_id,
            "article": article,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "engine": "Blogger Real Flow Adapter",
            "version": self.VERSION,
        }

    def info(self):

        return {
            "engine": "Blogger Real Flow Adapter",
            "version": self.VERSION,
            "status": "production",
        }
