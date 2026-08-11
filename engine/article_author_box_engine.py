# -*- coding: utf-8 -*-


class ArticleAuthorBoxEngine:
    """
    ينشئ صندوق الكاتب النهائي للمقالات.
    """

    def __init__(self):
        self.version = "1.0"

    def build(self, author=None):
        if not author:
            author = {
                "name": "الدكتور زياد الحوري",
                "title": "طبيب بيطري وكاتب محتوى بيطري",
                "url": "/p/about.html",
                "image": "",
            }

        html = f"""
<section id="author-box" class="author-box">

<div class="author-info">

<div class="author-avatar">
<img src="{author.get('image', '')}"
alt="{author.get('name', '')}"
loading="lazy">
</div>

<div class="author-details">
<h3>{author.get('name', '')}</h3>
<p>{author.get('title', '')}</p>
<a href="{author.get('url', '#')}">
الملف الشخصي
</a>
</div>

</div>

</section>
"""

        return html

    def schema(self, author=None):
        if not author:
            author = {"name": "الدكتور زياد الحوري", "url": "/p/about.html"}

        return {
            "@context": "https://schema.org",
            "@type": "Person",
            "name": author.get("name"),
            "url": author.get("url"),
        }

    def info(self):
        return {
            "engine": "Article Author Box Engine",
            "version": self.version,
            "status": "production",
        }
