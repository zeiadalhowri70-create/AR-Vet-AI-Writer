# -*- coding: utf-8 -*-


class ArticleNavigationEngine:
    """
    ينشئ تنقل المقالات السابق/التالي والسلسلة.
    """

    def __init__(self):
        self.version = "1.0"

    def build(self, article):
        previous_article = article.get(
            "previous_article", {"title": "المقال السابق", "url": "#"}
        )

        next_article = article.get(
            "next_article", {"title": "المقال التالي", "url": "#"}
        )

        series = article.get("series_url", "#")

        return f"""
<section id="article-navigation">

<div class="nav-buttons">

<a class="prev-article"
href="{previous_article.get('url', '#')}">
← {previous_article.get('title', 'المقال السابق')}
</a>

<a class="series-index"
href="{series}">
📚 فهرس السلسلة
</a>

<a class="next-article"
href="{next_article.get('url', '#')}">
{next_article.get('title', 'المقال التالي')} →
</a>

</div>

</section>
"""

    def info(self):
        return {
            "engine": "Article Navigation Engine",
            "version": self.version,
            "status": "production",
        }
