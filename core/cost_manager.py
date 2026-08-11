# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Production Cost Manager

Tracks AI usage cost estimation.
"""


class CostManager:

    VERSION = "1.0.0"

    def __init__(self):

        self.providers = {}
        self.total_cost = 0.0

    def register_provider(self, name, input_cost=0.0, output_cost=0.0):

        self.providers[name] = {"input_cost": input_cost, "output_cost": output_cost}

    def calculate(self, provider, input_tokens, output_tokens):

        if provider not in self.providers:
            raise KeyError(f"Provider not found: {provider}")

        data = self.providers[provider]

        cost = input_tokens * data["input_cost"] + output_tokens * data["output_cost"]

        self.total_cost += cost

        return {"provider": provider, "cost": cost, "total_cost": self.total_cost}

    def health(self):

        return {
            "status": True,
            "version": self.VERSION,
            "providers": len(self.providers),
            "total_cost": self.total_cost,
        }


if __name__ == "__main__":

    manager = CostManager()

    manager.register_provider("test-model", input_cost=0.001, output_cost=0.002)

    print(manager.health())

    print(manager.calculate("test-model", 100, 50))
