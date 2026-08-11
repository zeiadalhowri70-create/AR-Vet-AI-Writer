# -*- coding: utf-8 -*-


class ArticleImagePlaceholderEngine:
    """
    ينشئ مكان الصور داخل المقال.
    """

    def __init__(self):
        self.version = "1.0"

    def build(self, article):
        title = article.get("title", "صورة المقال")

        return f"""
<section id="article-image">
<div class="article-image-placeholder">
<img
src="/images/article-placeholder.jpg"
alt="{title}">
</div>
</section>
"""

    def info(self):
        return {
            "engine": "Article Image Placeholder Engine",
            "version": self.version,
            "status": "production",
        }
