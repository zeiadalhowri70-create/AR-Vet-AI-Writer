# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Production Blogger API Adapter

Connector for Blogger API publishing.
"""


class BloggerAPIAdapter:

    VERSION = "1.0.0"

    def __init__(self, api=None):

        self.api = api

    def create_draft(self, article):

        if not self.api:

            return {
                "status": False,
                "action": "draft",
                "error": "Blogger API unavailable",
                "article": article,
            }

        return self.api.create_draft(article)

    def update(self, post_id, article):

        if not self.api:

            return {
                "status": False,
                "action": "update",
                "error": "Blogger API unavailable",
                "post_id": post_id,
            }

        return self.api.update(post_id, article)

    def publish(self, article):

        if not self.api:

            return {
                "status": False,
                "action": "publish",
                "error": "Blogger API unavailable",
                "article": article,
            }

        return self.api.publish(article)

    def health(self):

        return {
            "status": True,
            "version": self.VERSION,
            "api_connected": self.api is not None,
        }


if __name__ == "__main__":

    adapter = BloggerAPIAdapter()

    print(adapter.health())

    print(adapter.create_draft("مرض النيوكاسل في الدواجن"))
