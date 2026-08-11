# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Veterinary Brain API Gateway
Production Final v1.0.0
"""

from core.veterinary_brain_integration_engine import VeterinaryBrainIntegrationEngine


class VeterinaryBrainAPIGateway:

    VERSION = "1.0.0"

    def __init__(self, integration_engine=None):
        self.integration_engine = (
            integration_engine or VeterinaryBrainIntegrationEngine()
        )
        self.requests = []

    def process(self, request):

        if not isinstance(request, dict):
            return {"status": False, "error": "invalid_request"}

        result = self.integration_engine.execute(request)

        self.requests.append(result)

        return result

    def health(self):

        return {
            "status": True,
            "gateway": "Veterinary Brain API Gateway",
            "version": self.VERSION,
            "connected": self.integration_engine is not None,
            "processed_requests": len(self.requests),
        }
