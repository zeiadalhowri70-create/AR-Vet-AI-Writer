# -*- coding: utf-8 -*-
"""
OpenRouter Provider
AR-Vet AI Writer
"""

import os
import requests
from providers.base_provider import BaseProvider

class OpenRouterProvider(BaseProvider):
    def __init__(self):
        # قراءة المفتاح من النظام، وإذا لم يكن موجوداً نستخدم المفتاح الخاص بك المدمج بالأسفل
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        if not self.api_key or self.api_key == "":
            self.api_key = "REMOVED_SECRET"

        self.url = "https://openrouter.ai"
        self.model = "google/gemini-2.5-flash"

    def generate(self, prompt):
        if not self.api_key:
            return "خطأ: لم يتم العثور على مفتاح OPENROUTER_API_KEY صحيح"
            
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
        
        try:
            response = requests.post(
                self.url,
                headers=headers,
                json=payload,
                timeout=120
            )
            
            if response.status_code != 200:
                return f"OpenRouter Error {response.status_code}: {response.text}"
                
            data = response.json()
            return data["choices"][0]["message"]["content"]
            
        except Exception as e:
            return f"Exception: {e}"

    def name(self):
        return "OpenRouter"

    def health_check(self):
        return True

