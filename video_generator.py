import os
import sys
from gtts import gTTS
from moviepy.video.VideoClip import ImageClip
from moviepy.audio.io.AudioFileClip import AudioFileClip


def create_video_from_text(text, output_video_path="output_video.mp4"):
    print("[*] جاري تحويل النص الطبي إلى صوت باللغة العربية...")

    # 1. توليد الصوت باللغة العربية
    tts = gTTS(text=text, lang="ar", slow=False)
    temp_audio = "temp_voice.mp3"
    tts.save(temp_audio)

    print("[*] جاري دمج الصوت مع الصورة وإنتاج الفيديو...")

    # 2. تحديد صورة ثابتة للفيديو من مجلد المشروع
    # نختبر وجود صورة داخل مجلد images أو نستخدم صورة افتراضية
    image_path = "./images/default.jpg"
    if not os.path.exists(image_path):
        # إذا لم يجد المجلد، سنبحث عن أي صورة في المجلد الرئيسي أو ننشئ مسار
        # افتراضي
        image_path = "temp_image.jpg"
        # أمر برمي لعمل صورة بسيطة في حال عدم وجود صور
        os.system("touch temp_image.jpg")

    try:
        # 3. إعداد مقطع الصوت والصورة وعمل المونتاج
        audio_clip = AudioFileClip(temp_audio)
        video_clip = ImageClip(image_path).with_duration(audio_clip.duration)
        video_clip = video_clip.with_audio(audio_clip)

        # 4. تصدير الفيديو النهائي بجودة مناسبة للهاتف وبسرعة
        video_clip.write_videofile(
            output_video_path, fps=24, codec="libx264", audio_codec="aac"
        )

        # إغلاق الملفات لتفريغ الذاكرة
        audio_clip.close()
        video_clip.close()

        # تنظيف الملفات المؤقتة
        if os.path.exists(temp_audio):
            os.remove(temp_audio)

        print(f"[✓] تم إنشاء الفيديو بنجاح وحفظه في: {output_video_path}")
        return True

    except Exception as e:
        print(f"[!] حدث خطأ أثناء معالجة الفيديو: {e}")
        return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[!] يرجى كتابة النص المراد تحويله بين علامتي تنصيص.")
    else:
        create_video_from_text(sys.argv[1])
