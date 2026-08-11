import os
import requests


class UnsplashProvider:
    def __init__(self):
        self.access_key = os.getenv("UNSPLASH_ACCESS_KEY")
        self.url = "https://unsplash.com"

    def get_animal_image(self, query):
        if not self.access_key:
            return None
        headers = {"Authorization": f"Client-ID {self.access_key}"}
        params = {"query": query, "per_page": 1, "orientation": "landscape"}
        try:
            response = requests.get(self.url, headers=headers, params=params)
            if response.status_code == 200:
                data = response.json()
                if data["results"]:
                    return data["results"][0]["urls"]["regular"]
        except Exception:
            return None
        return None
