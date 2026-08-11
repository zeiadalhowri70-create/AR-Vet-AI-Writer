# -*- coding: utf-8 -*-

from datetime import datetime, timezone
from pathlib import Path


class BloggerOperationsMonitorEngine:

    VERSION = "1.0"

    def check_file(self, path):

        return Path(path).exists()

    def run(self):

        checks = {
            "gateway": self.check_file("engine/blogger_gateway_engine.py"),
            "validation": self.check_file("engine/blogger_validation_engine.py"),
            "state": self.check_file("engine/blogger_publish_state_engine.py"),
            "audit": self.check_file("engine/blogger_publish_audit_engine.py"),
            "queue": self.check_file("engine/blogger_publish_queue_engine.py"),
            "recovery": self.check_file("engine/blogger_recovery_engine.py"),
            "api": self.check_file("engine/blogger_api_client_engine.py"),
        }

        failed = [k for k, v in checks.items() if not v]

        return {
            "engine": "Blogger Operations Monitor Engine",
            "version": self.VERSION,
            "status": "GREEN" if not failed else "WARNING",
            "checks": checks,
            "failed": failed,
            "generated_at": datetime.now(timezone.utc).isoformat(),
        }

    def info(self):

        return {
            "engine": "Blogger Operations Monitor Engine",
            "version": self.VERSION,
            "status": "production",
        }
