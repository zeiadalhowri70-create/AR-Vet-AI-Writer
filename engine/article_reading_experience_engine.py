# -*- coding: utf-8 -*-

import math
import re


class ArticleReadingExperienceEngine:
    def __init__(self, words_per_minute=200):
        self.words_per_minute = words_per_minute

    def _count_words(self, text):
        return len(re.findall(r"\S+", text or ""))

    def generate(self, article):
        text = article.get("content", "")
        words = self._count_words(text)
        minutes = max(1, math.ceil(words / self.words_per_minute))

        return f"""
<div id="reading-experience">

<div id="reading-progress">
<div id="reading-progress-bar"></div>
</div>

<div id="reading-meta">
<span>📖 {words} كلمة</span>
<span>⏱ {minutes} دقيقة قراءة</span>
</div>

<div id="reading-actions">
<button onclick="window.print()">🖨 طباعة</button>
<button onclick="navigator.clipboard.writeText(document.body.innerText)">📋 نسخ</button>
</div>

</div>

<script>
window.addEventListener("scroll",function(){{
const h=document.documentElement;
const s=(h.scrollTop)/(h.scrollHeight-h.clientHeight)*100;
const b=document.getElementById("reading-progress-bar");
if(b) b.style.width=s+"%";
}});
</script>
"""

    def info(self):
        return {
            "engine": "Article Reading Experience Engine",
            "version": "1.0",
            "status": "production",
        }
