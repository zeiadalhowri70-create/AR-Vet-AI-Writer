# -*- coding: utf-8 -*-

from pathlib import Path


class BloggerAPIActivationEngine:

    VERSION = "1.0"

    def check(self):

        token = Path("token.pickle")

        return {
            "api_engine": "Blogger API",
            "token_exists": token.exists(),
            "mode": "draft_only",
            "activated": token.exists(),
        }

    def info(self):

        return {
            "engine": "Blogger API Activation Engine",
            "version": self.VERSION,
            "status": "production",
        }
