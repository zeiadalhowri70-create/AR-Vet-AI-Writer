import os
import argparse
from dotenv import load_dotenv
from engine.ai_writer import AIWriter
from engine.blogger_poster import BloggerPoster

load_dotenv()


class FinalEngine:
    def __init__(self):
        # تفعيل الكلاسات الأصلية التي تعمل معك
        self.writer = AIWriter()
        self.poster = BloggerPoster()

    def generate_and_post(self, topic):
        print(f"[*] جاري المعالجة الحقيقية للموضوع: {topic}")

        # 1. التوليد باستخدام الذكاء الاصطناعي
        content_data = self.writer.generate({}, [{"title": topic}])
        article_text = content_data[0]["content"]

        # 2. النشر الفعلي في مدونة Blogger
        print("[*] جاري النشر في Blogger...")
        post_link = self.poster.post(topic, article_text)

        print(f"[+] تم النشر بنجاح!")
        print(f"[+] رابط المقال: {post_link}")
        return post_link


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", required=True)
    args = parser.parse_args()

    engine = FinalEngine()
    engine.generate_and_post(args.topic)
