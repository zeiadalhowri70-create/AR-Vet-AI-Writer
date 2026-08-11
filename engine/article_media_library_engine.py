# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Article Media Library Engine

Production Media Asset Collector
"""

from core.image_acquisition_adapter import ImageAcquisitionAdapter


class ArticleMediaLibraryEngine:

    VERSION = "3.0.0"

    def __init__(self, image_adapter=None):

        self.image_adapter = image_adapter or ImageAcquisitionAdapter()

    def build(self, topic):

        image_result = self.image_adapter.generate(
            topic,
            "gross_lesion",
            limit=3
        )

        files = image_result.get("files", [])

        media = {
            "featured_image": {},
            "anatomical_images": [],
            "histopathology": [],
            "scientific_figures": [
                {
                    "type": "pathogenesis_diagram"
                }
            ],
            "diagrams": [],
            "video": {
                "status": "planned"
            }
        }

        if files:

            media["featured_image"] = {
                "path": files[0],
                "type": "gross_lesion"
            }

            media["anatomical_images"] = [
                {
                    "path": item,
                    "type": "gross_lesion"
                }
                for item in files
            ]

        result = {
            "topic": topic,
            "media": media,
            "library_ready": True,
            "version": self.VERSION
        }

        result["valid"] = result["library_ready"]

        return result


    def info(self):

        return {
            "engine": "Article Media Library Engine",
            "version": self.VERSION,
            "status": "production"
        }


if __name__ == "__main__":

    engine = ArticleMediaLibraryEngine()

    print(engine.info())

    print(
        engine.build(
            "مرض النيوكاسل في الدواجن"
        )
    )
