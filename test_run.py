import os
import sys
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# إضافة مسارات المشروع
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
ENGINE_PATH = os.path.join(PROJECT_ROOT, "engine")

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

if ENGINE_PATH not in sys.path:
    sys.path.insert(0, ENGINE_PATH)

try:
    from engine.blogger_publisher import BloggerPublisher
except Exception as e:
    print(f"خطأ في استيراد BloggerPublisher:\n{e}")
    raise


def main():
    print("=" * 60)
    print("AR-Vet AI Writer")
    print("اختبار Blogger Publisher")
    print("=" * 60)

    publisher = BloggerPublisher()

    if publisher.health_check():
        print("\n✅ الاتصال بمدونة Blogger ناجح.")
        print("اسم المدونة:", publisher.name())
    else:
        print("\n❌ فشل الاتصال بمدونة Blogger.")


if __name__ == "__main__":
    main()
