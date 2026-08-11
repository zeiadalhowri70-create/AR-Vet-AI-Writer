# -*- coding: utf-8 -*-

"""
Article Blogger HTML Engine
AR-Vet AI Writer

Stage : P3.1
Version : 1.0
Status  : Production
"""

import html


class ArticleBloggerHTMLEngine:

    def build(self, article):

        if isinstance(article, dict):
            title = article.get("title", "")
            body = article.get("content", "")
        else:
            title = ""
            body = str(article)

        title = html.escape(title)

        return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>

<meta charset="utf-8">

<meta name="viewport"
content="width=device-width,initial-scale=1">

<title>{title}</title>

<meta name="description"
content="{title}">

<meta name="robots"
content="index,follow">

<style>

body{{
font-family:Tahoma,Arial,sans-serif;
direction:rtl;
background:#f5f5f5;
margin:0;
padding:30px;
line-height:2;
}}

article{{
max-width:900px;
margin:auto;
background:#fff;
padding:40px;
border-radius:10px;
box-shadow:0 0 10px rgba(0,0,0,.08);
}}

h1{{
color:#146c43;
margin-top:0;
}}

h2{{
margin-top:35px;
color:#0d6efd;
border-bottom:2px solid #eee;
padding-bottom:8px;
}}

p{{
font-size:18px;
text-align:justify;
}}

</style>

</head>

<body>

<article>

{body}

</article>

</body>
</html>
"""

    def info(self):

        return {
            "engine": "Article Blogger HTML Engine",
            "version": "1.0",
            "status": "production",
            "blogger_ready": True,
        }
