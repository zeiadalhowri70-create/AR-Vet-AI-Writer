# -*- coding: utf-8 -*-


class ArticleSEOMetaEngine:
    """
    ينشئ بيانات SEO و Meta Tags للمقالات.
    """

    def __init__(self):
        self.version = "1.0"

    def build(self, article):
        title = article.get("title", "")
        description = article.get(
            "description", "مقال علمي بيطري شامل من مدونة الدكتور زياد الحوري"
        )
        url = article.get("url", "")
        keywords = article.get("keywords", "طب بيطري, أمراض الدواجن, النيوكاسل")

        return f"""
<meta name="description" content="{description}">
<meta name="keywords" content="{keywords}">
<link rel="canonical" href="{url}">

<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="article">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">

<meta name="robots" content="index, follow">
"""

    def info(self):
        return {
            "engine": "Article SEO Meta Engine",
            "version": self.version,
            "status": "production",
        }
