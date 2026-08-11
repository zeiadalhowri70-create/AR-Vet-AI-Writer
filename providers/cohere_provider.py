import os
import requests
from providers.base_provider import BaseProvider


class CohereProvider(BaseProvider):
    def __init__(self):
        self.api_key = os.getenv("COHERE_API_KEY")
        self.url = "https://cohere.com"

    def generate(self, prompt):
        if not self.api_key:
            return {
                "provider": "cohere",
                "success": False,
                "content": "مفتاح كوهير ناقص",
            }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        payload = {"model": "command-r-plus", "message": prompt, "temperature": 0.3}

        try:
            response = requests.post(self.url, json=payload, headers=headers)
            if response.status_code == 200:
                text = response.json()["text"]
                return {"provider": "cohere", "success": True, "content": text}
            return {
                "provider": "cohere",
                "success": False,
                "content": f"خطأ من سيرفر كوهير: {response.status_code}",
            }
        except Exception as e:
            return {"provider": "cohere", "success": False, "content": str(e)}

    def health(self):
        return bool(self.api_key)
