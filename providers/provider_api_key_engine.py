# -*- coding: utf-8 -*-

import os


class ProviderAPIKeyEngine:

    def get(self, env_name):

        return os.getenv(env_name)

    def exists(self, env_name):

        return self.get(env_name) is not None

    def info(self):

        return {"engine": "Provider API Key Engine", "version": "1.0"}
