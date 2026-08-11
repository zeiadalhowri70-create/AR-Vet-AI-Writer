# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Production Blogger Pipeline Manager

Final Production Version
"""


class BloggerPipelineManager:

    VERSION = "2.0.0"

    def __init__(self, adapter=None):

        self.adapter = adapter

    def health(self):

        return {
            "status": True,
            "version": self.VERSION,
            "adapter_connected": self.adapter is not None,
        }

    def create_draft(self, article):

        if not self.adapter:

            return {
                "status": False,
                "action": "draft",
                "error": "Blogger adapter unavailable",
                "article": article,
            }

        return self.adapter.create_draft(article)

    def update(self, post_id, article):

        if not self.adapter:

            return {
                "status": False,
                "action": "update",
                "error": "Blogger adapter unavailable",
            }

        return self.adapter.update(post_id, article)

    def publish(self, article):

        if not self.adapter:

            return {
                "status": False,
                "action": "publish",
                "error": "Blogger adapter unavailable",
            }

        return self.adapter.publish(article)


if __name__ == "__main__":

    manager = BloggerPipelineManager()

    print(manager.health())

    print(manager.create_draft("مرض النيوكاسل في الدواجن"))
