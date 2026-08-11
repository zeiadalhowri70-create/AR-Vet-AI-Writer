import os
import requests
import sys


def check_groq():
    print("⏳ جاري فحص مفتاح Groq...")
    if not os.path.exists("groq_key.txt"):
        return "❌ ملف groq_key.txt غير موجود"

    with open("groq_key.txt", "r") as f:
        api_key = f.read().strip()

    url = "https://groq.com"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": "Hi"}],
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=7)
        if response.status_code == 200:
            return "✅ شغال 100% ويعمل بكفاءة فائقة!"
        elif response.status_code == 401:
            return "❌ المفتاح غير صحيح (Invalid API Key)"
        else:
            return f"❌ خطأ من السيرفر برقم: {response.status_code}"
    except Exception as e:
        return f"❌ فشل الاتصال بالسيرفر (قد يكون بسبب الشبكة): {e}"


def check_openrouter():
    print("⏳ جاري فحص مفتاح OpenRouter...")
    if not os.path.exists("openrouter_key.txt"):
        return "❌ ملف openrouter_key.txt غير موجود"

    with open("openrouter_key.txt", "r") as f:
        api_key = f.read().strip()

    url = "https://openrouter.ai"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": "openrouter/free",
        "messages": [{"role": "user", "content": "Hi"}],
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=7)
        if response.status_code == 200:
            return "✅ شغال 100% ويعمل بكفاءة!"
        elif response.status_code == 401:
            return "❌ المفتاح غير صحيح أو الحساب غير موجود"
        else:
            try:
                err_msg = response.json()["error"]["message"]
                return f"❌ السيرفر متصل ولكن يرفض الطلب: {err_msg}"
            except BaseException:
                return f"❌ حظر شبكي / السيرفر عاد بصفحة حجب فارغة (Status: {
                    response.status_code})"
    except Exception as e:
        return f"❌ فشل الاتصال تماماً بالسيرفر: {e}"


if __name__ == "__main__":
    print("=" * 45)
    print("🔍 فاحص المفاتيح التلقائي لمشروعك الذكي 🔍")
    print("=" * 45)

    groq_result = check_groq()
    print(f"نتـيجة Groq       -> {groq_result}\n")
    print("-" * 45)

    or_result = check_openrouter()
    print(f"نتـيجة OpenRouter -> {or_result}\n")
    print("=" * 45)
