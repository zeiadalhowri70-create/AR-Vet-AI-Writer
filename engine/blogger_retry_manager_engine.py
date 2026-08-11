# -*- coding: utf-8 -*-


class BloggerRetryManagerEngine:

    VERSION = "1.0"

    def retry(self, operation, attempts=3):

        return {
            "operation": operation,
            "max_attempts": attempts,
            "status": "retry_ready",
        }

    def info(self):

        return {
            "engine": "Blogger Retry Manager Engine",
            "version": self.VERSION,
            "status": "production",
        }
