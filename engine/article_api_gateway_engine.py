# -*- coding: utf-8 -*-


class ArticleAPIGatewayEngine:

    def request(self, topic):

        return {"topic": topic, "api_ready": True}

    def info(self):

        return {"engine": "Article API Gateway Engine", "version": "1.0"}
