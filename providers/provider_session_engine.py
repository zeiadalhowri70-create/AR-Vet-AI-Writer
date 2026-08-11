# -*- coding: utf-8 -*-


class ProviderSessionEngine:

    def session(self):

        return {"active": True, "session_id": "provider-session-v1"}

    def info(self):

        return {"engine": "Provider Session Engine", "version": "1.0"}
