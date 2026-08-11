import os
from dotenv import load_dotenv
from engine.ai_writer import AIWriter
from engine.blogger_poster import BloggerPoster

load_dotenv()


def run_real_job(topic):
    print(f"[*] جاري توليد مقال علمي عن: {topic}")

    writer = AIWriter()
    # توليد المحتوى
    content_list = writer.generate({}, [{"title": topic}])
    article_text = content_list[0]["content"]

    print("[*] جاري الاتصال بمدونة Blogger...")
    poster = BloggerPoster()

    # محاولة النشر
    try:
        response = poster.post(topic, article_text)
        print(f"[+] تم النشر بنجاح! الرابط: {response}")
    except Exception as e:
        print(f"[!] حدث خطأ أثناء النشر: {e}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", required=True)
    args = parser.parse_args()
    run_real_job(args.topic)
