import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("OPENROUTER_API_KEY")
if key:
    print(f"تم العثور على المفتاح بنجاح: {key[:5]}*******")
else:
    print("خطأ: لم يتم العثور على المفتاح في ملف .env")
