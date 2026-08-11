# -*- coding: utf-8 -*-

from engine.blogger_api_client_engine import BloggerAPIClientEngine


class BloggerRealDraftEngine:

    VERSION = "1.0"

    def __init__(self):

        self.client = BloggerAPIClientEngine()

    def create(self, article):

        result = self.client.create_draft(article)

        result["activation_layer"] = True

        return result

    def info(self):

        return {
            "engine": "Blogger Real Draft Engine",
            "version": self.VERSION,
            "status": "production",
        }
