# -*- coding: utf-8 -*-

from engine.article_writer_integration_engine import ArticleWriterIntegrationEngine


class ArticleBloggerFinalDraftEngine:

    def generate(self, topic):

        article = ArticleWriterIntegrationEngine().generate(topic)

        html = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<title>{article['title']}</title>
</head>
<body>

<h1>{article['title']}</h1>

<h2>المقدمة</h2>
<pre>{article['introduction']}</pre>

<h2>التعريف</h2>
<pre>{article['definition']}</pre>

<h2>الأسباب</h2>
<pre>{article['causes']}</pre>

<h2>الأعراض</h2>
<pre>{article['symptoms']}</pre>

<h2>التشخيص</h2>
<pre>{article['diagnosis']}</pre>

<h2>العلاج</h2>
<pre>{article['treatment']}</pre>

</body>
</html>"""

        return {"html_ready": True, "content": html}

    def info(self):

        return {"engine": "Article Blogger Final Draft Engine", "version": "1.0"}
