# -*- coding: utf-8 -*-


class ArticleCoverImageEngine:
    """
    ينشئ صورة الغلاف الرئيسية للمقال.
    """

    def __init__(self):
        self.version = "1.0"

    def build(self, article):
        title = article.get("title", "AR-Vet Article")

        return f"""
<section id="cover-image">
<div class="cover-image">
<img src="cover-placeholder.jpg"
     alt="{title}">
</div>
</section>
"""

    def info(self):
        return {
            "engine": "Article Cover Image Engine",
            "version": self.version,
            "status": "production",
        }
