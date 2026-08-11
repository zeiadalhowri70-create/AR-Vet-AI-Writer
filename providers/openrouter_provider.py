# -*- coding: utf-8 -*-

import os
import requests
import config

from providers.base_provider import BaseProvider


class OpenRouterProvider(BaseProvider):

    def __init__(self):

        self.api_key = os.getenv("OPENROUTER_API_KEY")

        self.model = "openai/gpt-oss-20b:free"

        self.url = "https://openrouter.ai/api/v1/chat/completions"

    def generate(self, prompt):

        if not self.api_key:

            return {
                "provider": "openrouter",
                "success": False,
                "content": "OPENROUTER_API_KEY غير موجود",
            }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": getattr(
                config, "BLOG_URL", "https://arvetinfo.blogspot.com"
            ),
            "X-Title": "AR-Vet AI Writer",
        }

        payload = {
            "model": self.model,
            "temperature": 0.3,
            "max_tokens": 3000,
            "messages": [
                {
                    "role": "system",
                    "content": "أنت طبيب بيطري متخصص. اكتب بالعربية الفصحى بأسلوب علمي.",
                },
                {"role": "user", "content": prompt},
            ],
        }

        try:

            r = requests.post(self.url, headers=headers, json=payload, timeout=180)

            if r.status_code != 200:

                return {
                    "provider": "openrouter",
                    "success": False,
                    "content": f"HTTP {r.status_code}: {r.text[:500]}",
                }

            data = r.json()

            return {
                "provider": "openrouter",
                "success": True,
                "content": data["choices"][0]["message"]["content"],
            }

        except Exception as e:

            return {"provider": "openrouter", "success": False, "content": str(e)}

    def health(self):

        return bool(self.api_key)

    def info(self):

        return {
            "provider": "OpenRouter Provider",
            "version": "4.0",
            "model": self.model,
            "url": self.url,
        }
