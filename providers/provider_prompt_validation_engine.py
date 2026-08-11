# -*- coding: utf-8 -*-


class ProviderPromptValidationEngine:

    def validate(self, prompt):

        return {"valid": len(prompt.strip()) > 0, "length": len(prompt)}

    def info(self):

        return {"engine": "Provider Prompt Validation Engine", "version": "1.0"}
