# -*- coding: utf-8 -*-


class BloggerPublishQueueEngine:

    VERSION = "1.0"

    def enqueue(self, article):

        return {"queue_status": "waiting", "article": article}

    def dequeue(self, item):

        item["queue_status"] = "processing"

        return item

    def complete(self, item):

        item["queue_status"] = "completed"

        return item

    def info(self):

        return {
            "engine": "Blogger Publish Queue Engine",
            "version": self.VERSION,
            "status": "production",
        }
