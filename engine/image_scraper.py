# -*- coding: utf-8 -*-
import os
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import urllib.parse  # مكتبة هامة جداً لتهيئة نصوص البحث بشكل آمن


class ImageScraper:
    def __init__(self):
        self.output_dir = (
            "/data/data/com.termux/files/home/AR-Vet-AI-Writer/output/images"
        )
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def download_disease_images(self, disease_name: str, limit: int = 3):
        # التحقق من أن الاسم ليس كود موقع تالف
        if (
            "html" in disease_name
            or "chunks" in disease_name
            or len(disease_name) > 100
        ):
            print(
                "تنبيه: نص البحث المستلم طويل جداً أو تالف، سيتم تخطي سحب الصور لتفادي الانهيار."
            )
            return []

        print(f"جاري البحث عن صور تشريح لمرض: {disease_name}...")

        # 1. صياغة الاستعلام وتهيئته آمنياً للإنترنت لعدم حدوث خطأ 404
        search_query = f"{disease_name} chicken lesions"
        encoded_query = urllib.parse.quote_plus(search_query)

        # 2. تصحيح رابط البحث الرسمي لـ Bing وعلامة الاستفهام المفقودة
        url = f"https://www.bing.com/images/search?q={encoded_query}"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36"
        }

        try:
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code != 200:
                print(f"خطأ في الاتصال بموقع البحث: {response.status_code}")
                return []

            soup = BeautifulSoup(response.text, "html.parser")

            # 3. تحديث الوسوم البرمجية لجلب روابط الصور المصغرة الحقيقية من
            # Bing
            image_elements = soup.find_all("img", class_="iusc") or soup.find_all(
                "a", class_="iusc"
            )

            downloaded_paths = []
            count = 0

            # استخراج الروابط الذكي من محاذاة الصور المحدثة
            for el in soup.find_all("img"):
                if count >= limit:
                    break

                # جلب الرابط الأساسي للصورة
                img_url = el.get("src") or el.get("data-src")

                # تصفية وتخطي الصور التعبيرية الصغيرة أو الأيقونات لضمان جودة
                # الصور الطبية
                if img_url and img_url.startswith("http") and "bing.com" not in img_url:
                    try:
                        img_res = requests.get(img_url, timeout=3)
                        image = Image.open(BytesIO(img_res.content))
                        image = image.resize((1080, 1080))

                        # حفظ الصور داخل المجلد المخصص بأمان في Termux
                        path = os.path.join(self.output_dir, f"img_{count}.jpg")
                        image.save(path)
                        downloaded_paths.append(path)
                        count += 1
                        print(f"✅ تم تحميل الصورة بنجاح: img_{count}.jpg")
                    except Exception:
                        continue

            return downloaded_paths

        except Exception as e:
            print(f"فشل سحب الصور: {e}")
            return []
