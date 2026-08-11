# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Production Retry Manager

Controls retry policies for AI providers.
"""

import time


class RetryManager:

    VERSION = "1.0.0"

    def __init__(self, max_retries=3, delay_seconds=2):

        self.max_retries = max_retries
        self.delay_seconds = delay_seconds

    def execute(self, function, *args, **kwargs):

        attempts = 0
        last_error = None

        while attempts <= self.max_retries:

            try:

                result = function(*args, **kwargs)

                return {"success": True, "attempts": attempts + 1, "result": result}

            except Exception as error:

                last_error = error
                attempts += 1

                if attempts <= self.max_retries:
                    time.sleep(self.delay_seconds)

        return {"success": False, "attempts": attempts, "error": str(last_error)}

    def health(self):

        return {
            "status": True,
            "version": self.VERSION,
            "max_retries": self.max_retries,
        }


if __name__ == "__main__":

    manager = RetryManager(max_retries=2, delay_seconds=0)

    def test():

        return "AI Provider OK"

    print(manager.health())

    print(manager.execute(test))
