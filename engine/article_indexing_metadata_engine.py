# -*- coding: utf-8 -*-

from datetime import datetime, timezone
from xml.sax.saxutils import escape


class ArticleIndexingMetadataEngine:
    """
    Enterprise Indexing Metadata Engine v2.0
    Production SEO indexing layer.
    """

    VERSION = "2.0"

    def build(self, article):

        title = article.get("title", "")
        url = article.get("canonical_url", "")

        now = datetime.now(timezone.utc).strftime("%Y-%m-%d")

        sitemap_entry = f"""
<url>
    <loc>{escape(url)}</loc>
    <lastmod>{now}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
</url>
""".strip()

        return {
            "canonical_url": url,
            "robots": {"index": True, "follow": True, "content": "index, follow"},
            "sitemap": {
                "entry": sitemap_entry,
                "last_modified": now,
                "priority": 0.8,
                "change_frequency": "weekly",
            },
            "google": {"discoverable": True, "news_ready": False, "search_ready": True},
            "article": {"title": title, "indexed": True},
        }

    def info(self):

        return {
            "engine": "Enterprise Indexing Metadata Engine",
            "version": self.VERSION,
            "status": "production",
            "sitemap_xml": True,
            "google_ready": True,
        }
