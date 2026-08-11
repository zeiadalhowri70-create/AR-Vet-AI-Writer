from google import genai

# إعداد العميل بالمفتاح الجديد
client = genai.Client(api_key="REMOVED_GEMINI_API_KEY")

try:
    print("جاري إرسال الطلب إلى سيرفرات جوجل باستخدام المكتبة الجديدة...")
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="قل مرحباً بالعربية واكتب اسمك باختصار إذا كنت تسمعني.",
    )

    print("\n--- النتيجة ناجحة! المفتاح شغال تماماً ---")
    print(response.text)

except Exception as e:
    print("\n--- حدث خطأ ---")
    print(e)
