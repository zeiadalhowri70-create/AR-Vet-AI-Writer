# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Production Model Router

Selects suitable AI model based on task.
"""


class ModelRouter:

    VERSION = "1.0.0"

    def __init__(self):

        self.models = {}

    def register_model(self, name, provider, tasks, priority=1):

        self.models[name] = {"provider": provider, "tasks": tasks, "priority": priority}

    def select(self, task):

        candidates = []

        for name, data in self.models.items():

            if task in data["tasks"]:
                candidates.append((name, data))

        if not candidates:
            return None

        candidates.sort(key=lambda x: x[1]["priority"])

        name, data = candidates[0]

        return {
            "model": name,
            "provider": data["provider"],
            "priority": data["priority"],
        }

    def list_models(self):

        return list(self.models.keys())

    def health(self):

        return {"status": True, "version": self.VERSION, "models": len(self.models)}


if __name__ == "__main__":

    router = ModelRouter()

    router.register_model("deepseek-chat", "openrouter", ["article", "seo"], priority=1)

    router.register_model("gemini-pro", "google", ["analysis"], priority=2)

    print(router.health())

    print(router.select("article"))
