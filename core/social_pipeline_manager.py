from core.linkedin_adapter import LinkedInAdapter
from core.pinterest_adapter import PinterestAdapter
from core.x_adapter import XAdapter

# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Production Social Pipeline Manager

Controls social publishing workflow.
"""


class SocialPipelineManager:

    VERSION = "1.0.0"

    def __init__(
        self,
        facebook=None,
        telegram=None,
        x_adapter=None,
        linkedin=None,
        pinterest=None,
    ):

        self.facebook = facebook
        self.telegram = telegram
        self.x_adapter = x_adapter
        self.linkedin = linkedin
        self.pinterest = pinterest

    def publish(self, content):

        result = {"content": content, "version": self.VERSION, "channels": {}}

        if self.facebook:
            result["channels"]["facebook"] = self.facebook.publish(content)

        if self.telegram:
            result["channels"]["telegram"] = self.telegram.publish(content)

        if self.x_adapter:
            result["channels"]["x"] = self.x_adapter.publish(content)

        if self.linkedin:
            result["channels"]["linkedin"] = self.linkedin.publish(content)

        if self.pinterest:
            result["channels"]["pinterest"] = self.pinterest.publish(content)

        return result

    def health(self):

        return {
            "status": True,
            "version": self.VERSION,
            "facebook": self.facebook is not None,
            "telegram": self.telegram is not None,
            "x": self.x_adapter is not None,
            "linkedin": self.linkedin is not None,
            "pinterest": self.pinterest is not None,
        }

        self.x_adapter = XAdapter()
        self.linkedin_adapter = LinkedInAdapter()
        self.pinterest_adapter = PinterestAdapter()


if __name__ == "__main__":

    manager = SocialPipelineManager()

    print(manager.health())

    print(manager.publish("مرض النيوكاسل في الدواجن"))
