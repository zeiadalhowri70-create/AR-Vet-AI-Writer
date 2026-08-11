# -*- coding: utf-8 -*-
"""
AR-Vet AI Writer
Intelligence Service Manager
"""


class IntelligenceServiceManager:

    VERSION = "1.0.0"

    def __init__(self):

        self.services = {}

    def register_service(self, name, service):

        self.services[name] = service

        return {"status": True, "service": name}

    def health_check(self):

        result = {}

        for name, service in self.services.items():

            try:

                result[name] = service.health()

            except Exception as e:

                result[name] = {"status": False, "error": str(e)}

        return result

    def status(self):

        return {"services": len(self.services), "version": self.VERSION}
