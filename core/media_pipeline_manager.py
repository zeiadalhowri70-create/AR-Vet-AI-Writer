# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Production Media Pipeline Manager

Full media assembly workflow.
"""


class MediaPipelineManager:

    VERSION = "1.2.0"

    def __init__(self, image_adapter=None, alt_adapter=None, video_adapter=None, enable_video=False):

        self.image = image_adapter
        self.alt = alt_adapter
        self.video = video_adapter
        self.enable_video = enable_video

    def build(self, article):

        package = {"article": article, "version": self.VERSION, "media": {}}

        if self.image:

            package["media"]["image"] = self.image.generate(article)

        if self.alt:

            package["media"]["alt"] = self.alt.generate(article)

        if self.video and self.enable_video:

            package["media"]["video"] = self.video.generate(article)

        return package

    def health(self):

        return {
            "status": True,
            "version": self.VERSION,
            "image": self.image is not None,
            "alt": self.alt is not None,
            "video": self.video is not None,
            "video_enabled": self.enable_video,
        }


if __name__ == "__main__":

    manager = MediaPipelineManager()

    print(manager.health())

    print(manager.build("مرض النيوكاسل في الدواجن"))
