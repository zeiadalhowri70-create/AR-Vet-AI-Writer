# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Production Image Acquisition Adapter

Connects Image Intelligence Layer with real image sources.
"""

from engine.image_scraper import ImageScraper


class ImageAcquisitionAdapter:

    VERSION = "1.0.0"

    def __init__(self, scraper=None):
        self.scraper = scraper or ImageScraper()

    def generate(self, article, image_type="gross_lesion", limit=3):

        topic = article if isinstance(article, str) else article.get(
            "title",
            "veterinary disease"
        )

        query = f"{topic} {image_type}"

        files = self.scraper.download_disease_images(
            query,
            limit=limit
        )

        return {
            "topic": topic,
            "image_type": image_type,
            "files": files,
            "count": len(files),
            "status": "ready" if files else "empty",
        }

    def health(self):

        return {
            "status": True,
            "version": self.VERSION,
            "scraper_connected": self.scraper is not None,
        }


if __name__ == "__main__":

    adapter = ImageAcquisitionAdapter()

    print(adapter.health())

    print(
        adapter.generate(
            "مرض النيوكاسل في الدواجن",
            "gross_lesion"
        )
    )
