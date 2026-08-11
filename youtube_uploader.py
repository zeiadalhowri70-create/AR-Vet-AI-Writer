import os
import sys
from simple_youtube_api.Channel import Channel
from simple_youtube_api.LocalVideo import LocalVideo
from google_auth_oauthlib.flow import InstalledAppFlow


def get_authenticated_channel():
    # استخدام ملف credentials.json الخاص بك
    flow = InstalledAppFlow.from_client_secrets_file(
        "credentials.json", scopes=["https://googleapis.com"]
    )
    # إجبار نظام جوجل على توليد كود التحقق النصي الصريح المناسب للهواتف
    flow.redirect_uri = "http://localhost:8080/"
    auth_url, _ = flow.authorization_url(prompt="consent")

    print("\n" + "=" * 60)
    print("[*] من فضلك انسخ هذا الرابط وافتحه في متصفح هاتفك:\n")
    print(auth_url)
    print("=" * 60 + "\n")

    print(
        "[💡 تعليمات]: بعد قبول الصلاحيات في المتصفح، سيفشل المتصفح في فتح الصفحة وتتحول شريط العناوين إلى رابط يبدأ بـ http://localhost:8080/?code=..."
    )
    print(
        "[💡 المطلوب]: قم بنسخ هذا الرابط بالكامل من شريط عنوان المتصفح والصفه بالأسفل هنا.\n"
    )

    response_url = input("[?] الصق الرابط الكامل المنسوخ من المتصفح هنا: ").strip()

    flow.fetch_token(authorization_response=response_url)
    channel = Channel()
    channel.credentials = flow.credentials
    return channel


def upload_video(channel, video_file):
    try:
        print("[*] جاري رفع الفيديو وتجهيزه...")
        video = LocalVideo(file_path=video_file)
        video.set_title("فيديو تجريبي من البوت")
        video.set_description("تم الرفع تلقائياً بواسطة بايثون على Termux")
        video.set_category("Entertainment")
        video.set_privacy_status("private")  # خاص للاختبار

        uploaded_video = channel.upload_video(video)
        print(f"\n[✓] تم الرفع بنجاح! معرف الفيديو هو: {uploaded_video.id}")
    except Exception as e:
        print(f"[!] حدث خطأ أثناء الرفع: {e}")


if __name__ == "__main__":
    video_to_upload = sys.argv[1] if len(sys.argv) > 1 else "output_video.mp4"

    if not os.path.exists(video_to_upload):
        print(f"[!] ملف الفيديو {video_to_upload} غير موجود!")
        sys.exit(1)

    channel = get_authenticated_channel()
    upload_video(channel, video_to_upload)
