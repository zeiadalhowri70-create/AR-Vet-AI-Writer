# -*- coding: utf-8 -*-


class ArticleCSSEngine:

    VERSION = "1.0"

    def build(self):

        return """
<style>

:root{
    --primary:#0f766e;
    --secondary:#134e4a;
    --background:#f8fafc;
    --surface:#ffffff;
    --text:#1f2937;
    --border:#d1d5db;
    --radius:12px;
}

*{
    box-sizing:border-box;
}

body{
    margin:0;
    padding:0;
    background:var(--background);
    color:var(--text);
    font-family:"Tajawal","Cairo",sans-serif;
    line-height:1.9;
}

#site-header{
    background:var(--primary);
    color:#fff;
    padding:40px 20px;
    text-align:center;
}

#article-content{
    max-width:900px;
    margin:40px auto;
    background:var(--surface);
    padding:40px;
    border-radius:var(--radius);
    box-shadow:0 4px 18px rgba(0,0,0,.08);
}

h1,h2,h3{
    color:var(--secondary);
}

img{
    max-width:100%;
    height:auto;
}

table{
    width:100%;
    border-collapse:collapse;
}

table td,
table th{
    border:1px solid var(--border);
    padding:10px;
}

#site-footer{
    margin-top:60px;
    padding:30px;
    text-align:center;
    color:#666;
}

</style>
"""

    def info(self):
        return {
            "engine": "Article CSS Engine",
            "version": "1.0",
            "status": "production",
        }
