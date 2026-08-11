# -*- coding: utf-8 -*-


class BloggerHealthCheckEngine:

    VERSION = "1.0"

    def check(self, gateway):

        checks = {
            "gateway": gateway is not None,
            "publisher": hasattr(gateway, "publisher"),
            "validator": hasattr(gateway, "validator"),
            "storage": hasattr(gateway, "storage"),
            "queue": hasattr(gateway, "queue"),
        }

        return {
            "healthy": all(checks.values()),
            "checks": checks,
            "engine": "Blogger Health Check Engine",
            "version": self.VERSION,
        }

    def info(self):

        return {
            "engine": "Blogger Health Check Engine",
            "version": self.VERSION,
            "status": "production",
        }
