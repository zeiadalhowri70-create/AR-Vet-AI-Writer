# -*- coding: utf-8 -*-


class ProviderResponseValidationEngine:

    def validate(self, response):

        return {"valid": (isinstance(response, dict) and "content" in response)}

    def info(self):

        return {"engine": "Provider Response Validation Engine", "version": "1.0"}
