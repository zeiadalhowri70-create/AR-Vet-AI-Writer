# -*- coding: utf-8 -*-
"""
AR-Vet AI Writer
Intelligence Health Monitor
"""


class IntelligenceHealthMonitor:

    VERSION = "1.0.0"

    def __init__(self):

        self.reports = []

    def check_service(self, name, service):

        try:

            status = service.health()

            report = {"service": name, "status": status}

        except Exception as e:

            report = {"service": name, "status": False, "error": str(e)}

        self.reports.append(report)

        return report

    def get_reports(self):

        return self.reports

    def health(self):

        return {
            "status": True,
            "monitor": "Intelligence Health Monitor",
            "version": self.VERSION,
        }
