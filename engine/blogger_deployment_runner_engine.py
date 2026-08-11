# -*- coding: utf-8 -*-

from engine.blogger_deployment_verifier_engine import BloggerDeploymentVerifierEngine

from engine.blogger_release_report_engine import BloggerReleaseReportEngine


class BloggerDeploymentRunnerEngine:

    VERSION = "1.0"

    def run(self):

        verifier = BloggerDeploymentVerifierEngine()

        result = verifier.verify()

        report = BloggerReleaseReportEngine().generate(result)

        return report

    def info(self):

        return {
            "engine": "Blogger Deployment Runner Engine",
            "version": self.VERSION,
            "status": "production",
        }
