import requests
import json

# ==========================================
# [إعدادات المفاتيح السرية]
# قم بوضع مفاتيحك الفعلية والكاملة بين علامات التنصيص أدناه
# ==========================================
GEMINI_API_KEY = "REMOVED_GEMINI_API_KEY"
UNSPLASH_ACCESS_KEY = "BiVvR99mTARhdPrVFnObWRhviJ0sH5B6WDsLlDgJmnc"
YOUTUBE_API_KEY = "REMOVED_GCP_KEY"


def get_medical_image(keyword):
    """جلب صورة تشريحية متوافقة مع السيو من Unsplash"""
    url = f"https://unsplash.com{keyword}&per_page=1&orientation=landscape"
    headers = {"Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get("results"):
                image_url = data["results"][0]["urls"]["regular"]
                alt_text = data["results"][0]["alt_description"] or keyword
                return f'<div style="text-align:center; margin:25px 0;"><img src="{image_url}" alt="{alt_text}" style="max-width:100%; height:auto; border-radius:12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);"><p style="font-size:12px; color:#7f8c8d; font-style:italic; margin-top:5px;">مصدر الصورة التشريحية: Unsplash</p></div>'
        return ""
    except BaseException:
        return ""


def get_youtube_video(keyword):
    """جلب فيديو طبي تعليمي متوافق مع الموبايل من YouTube"""
    url = f"https://googleapis.com{keyword}&type=video&videoEmbeddable=true&maxResults=1&key={YOUTUBE_API_KEY}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get("items"):
                video_id = data["items"][0]["id"]["videoId"]
                video_title = data["items"][0]["snippet"]["title"]
                return f'<div style="margin:35px 0; text-align:center;"><h3 style="color:#2c3e50; margin-bottom:15px; font-size:20px;">فيديو تعليمي وتوضيحي مكمل:</h3><div style="position:relative; padding-bottom:56.25%; height:0; overflow:hidden; max-width:100%; border-radius:12px; box-shadow:0 4px 15px rgba(0,0,0,0.15);"><iframe src="https://youtube.com{video_id}" style="position:absolute; top:0; left:0; width:100%; height:100%; border:0;" allowfullscreen></iframe></div></div>'
        return ""
    except BaseException:
        return ""


def call_gemini_ai(title):
    """الاتصال بـ Gemini لتوليد المقال الطبي والجداول بصيغة HTML نظيفة"""
    url = f"https://googleapis.com{GEMINI_API_KEY}"
    headers = {"Content-Type": "application/json"}

    prompt = f"""
    اكتب مقالاً علمياً طبياً استشارياً فائق الاحترافية ومبتكر حول موضوع ({title}) متوافق تماماً مع معايير Google E-E-A-T ومحركات البحث وقبول أدسنس.
    يجب تقسيم المقال بعناوين فرعية واضحة باستخدام وسوم HTML (مثل الأعراض، الأسباب، التشخيص، العلاج، الوقاية).
    ملاحظة إلزامية: قم بإنشاء جدول مقارنة أو جدول بيانات طبي واحد على الأقل داخل المقال باستخدام وسوم HTML النظيفة <table> مع تنسيق جذاب ومريح للعين (خلفية رمادية خفيفة لرأس الجدول وحدود رفيعة).
    تنبيه صارم: لا تضع أي رموز باك تيك (```) أو كلمة html في مخرجاتك نهائياً، أريد النص الطبي والجدول مصاغاً بـ HTML مباشرة وجاهزاً للنشر فوراً.
    """

    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        if response.status_code == 200:
            data = response.json()
            return data["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return f"<p>خطأ في استجابة الذكاء الاصطناعي: {response.text}</p>"
    except Exception as e:
        return f"<p>فشل الاتصال بمحرك التوليد: {e}</p>"


def generate_full_article(title):
    """تجميع المقال النهائي الشامل ودمج الصور والفيديوهات والتنويه الطبي"""
    print(f"\033[94m[+] جاري جلب الوسائط والمحتوى لموضوع: {title}...\033[0m")

    # 1. استدعاء المكونات المرئية
    image_html = get_medical_image(f"{title} anatomy medical")
    video_html = get_youtube_video(f"{title} شرح طبي دكتور")

    # 2. توليد المقال والجدول من الذكاء الاصطناعي
    ai_article_body = call_gemini_ai(title)

    # 3. إخلاء المسؤولية الطبي الإلزامي لأدسنس
    medical_disclaimer = """
    <div style="background-color:#fff5f5; border-right:6px solid #e53e3e; padding:15px; margin-top:40px; border-radius:6px; font-size:14px; color:#c53030; line-height:1.6; text-align:right;" dir="rtl">
        <strong>تنويه طبي هام ومسؤولية قانونية:</strong> المحتوى الوارد في هذا المقال مخصص للأغراض التثقيفية والإرشادية العامة فقط. لا يمكن بأي حال من الأحوال اعتبار هذه المعلومات بديلاً عن الاستشارة الطبية المتخصصة، أو التشخيص السريري، أو الخطة العلاجية المقرة من الطبيب المؤهل. يرجى دائماً مراجعة رائد الرعاية الصحية الخاص بك قبل اتخاذ أي قرارات طبية.
    </div>
    """

    # 4. بناء القالب المتكامل النهائي
    final_html_content = f"""
    <div dir="rtl" style="text-align: right; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.9; color: #2c3e50; padding:10px;">
        <h1>{title}</h1>
        {image_html}
        <div class="article-text-content" style="font-size:17px;">
            {ai_article_body}
        </div>
        {video_html}
        {medical_disclaimer}
    </div>
    """

    # 5. رفع المقال إلى بلوجر تلقائياً
    try:
        from uploader import upload_to_blogger  # أو اسم مكتبة الرفع لديك

        upload_to_blogger(title, final_html_content)
        print("[92m[✓] تم نشر المقال العلمي الشامل بنجاح كمُسودة على Blogger![0m")
    except Exception as e:
        # إذا كانت الدالة مدمجة في كلاس، يتم استدعاؤها عبر السكريبت الأساسي
        # لديك
        print(
            f"[93m[!] تم تجهيز المقال، يرجى تشغيل سكريبت الرفع المعتاد (مثل python main.py) لنشره.[0m"
        )

    # حفظ النتيجة في ملف محلي للمعاينة السريعة

    output_file = "tested_article.html"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(final_html_content)

    print(
        f"\033[92m[✓] نجح التوليد! تم حفظ المقال العلمي الشامل بالجداول والوسائط في ملف: {output_file}\033[0m"
    )
    print(
        "\033[93m[!] يمكنك الآن رفع متغير final_html_content إلى Blogger بأمان.\033[0m"
    )


if __name__ == "__main__":
    import sys

    topic = sys.argv[1] if len(sys.argv) > 1 else "التهاب المفاصل الروماتويدي"
    generate_full_article(topic)
