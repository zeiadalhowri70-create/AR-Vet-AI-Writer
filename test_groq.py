import os
from groq import Groq

if not os.path.exists("groq_key.txt"):
    print("خطأ: لم يتم العثور على ملف groq_key.txt")
    exit()

with open("groq_key.txt", "r") as f:
    api_key = f.read().strip()

try:
    # تشغيل الاتصال عبر المكتبة الرسمية مباشرة
    client = Groq(api_key=api_key)

    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": "Hello! clear test response please."}],
    )

    print("✅ نجح الاتصال بنجاح مبهر!")
    print("الرد النصي للذكاء الاصطناعي:")
    print(completion.choices[0].message.content)

except Exception as e:
    print("❌ حدث خطأ أثناء معالجة الطلب:")
    print(e)
