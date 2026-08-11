# -*- coding: utf-8 -*-


class ArticleSocialShareEngine:
    """
    ينشئ أزرار مشاركة المقال على منصات التواصل.
    """

    def __init__(self):
        self.version = "1.0"

    def build(self, article):
        title = article.get("title", "")
        url = article.get("url", "")

        return f"""
<section id="social-share">
<h2>مشاركة المقال</h2>

<div class="share-buttons">

<a class="share-facebook"
href="https://www.facebook.com/sharer/sharer.php?u={url}"
target="_blank">
Facebook
</a>

<a class="share-x"
href="https://twitter.com/intent/tweet?text={title}&url={url}"
target="_blank">
X
</a>

<a class="share-whatsapp"
href="https://wa.me/?text={title}%20{url}"
target="_blank">
WhatsApp
</a>

<a class="share-telegram"
href="https://t.me/share/url?url={url}&text={title}"
target="_blank">
Telegram
</a>

</div>
</section>
"""

    def info(self):
        return {
            "engine": "Article Social Share Engine",
            "version": self.version,
            "status": "production",
        }
