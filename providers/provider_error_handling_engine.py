# -*- coding: utf-8 -*-


class ProviderErrorHandlingEngine:

    def handle(self, error):

        return {"handled": True, "message": str(error)}

    def info(self):

        return {"engine": "Provider Error Handling Engine", "version": "1.0"}
