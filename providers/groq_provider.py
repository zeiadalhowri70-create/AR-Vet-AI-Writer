# -*- coding: utf-8 -*-

import os
import requests
from providers.base_provider import BaseProvider


class GroqProvider(BaseProvider):

    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.url = "https://api.groq.com/openai/v1/chat/completions"

        self.model = "llama-3.1-8b-instant"

    def generate(self, prompt):

        if not self.api_key:
            return {
                "provider": "groq",
                "success": False,
                "content": "GROQ_API_KEY غير موجود",
            }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": self.model,
            "temperature": 0.25,
            "max_tokens": 4000,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "أنت طبيب بيطري متخصص في أمراض الدواجن. "
                        "اكتب باللغة العربية الفصحى بأسلوب موسوعي علمي دقيق. "
                        "استخدم المصطلحات البيطرية الصحيحة."
                    ),
                },
                {"role": "user", "content": prompt},
            ],
        }

        try:
            response = requests.post(
                self.url, headers=headers, json=payload, timeout=180
            )

            if response.status_code == 200:

                data = response.json()

                return {
                    "provider": "groq",
                    "success": True,
                    "content": data["choices"][0]["message"]["content"],
                }

            return {
                "provider": "groq",
                "success": False,
                "content": f"Groq Error {response.status_code}: {response.text[:500]}",
            }

        except Exception as e:

            return {"provider": "groq", "success": False, "content": str(e)}

    def health(self):
        return bool(self.api_key)

    def info(self):

        return {
            "provider": "GroqProvider",
            "version": "2.0",
            "model": self.model,
            "status": "production",
        }
