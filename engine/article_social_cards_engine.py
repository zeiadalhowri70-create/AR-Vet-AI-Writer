# -*- coding: utf-8 -*-


class ArticleSocialCardsEngine:
    """
    Open Graph + Social Cards Engine v1.0
    تجهيز بيانات المشاركة الاجتماعية.
    """

    VERSION = "1.0"

    def build(self, article):

        title = article.get("title", "")

        return {
            "open_graph": {
                "og:title": title,
                "og:description": (
                    f"مقال علمي شامل حول {title} " "من موسوعة AR-Vet Info."
                ),
                "og:type": "article",
                "og:url": "",
                "og:image": "",
            },
            "twitter_card": {
                "card": "summary_large_image",
                "title": title,
                "description": (f"دليل بيطري متخصص حول {title}"),
                "image": "",
            },
        }

    def info(self):

        return {
            "engine": "Article Social Cards Engine",
            "version": self.VERSION,
            "status": "production",
            "open_graph": True,
            "twitter_card": True,
        }
