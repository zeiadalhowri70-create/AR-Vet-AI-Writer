# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Production Provider Bridge

Connects AI Core with Provider Layer.
"""


class ProviderBridge:

    VERSION = "1.0.0"

    def __init__(
        self, provider_manager=None, router=None, retry=None, budget=None, cost=None
    ):

        self.provider_manager = provider_manager
        self.router = router
        self.retry = retry
        self.budget = budget
        self.cost = cost

    def select_model(self, task):

        if not self.router:
            return None

        return self.router.select(task)

    def execute(self, task, prompt, tokens=0):

        model = self.select_model(task)

        if self.budget:

            check = self.budget.consume(task, tokens)

            if not check["allowed"]:
                return {"success": False, "error": "Token budget exceeded"}

        if not self.provider_manager:

            return {
                "success": False,
                "error": "Provider manager unavailable",
                "model": model,
            }

        result = self.provider_manager.generate(prompt)

        return {"success": True, "model": model, "result": result}

    def health(self):

        return {"status": True, "version": self.VERSION}


if __name__ == "__main__":

    bridge = ProviderBridge()

    print(bridge.health())
