# -*- coding: utf-8 -*-


class ProviderBillingEngine:

    def summary(self):

        return {"currency": "USD", "total_cost": 0.0, "status": "ready"}

    def info(self):

        return {"engine": "Provider Billing Engine", "version": "1.0"}
