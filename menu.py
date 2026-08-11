# -*- coding: utf-8 -*-
import os
import subprocess


def run_menu():
    print("\n" + "=" * 45)
    print("  🤖 لوحة تحكم مشروع AR-Vet-AI-Writer الاحترافية 🤖")
    print("=" * 45)

    # 1. اختيار الذكاء الاصطناعي
    print("\n🔹 [الخطوة 1] اختر مزود الذكاء الاصطناعي:")
    print("1) Google Gemini (الأدق والأنصح به)")
    print("2) Groq Llama (الأسرع عالمياً)")
    print("3) Cohere (للمقالات الطويلة المعمقة)")
    print("4) OpenRouter (الخيار الاحتياطي)")

    choice = input("\n✍️ أدخل رقم الاختيار (1-4): ").strip()

    providers = {"1": "gemini", "2": "groq", "3": "cohere", "4": "openrouter"}
    selected_provider = providers.get(choice, "gemini")

    # تحديث ملف config.py تلقائياً وبأمان
    if os.path.exists("config.py"):
        with open("config.py", "r", encoding="utf-8") as f:
            lines = f.readlines()

        with open("config.py", "w", encoding="utf-8") as f:
            for line in lines:
                if line.startswith("ACTIVE_PROVIDER"):
                    f.write(f'ACTIVE_PROVIDER = "{selected_provider}"\n')
                else:
                    f.write(line)
        print(f"🔹 تم تفعيل المزوّد بنجاح: {selected_provider.upper()}")
    else:
        print("⚠️ ملف config.py غير موجود في هذا المجلد!")

    # 2. تحديد عنوان المقال
    print("\n🔹 [الخطوة 2] حدد عنوان المقال البيطري الجديد:")
    title = input("✍️ اكتب أو الصق عنوان المقالة هنا واضغط Enter:\n👉 ").strip()

    if title:
        with open("scientific_article.txt", "w", encoding="utf-8") as f:
            f.write(title)
        print("🔹 تم حفظ عنوان المقال الجديد بنجاح في ملف الخطة.")
    else:
        print("⚠️ لم تكتب عنواناً، سيتم استخدام آخر عنوان تم تسجيله.")

    # 3. التشغيل التلقائي والربط ببلوجر
    print("\n🚀 [الخطوة 3] جاري استدعاء الصور وصياغة المقال والنشر على بلوجر...")
    print("=" * 45 + "\n")

    try:
        subprocess.run(["python", "run_production.py"])
    except Exception as e:
        print(f"❌ حدث خطأ أثناء تشغيل السكريبت الرئيسي: {e}")


if __name__ == "__main__":
    run_menu()
