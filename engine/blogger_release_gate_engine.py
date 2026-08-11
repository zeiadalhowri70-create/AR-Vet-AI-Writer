# -*- coding: utf-8 -*-


class BloggerReleaseGateEngine:

    VERSION = "1.0"

    def evaluate(self, health, oauth):

        passed = health.get("healthy") and oauth.get("ready")

        return {
            "release_ready": passed,
            "health": health,
            "oauth": oauth,
            "engine": "Blogger Release Gate Engine",
        }

    def info(self):

        return {
            "engine": "Blogger Release Gate Engine",
            "version": self.VERSION,
            "status": "production",
        }
