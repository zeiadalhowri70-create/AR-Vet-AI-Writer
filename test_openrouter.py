import requests
import os

if not os.path.exists("openrouter_key.txt"):
    print("خطأ: لم يتم العثور على ملف openrouter_key.txt")
    exit()

with open("openrouter_key.txt", "r") as f:
    api_key = f.read().strip()

url = "https://openrouter.ai"
headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

# استخدام الموجه المجاني الشامل الذي يختار أفضل النماذج المجانية المتاحة فوراً
payload = {
    "model": "openrouter/free",
    "messages": [
        {
            "role": "user",
            "content": "Hello! confirm if the free router setup is active.",
        }
    ],
}

try:
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    if response.status_code == 200 and "choices" in data:
        print("✅ نجح اتصال الموجه المجاني لـ OpenRouter بنجاح تام!")
        print("\n🤖 رد الذكاء الاصطناعي:")
        print(data["choices"]["message"]["content"])
    else:
        print(f"❌ فشل الاتصال، رد السيرفر:")
        print(data)
except Exception as e:
    print("❌ حدث خطأ داخلي في الكود:", e)
