# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
YouTube Publisher
Phase B.2.1
Real Veterinary Video Render Engine
"""

import os
import pickle

from gtts import gTTS
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

from gtts import gTTS
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.VideoClip import ImageClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
from engine.veterinary_video_generator_engine import VeterinaryVideoGeneratorEngine
from engine.article_video_metadata_engine import ArticleVideoMetadataEngine


class YouTubePublisher:

    VERSION = "3.0.0"

    def __init__(self):

        self.output_dir = (
            "/data/data/com.termux/files/home/AR-Vet-AI-Writer/output/videos"
        )

        os.makedirs(
            self.output_dir,
            exist_ok=True
        )

        self.video_generator = VeterinaryVideoGeneratorEngine()
        self.metadata_engine = ArticleVideoMetadataEngine()


    def extract_images(self, media_library):

        images = []

        media = media_library.get(
            "media",
            {}
        )

        featured = media.get(
            "featured_image",
            {}
        )

        if featured.get("path"):
            images.append(
                featured["path"]
            )

        for item in media.get(
            "anatomical_images",
            []
        ):
            if item.get("path"):
                images.append(
                    item["path"]
                )

        return images


    def create_video(
        self,
        article_data,
        filename="veterinary_short.mp4"
    ):

        title = article_data.get(
            "title",
            "مرض بيطري"
        )

        media_library = article_data.get(
            "media_library",
            {}
        )

        images = self.extract_images(
            media_library
        )


        if not images:
            raise ValueError(
                "No media images available"
            )


        try:
            video_script = self.video_generator.generate_video_script(
                article_data
            )

            scenes = video_script.get(
                "storyboard",
                []
            )

            voice_text = " ".join(
                scene.get("audio_text", "")
                for scene in scenes
            ).strip()

            if not voice_text:
                raise ValueError("Empty storyboard audio")

        except Exception:
            voice_text = (
                f"شرح بيطري شامل عن {title}. "
                "هذا الفيديو يوضح العلامات التشريحية "
                "والأهمية المرضية وطرق الوقاية."
            )


        audio_path = os.path.join(
            self.output_dir,
            "voice.mp3"
        )


        tts = gTTS(
            text=voice_text,
            lang="ar"
        )

        tts.save(
            audio_path
        )


        audio = AudioFileClip(
            audio_path
        )


        duration = audio.duration / len(images)


        clips = []

        for image in images:

            clip = (
                ImageClip(image)
                .set_duration(duration)
                
            )

            clips.append(
                clip
            )


        video = concatenate_videoclips(
            clips,
            method="compose"
        )


        video = video.set_audio(
            audio
        )


        output = os.path.join(
            self.output_dir,
            filename
        )


        video.write_videofile(
            output,
            fps=24,
            codec="libx264",
            audio_codec="aac"
        )


        metadata = self.metadata_engine.generate(title)

        return {
            "status": "ready",
            "video_path": output,
            "images_used": len(images),
            "metadata": metadata,
            "version": self.VERSION
        }



    def upload_to_youtube(
        self,
        video_path,
        title,
        description="",
        tags=None,
        privacy_status="private",
        category_id="27",
    ):
        """Upload a rendered veterinary video to YouTube."""

        project_root = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )
        token_path = os.path.join(
            project_root,
            "youtube_token.pickle",
        )

        if not os.path.exists(token_path):
            raise FileNotFoundError(
                f"YouTube OAuth token not found: {token_path}"
            )

        if not os.path.exists(video_path):
            raise FileNotFoundError(
                f"Video file not found: {video_path}"
            )

        with open(token_path, "rb") as token_file:
            credentials = pickle.load(token_file)

        if not credentials.valid:
            if credentials.expired and credentials.refresh_token:
                from google.auth.transport.requests import Request

                credentials.refresh(Request())
            else:
                raise RuntimeError(
                    "YouTube OAuth credentials are invalid "
                    "and cannot be refreshed."
                )

        youtube = build(
            "youtube",
            "v3",
            credentials=credentials,
            cache_discovery=False,
        )

        body = {
            "snippet": {
                "title": title,
                "description": description,
                "tags": tags or [],
                "categoryId": category_id,
            },
            "status": {
                "privacyStatus": privacy_status,
                "selfDeclaredMadeForKids": False,
            },
        }

        media = MediaFileUpload(
            video_path,
            mimetype="video/mp4",
            resumable=True,
        )

        request = youtube.videos().insert(
            part="snippet,status",
            body=body,
            media_body=media,
        )

        response = None

        while response is None:
            _, response = request.next_chunk()

        video_id = response.get("id")

        if not video_id:
            raise RuntimeError(
                f"YouTube upload returned no video ID: {response}"
            )

        return {
            "youtube_status": "uploaded",
            "youtube_video_id": video_id,
            "youtube_url": (
                f"https://www.youtube.com/watch?v={video_id}"
            ),
            "privacy_status": privacy_status,
        }

    def build_social_payload(self, video_result, article_url=""):

        metadata = video_result.get(
            "metadata",
            {}
        )

        return {
            "video_path": video_result.get(
                "video_path",
                ""
            ),
            "title": metadata.get(
                "title",
                ""
            ),
            "description": metadata.get(
                "description",
                ""
            ),
            "tags": metadata.get(
                "tags",
                []
            ),
            "article_url": article_url,
            "platforms": [
                "youtube_shorts",
                "facebook_reels",
                "instagram_reels",
                "tiktok"
            ],
            "ready_for_social_pipeline": True
        }


    def info(self):

        return {
            "engine": "YouTube Publisher Render Engine",
            "version": self.VERSION,
            "status": "production"
        }
