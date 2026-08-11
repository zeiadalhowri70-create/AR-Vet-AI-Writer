import os
import arabic_reshaper
from bidi.algorithm import get_display
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
from googleapiclient.discovery import build

SCOPES = ["https://googleapis.com"]


def fix_arabic(text):
    reshaped_text = arabic_reshaper.reshape(text)
    return get_display(reshaped_text)


class ArticleFullGenerationEngine:
    def __init__(self):
        # تم وضع رقم مدونتك هنا مباشرة ليكون جاهزاً
        self.blog_id = "8962115474116118357"

    def get_blogger_service(self):
        creds = None
        if os.path.exists("token.pickle"):
            with open("token.pickle", "rb") as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                if not os.path.exists("client_secret.json"):
                    print(
                        fix_arabic(
                            "❌ خطأ: ملف client_secret.json غير موجود بمجلد المشروع."
                        )
                    )
                    return None
                flow = InstalledAppFlow.from_client_secrets_file(
                    "client_secret.json", SCOPES
                )
                creds = flow.run_local_server(port=0)
            with open("token.pickle", "wb") as token:
                pickle.dump(creds, token)
        return build("blogger", "v3", credentials=creds)

    def generate(self, title):
        # صياغة محتوى المقال بتنسيق HTML متوافق مع بلوجر
        html_content = f"""
        <div dir="rtl" style="text-align: right; font-family: Arial, sans-serif; line-height: 1.8;">
            <p>تعتبر هذه الحالة من أهم التحديات التي تواجه قطاع إنتاج الثروة الحيوانية عالمياً. تؤثر بشكل مباشر على الكفاءة الإنتاجية للحيوان وتتسبب في خسائر اقتصادية فادحة.</p>
            <h3>1. المسببات المرضية والربط الوبائي (Etiology):</h3>
            <p>تنشأ الحالة نتيجة تداخل معقد بين مسببات بكتيرية، فيروسية، أو عوامل بيئية وإدارية داخل المزرعة.</p>
            <h3>2. الأعراض الإكلينيكية والتشخيص المخبري (Diagnosis):</h3>
            <p>تغيرات واضحة في العلامات الحيوية، خمول، وانخفاض الشهية. يعتمد الفحص الدقيق على الفحص الفيزيائي وعمل الفحوصات المخبرية اللازمة.</p>
            <h3>3. البروتوكول العلاجي المعتمد (Treatment):</h3>
            <p>استخدام مضادات ميكروبية واسعة الطيف بناءً على نتائج التحليل، مع تقديم مضادات الالتهاب والمحاليل الداعمة.</p>
            <h3>4. الإجراءات الوقائية والأمن الحيوي (Prevention):</h3>
            <p>تطبيق معايير الأمن الحيوي الصارمة، تطهير الحظائر دورياً، وعزل الحيوانات المصابة فوراً.</p>
        </div>
        """

        print(fix_arabic("[+] جاري الاتصال بـ Blogger API لرفع المسودة..."))
        try:
            service = self.get_blogger_service()
            if service:
                body = {"kind": "blogger#post", "title": title, "content": html_content}
                # تشغيل الإدخال كمسودة عن طريق إعطاء كائن isDraft القيمة True
                service.posts().insert(
                    blogId=self.blog_id, body=body, isDraft=True
                ).execute()
                print(
                    fix_arabic(
                        "🎉 تم رفع المقالة بنجاح كمسودة (Draft) في بلوجر! يمكنك مراجعتها الآن."
                    )
                )
        except Exception as e:
            print(fix_arabic(f"❌ حدث خطأ أثناء الرفع: {str(e)}"))
