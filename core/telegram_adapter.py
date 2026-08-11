# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Production Telegram Adapter

Connector for Telegram publishing.
"""


class TelegramAdapter:

    VERSION = "1.0.0"

    def __init__(self, api=None):

        self.api = api

    def publish(self, content):

        if not self.api:

            return {
                "status": False,
                "channel": "telegram",
                "error": "Telegram API unavailable",
                "content": content,
            }

        return self.api.publish(content)

    def health(self):

        return {
            "status": True,
            "version": self.VERSION,
            "api_connected": self.api is not None,
        }


if __name__ == "__main__":

    adapter = TelegramAdapter()

    print(adapter.health())

    print(adapter.publish("مرض النيوكاسل في الدواجن"))
