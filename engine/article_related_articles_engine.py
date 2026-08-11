# -*- coding: utf-8 -*-


class ArticleRelatedArticlesEngine:
    """
    ينشئ قسم المقالات المرتبطة للمقال.
    """

    def __init__(self):
        self.version = "1.0"

    def build(self, article):
        related = article.get("related_articles", [])

        if not related:
            related = [
                {"title": "مرض الجمبورو IBD في الدواجن", "url": "/search/label/IBD"},
                {"title": "أمراض الدواجن الفيروسية", "url": "/search/label/فيروسات"},
                {"title": "برامج التحصين في الدواجن", "url": "/search/label/تحصين"},
            ]

        html = [
            '<section id="related-articles">',
            "<h2>مقالات ذات صلة</h2>",
            '<div class="related-list">',
        ]

        for item in related:
            html.append(
                '<article class="related-card">'
                '<a href="'
                + item.get("url", "#")
                + '">'
                + item.get("title", "")
                + "</a></article>"
            )

        html.append("</div>")
        html.append("</section>")

        return "\\n".join(html)

    def schema(self, article):
        related = article.get("related_articles", [])

        items = []

        for index, item in enumerate(related, start=1):
            items.append(
                {
                    "@type": "ListItem",
                    "position": index,
                    "name": item.get("title", ""),
                    "url": item.get("url", ""),
                }
            )

        return {
            "@context": "https://schema.org",
            "@type": "ItemList",
            "itemListElement": items,
        }

    def info(self):
        return {
            "engine": "Article Related Articles Engine",
            "version": self.version,
            "status": "production",
        }
