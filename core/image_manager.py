# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Image Manager
Media Intelligence Upgrade Phase A.2
"""

from pathlib import Path
import hashlib
import json


class ImageManager:

    VERSION = "2.0.0"

    def __init__(self, media_folder="media"):
        self.media_folder = Path(media_folder)
        self.media_folder.mkdir(
            exist_ok=True
        )

    def create_media_id(self, topic):
        return hashlib.sha256(
            topic.encode("utf-8")
        ).hexdigest()[:16]

    def build_image_record(
        self,
        topic,
        image_type="anatomical",
        prompt=""
    ):
        return {
            "media_id": self.create_media_id(topic),
            "topic": topic,
            "type": image_type,
            "prompt": prompt,
            "status": "ready_for_provider",
            "url": "",
        }

    def save_metadata(self, record):
        file = self.media_folder / (
            record["media_id"] + ".json"
        )

        file.write_text(
            json.dumps(
                record,
                ensure_ascii=False,
                indent=2
            ),
            encoding="utf-8"
        )

        return str(file)

    def info(self):
        return {
            "engine": "Image Manager",
            "version": self.VERSION,
            "status": "production",
        }
