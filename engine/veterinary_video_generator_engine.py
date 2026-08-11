# -*- coding: utf-8 -*-
import json


class VeterinaryVideoGeneratorEngine:
    """
    محرك توليد سيناريوهات الفيديو القصير (Shorts/Reels/TikTok) تلقائياً من المقالات الطبية.
    """

    def __init__(self):
        self.version = "2.0.0"
        self.status = "production"

    def generate_video_script(self, article_data):
        topic = article_data.get("title", "مرض بيطري")
        faq = article_data.get("faq_items", [])

        media = article_data.get("media_library", {})
        disease_profile = article_data.get("disease_profile", {})
        scientific_profile = disease_profile.get("scientific_profile", {})
        
        lesions = scientific_profile.get("lesions", [])
        clinical_signs = scientific_profile.get("clinical_signs", [])

        visual_assets = {
            "featured_image": media.get("featured_image", {}),
            "anatomical_images": media.get("anatomical_images", []),
            "histopathology": media.get("histopathology", []),
            "scientific_figures": media.get("scientific_figures", []),
            "diagrams": media.get("diagrams", []),
        }

        # استخلاص نقاط القوة لجعل السيناريو تفاعلياً ومثيراً للاهتمام في أول 3
        # ثوانٍ
        hook = (
            f"هل تعلم أن {topic} يمكن أن يدمر قطيع الدواجن بالكامل في أقل من 72 ساعة؟"
        )

        body_points = []

        if faq:
            for item in faq[:2]:
                body_points.append(
                    f"سؤال مهم: {item.get('question', '')} "
                    f"الجواب التشريحي: {item.get('answer', '')}"
                )

        if lesions:
            body_points.append(
                "الآفات التشريحية الرئيسية تشمل: "
                + ", ".join(lesions)
            )

        if clinical_signs:
            body_points.append(
                "العلامات السريرية المهمة تشمل: "
                + ", ".join(clinical_signs)
            )

        if not body_points:
            body_points.append(
                "يتميز هذا المرض بتغيرات مرضية تحتاج إلى التشخيص البيطري."
            )

        body_points.append(
            "الوقاية تعتمد على الأمن الحيوي والتحصين والإدارة الصحية للقطيع."
        )

        call_to_action = "للمزيد من التفاصيل الطبية وجدول التحصين الكامل، شرفنا بزيارة مدونة الدكتور زياد الحوري البيطرية!"

        script = {
            "visual_assets": visual_assets,
            "metadata": {
                "target_platforms": [
                    "YouTube Shorts",
                    "TikTok",
                    "Facebook Reels",
                    "Instagram Reels",
                ],
                "estimated_duration": "59s",
                "language": "ar",
            },
            "storyboard": [
                {
                    "scene": 1,
                    "duration": "5s",
                    "visual_prompt": f"لقطة ديناميكية مقربة لقطيع دجاج يبدو عليه الخمول، مع نص متحرك باللون الأحمر: خطورة {topic}!",
                    "audio_text": hook,
                },
                {
                    "scene": 2,
                    "duration": "25s",
                    "visual_prompt": "انتقال سريع لرسومات تشريحية مجهرية لغدد المعدة الغدية واللوزتين الأعوريتين توضح النزوف النقطية النموذجية.",
                    "audio_text": " ".join(body_points),
                },
                {
                    "scene": 3,
                    "duration": "20s",
                    "visual_prompt": "لقطة لطبيب بيطري يقوم بالإشراف على عملية تحصين حقلية باستخدام عترة لاصوتا وتطبيق إجراءات الأمن الحيوي.",
                    "audio_text": "التشخيص المبكر والسريع بالصفة التشريحية يعزل العدوى فوراً ويحمي بقية العنابر من النفوق المفاجئ.",
                },
                {
                    "scene": 4,
                    "duration": "9s",
                    "visual_prompt": "ظهور شعار 'موسوعة Arvetinfo للطب البيطري - الدكتور زياد الحوري' مع روابط منصات التواصل.",
                    "audio_text": call_to_action,
                },
            ],
        }
        return script

    def info(self):
        return {
            "engine": "Veterinary Video Generator Engine",
            "version": self.version,
            "status": self.status,
        }
