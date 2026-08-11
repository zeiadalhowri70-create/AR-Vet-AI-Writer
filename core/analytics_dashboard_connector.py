# -*- coding: utf-8 -*-
"""
AR-Vet AI Writer
Analytics Dashboard Connector
"""

from core.analytics_memory_engine import AnalyticsMemoryEngine


class AnalyticsDashboardConnector:

    VERSION = "1.0.0"

    def __init__(self):

        self.analytics = AnalyticsMemoryEngine()

    def build_dashboard_data(self):

        metrics = self.analytics.get_metrics()

        return {
            "status": True,
            "metrics_count": len(metrics),
            "metrics": metrics,
            "connector": "Analytics Dashboard Connector",
            "version": self.VERSION,
        }

    def get_summary(self):

        data = self.build_dashboard_data()

        return {
            "analytics": True,
            "records": data["metrics_count"],
            "version": self.VERSION,
        }

    def health(self):

        return {
            "status": True,
            "connector": "Analytics Dashboard Connector",
            "version": self.VERSION,
        }
