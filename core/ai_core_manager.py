# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Production AI Core Manager

Unified controller for AI production components.
"""

try:
    from core.prompt_manager import PromptManager
    from core.prompt_templates_engine import PromptTemplatesEngine
    from core.token_budget_manager import TokenBudgetManager
    from core.retry_manager import RetryManager
    from core.cost_manager import CostManager
    from core.model_router import ModelRouter

except ModuleNotFoundError:
    from prompt_manager import PromptManager
    from prompt_templates_engine import PromptTemplatesEngine
    from token_budget_manager import TokenBudgetManager
    from retry_manager import RetryManager
    from cost_manager import CostManager
    from model_router import ModelRouter


class AICoreManager:

    VERSION = "1.0.0"

    def __init__(self):

        self.prompt_manager = PromptManager()
        self.templates = PromptTemplatesEngine()
        self.token_budget = TokenBudgetManager()
        self.retry = RetryManager()
        self.cost = CostManager()
        self.router = ModelRouter()

    def health(self):

        return {
            "status": True,
            "version": self.VERSION,
            "components": {
                "prompt_manager": True,
                "templates": True,
                "token_budget": True,
                "retry": True,
                "cost": True,
                "router": True,
            },
        }

    def build_prompt(self, template, **kwargs):

        return self.templates.render(template, **kwargs)


if __name__ == "__main__":

    manager = AICoreManager()

    print(manager.health())

    print(manager.build_prompt("veterinary_article", topic="مرض النيوكاسل في الدواجن"))
