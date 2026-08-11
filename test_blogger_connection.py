# -*- coding: utf-8 -*-
# نقوم باستيراد الملف الصحيح كما ظهر في قائمة الملفات لديك
from engine.blogger_publisher import BloggerPublisher


def test_connection():
    print("--- بدء فحص الاتصال بـ Blogger ---")
    try:
        # تأكد من استخدام اسم الكلاس الصحيح (غالباً BloggerPublisher)
        publisher = BloggerPublisher()
        if hasattr(publisher, "check_connection"):
            result = publisher.check_connection()
            print(f"[✓] نجح الاتصال! الحالة: {result}")
        else:
            print("[!] المحرك موجود ولكن دالة check_connection غير معرفة.")
            print(f"[!] المتاح في المحرك: {dir(publisher)}")
    except Exception as e:
        print(f"[X] فشل الاتصال. التفاصيل: {e}")


if __name__ == "__main__":
    test_connection()
