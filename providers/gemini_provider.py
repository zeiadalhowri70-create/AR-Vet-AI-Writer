import os
import requests
from providers.base_provider import BaseProvider


class GeminiProvider(BaseProvider):
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

    def generate(self, prompt):
        if not self.api_key:
            return {
                "provider": "gemini",
                "success": False,
                "content": "مفتاح جيميناي ناقص",
            }

        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"temperature": 0.3},
        }
        try:
            response = requests.post(
                self.url, params={"key": self.api_key}, json=payload
            )
            if response.status_code == 200:
                res_data = response.json()
                text = res_data["candidates"][0]["content"]["parts"][0]["text"]
                return {"provider": "gemini", "success": True, "content": text}
            return {
                "provider": "gemini",
                "success": False,
                "content": f"Google Error {
                    response.status_code}: {
                    response.text}",
            }
        except Exception as e:
            return {"provider": "gemini", "success": False, "content": str(e)}

    def health(self):
        return bool(self.api_key)
