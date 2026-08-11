# -*- coding: utf-8 -*-
"""
AR-Vet AI Writer
Intelligence API Gateway
"""


class IntelligenceAPIGateway:

    VERSION = "1.0.0"

    def __init__(self):

        self.requests = []

    def process(self, request):

        response = {"status": True, "request": request, "message": "processed"}

        self.requests.append(response)

        return response

    def history(self):

        return self.requests

    def health(self):

        return {
            "status": True,
            "gateway": "Intelligence API Gateway",
            "version": self.VERSION,
        }
