# -*- coding: utf-8 -*-

import os

from engine.article_writer_integration_engine import ArticleWriterIntegrationEngine
from engine.article_html_writer_engine import ArticleHTMLWriterEngine
from engine.blogger_production_pipeline_engine import BloggerProductionPipelineEngine


class ArticleProductionPipelineEngine:

    def __init__(self):

        self.writer = ArticleWriterIntegrationEngine()
        self.html = ArticleHTMLWriterEngine()
        self.production = BloggerProductionPipelineEngine()

        os.makedirs("output", exist_ok=True)

    def build(self, topic):

        article = self.writer.generate(topic)

        if isinstance(article, dict):

            title = article.get("title", topic)

            body = article.get("content", "")

            faq_html = article.get("faq_html", "")

            faq_schema = article.get("faq_schema", "")

            if isinstance(faq_schema, dict):
                import json

                faq_schema = json.dumps(faq_schema, ensure_ascii=False, indent=2)

            body = body + "\n" + faq_html + "\n" + faq_schema

        else:

            title = topic
            body = str(article)

        html = self.html.render(title, body)

        filename = f"output/{topic.replace(' ', '_')}.html"

        with open(filename, "w", encoding="utf-8") as f:

            f.write(html)

        if isinstance(article, dict):
            article["html"] = html
            article["html_path"] = filename

        production_result = self.production.process(article)

        return {
            "article": article,
            "html_path": filename,
            "production": production_result,
            "title": title,
            "production_status": "ready",
            "engine": "Article Production Pipeline Engine",
            "version": "4.1",
        }

    def info(self):

        return {
            "engine": "Article Production Pipeline Engine",
            "version": "4.0",
            "status": "production",
            "writer": "connected",
            "html_writer": "connected",
            "faq": True,
        }
