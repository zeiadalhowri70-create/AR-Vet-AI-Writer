# -*- coding: utf-8 -*-

from datetime import datetime
from pathlib import Path


class ArticleGenerator:

    def __init__(self):
        pass

    def generate(
        self, title, content, category="عام", author="د. زياد الحوري", keywords=None
    ):

        if keywords is None:
            keywords = []

        date = datetime.now().strftime("%Y-%m-%d")

        keywords_text = ", ".join(keywords)

        html = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>{title}</title>

<meta name="author" content="{author}">
<meta name="keywords" content="{keywords_text}">
<meta name="description" content="{title} - مقال بيطري علمي">

<style>

body {{
    font-family: Tahoma, Arial;
    direction: rtl;
    line-height: 2;
    background:#fff;
    padding:20px;
}}

.container {{
    max-width:900px;
    margin:auto;
}}

h1 {{
    color:#1565c0;
}}

h2 {{
    color:#2e7d32;
}}

.info {{
    background:#f2f2f2;
    padding:15px;
    border-radius:10px;
}}

.content {{
    font-size:18px;
}}

.footer {{
    margin-top:40px;
    padding:20px;
    background:#eee;
    text-align:center;
}}

</style>

</head>


<body>

<div class="container">

<h1>{title}</h1>

<div class="info">

<p>الكاتب: {author}</p>

<p>التصنيف: {category}</p>

<p>تاريخ الإنشاء: {date}</p>

</div>


<div class="content">

{content}

</div>


<div class="footer">

مدونة الدكتور زياد الحوري البيطرية

</div>


</div>

</body>

</html>
"""

        return html

    def save(self, html, filename, output_dir="articles"):

        folder = Path(output_dir)

        folder.mkdir(exist_ok=True)

        file_path = folder / filename

        with open(file_path, "w", encoding="utf-8") as f:

            f.write(html)

        return str(file_path)
