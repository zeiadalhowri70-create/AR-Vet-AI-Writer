# -*- coding: utf-8 -*-

from datetime import datetime


class ArticleMetadataBarEngine:
    VERSION = "1.0"

    def build(self, article):
        stats = article.get("statistics", {})
        words = stats.get("words", 0)
        reading = stats.get("reading_time", "-")

        return f"""
<section id="article-meta-bar">
<div class="meta-item">📅 {datetime.now().strftime("%Y-%m-%d")}</div>
<div class="meta-item">📖 {words} كلمة</div>
<div class="meta-item">⏱ {reading}</div>
</section>
"""

    def info(self):
        return {
            "engine": "Article Metadata Bar Engine",
            "version": self.VERSION,
            "status": "production",
        }
