import requests

API_KEY = "ضع_مفتاحك_هنا"
URL = "https://googleapis.com"

payload = {"contents": [{"parts": [{"text": "Hello"}]}]}
params = {"key": API_KEY}

try:
    response = requests.post(URL, params=params, json=payload)
    print("الكود نجح في الاتصال! الرد هو:")
    print(response.json())
except Exception as e:
    print("حدث خطأ:", e)
