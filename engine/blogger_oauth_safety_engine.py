# -*- coding: utf-8 -*-


class BloggerOAuthSafetyEngine:

    VERSION = "1.0"

    def check(self, client):

        return {
            "oauth_available": bool(getattr(client, "service", None)),
            "blog_configured": bool(getattr(client, "blog_id", None)),
            "ready": bool(
                getattr(client, "service", None) and getattr(client, "blog_id", None)
            ),
        }

    def info(self):

        return {
            "engine": "Blogger OAuth Safety Engine",
            "version": self.VERSION,
            "status": "production",
        }
