# -*- coding: utf-8 -*-
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


class ArticleMedicalWriterEngine:
    def __init__(self):
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"
        self.api_key = os.getenv("OPENROUTER_API_KEY")

    def write_section(self, topic, section_type):
        # سنرسل الطلب للنموذج الذكي
        prompt = f"اكتب نصاً طبياً بيطرياً احترافياً عن {topic}، قسم: {section_type}. بدون مقدمات طويلة."

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://arvetinfo.blogspot.com/",
            "X-Title": "AR-Vet-AI",
        }
        data = {
            "model": "anthropic/claude-3.5-sonnet",
            "messages": [{"role": "user", "content": prompt}],
        }

        try:
            response = requests.post(self.api_url, headers=headers, json=data)
            response_json = response.json()
            # استخراج النص من رد الـ AI
            return response_json["choices"][0]["message"]["content"]
        except Exception as e:
            return f"خطأ تقني في محرك الذكاء: {str(e)}"
