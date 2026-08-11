# -*- coding: utf-8 -*-


class BloggerJobTrackerEngine:

    VERSION = "1.0"

    def track(self, job, status):

        job["status"] = status

        return job

    def info(self):

        return {
            "engine": "Blogger Job Tracker Engine",
            "version": self.VERSION,
            "status": "production",
        }
