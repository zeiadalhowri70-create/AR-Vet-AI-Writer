# -*- coding: utf-8 -*-


class BloggerWorkflowControllerEngine:

    VERSION = "1.0"

    STATES = ["CREATED", "VALIDATED", "DRAFT_CREATED", "REVIEW_READY", "PUBLISHED"]

    def can_publish(self, state):

        return state in ["DRAFT_CREATED", "REVIEW_READY"]

    def info(self):

        return {
            "engine": "Blogger Workflow Controller Engine",
            "version": self.VERSION,
            "status": "production",
        }
