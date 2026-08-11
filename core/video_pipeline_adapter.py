# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Production Video Pipeline Adapter

Connects Media Pipeline with Video Intelligence Layer.
"""

from engine.veterinary_video_generator_engine import VeterinaryVideoGeneratorEngine
from engine.article_video_metadata_engine import ArticleVideoMetadataEngine
from engine.youtube_publisher import YouTubePublisher


class VideoPipelineAdapter:

    VERSION = "1.0.0"

    def __init__(
        self,
        video_generator=None,
        metadata_engine=None,
        publisher=None,
    ):

        self.video_generator = (
            video_generator or VeterinaryVideoGeneratorEngine()
        )

        self.metadata_engine = (
            metadata_engine or ArticleVideoMetadataEngine()
        )

        self.publisher = (
            publisher or YouTubePublisher()
        )


    def generate(self, article):

        topic = (
            article.get("title", "مرض بيطري")
            if isinstance(article, dict)
            else str(article)
        )

        metadata = self.metadata_engine.generate(topic)

        if isinstance(article, dict):
            article_data = article.copy()
        else:
            article_data = {
                "title": topic
            }

        script = self.video_generator.generate_video_script(
            article_data
        )

        video_result = self.publisher.create_video(
            article_data,
            filename="veterinary_pipeline_video.mp4"
        )

        # Real YouTube production upload bridge.
        # Keep the existing render result intact and append upload metadata.
        upload_result = self.publisher.upload_to_youtube(
            video_path=video_result.get("video_path", ""),
            title=metadata.get("title", topic),
            description=metadata.get("description", ""),
            tags=metadata.get("tags", []),
            privacy_status="private",
        )

        return {
            **video_result,
            **upload_result,
            "metadata": metadata,
            "script": script,
            "status": "ready",
            "version": self.VERSION,
        }


    def health(self):

        return {
            "status": True,
            "version": self.VERSION,
            "video_generator": self.video_generator is not None,
            "metadata_engine": self.metadata_engine is not None,
            "publisher": self.publisher is not None,
        }


if __name__ == "__main__":

    adapter = VideoPipelineAdapter()

    print(adapter.health())
