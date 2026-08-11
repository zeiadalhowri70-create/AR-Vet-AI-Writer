# -*- coding: utf-8 -*-

import sys

from platform_core.integration.platform_bootstrap import PlatformBootstrap

BLOG_ID = "8962115474116118357"


def main():
    topic = sys.argv[1] if len(sys.argv) > 1 else "مرض بيطري"

    print(f"🚀 بدء توليد المقال: {topic}")

    platform = PlatformBootstrap()

    article = platform.generate(topic)

    if isinstance(article, dict):
        content = (
            article.get("html")
            or article.get("content")
            or article.get("blogger_draft")
            or ""
        )
    else:
        content = str(article)

    if not content.strip():
        print("❌ فشل توليد المحتوى. تم إيقاف النشر.")
        return

    print("🚀 جاري رفع المقال إلى Blogger...")

    result = platform.publish(
        title=topic,
        html=content,
        draft=True,
    )

    print("✅ تم النشر بنجاح")
    print(result)


if __name__ == "__main__":
    main()
