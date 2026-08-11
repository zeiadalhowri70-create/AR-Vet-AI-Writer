# -*- coding: utf-8 -*-


class BloggerArticleRequestAdapter:

    VERSION = "1.0"

    def build(self, job):

        topic = job.get("topic", {})

        return {
            "title": topic.get("topic", "Veterinary Article"),
            "category": topic.get("category", "general"),
            "source": "autonomous_workflow",
            "job_id": job.get("job_id"),
            "engine": "Blogger Article Request Adapter",
            "version": self.VERSION,
        }

    def info(self):

        return {
            "engine": "Blogger Article Request Adapter",
            "version": self.VERSION,
            "status": "production",
        }
