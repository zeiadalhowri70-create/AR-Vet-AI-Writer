# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Production Token Budget Manager

Controls token allocation for AI requests.
"""


class TokenBudgetManager:

    VERSION = "1.0.0"

    def __init__(self, default_limit=8000):

        self.default_limit = default_limit
        self.usage = {}

    def create_budget(self, request_id, limit=None):

        self.usage[request_id] = {"limit": limit or self.default_limit, "used": 0}

        return self.usage[request_id]

    def consume(self, request_id, tokens):

        if request_id not in self.usage:
            self.create_budget(request_id)

        budget = self.usage[request_id]

        if budget["used"] + tokens > budget["limit"]:
            return {"allowed": False, "remaining": 0}

        budget["used"] += tokens

        return {"allowed": True, "remaining": budget["limit"] - budget["used"]}

    def remaining(self, request_id):

        if request_id not in self.usage:
            return self.default_limit

        budget = self.usage[request_id]

        return budget["limit"] - budget["used"]

    def health(self):

        return {
            "status": True,
            "version": self.VERSION,
            "active_budgets": len(self.usage),
        }


if __name__ == "__main__":

    manager = TokenBudgetManager()

    print(manager.health())

    manager.create_budget("article_001", 1000)

    print(manager.consume("article_001", 300))

    print(manager.remaining("article_001"))
