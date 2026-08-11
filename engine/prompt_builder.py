# -*- coding: utf-8 -*-


class PromptBuilder:

    def __init__(self):
        pass

    def build(self, strategy, project, part, knowledge=None):

        disease = project.disease
        section = part.title

        prompt = f"""
أنت طبيب بيطري واستشاري متخصص في أمراض الدواجن.

اكتب قسمًا من مقال علمي باللغة العربية الفصحى فقط.

الموضوع:
{disease}

القسم المطلوب:
{section}

التعليمات:

- اكتب معلومات صحيحة علمياً.
- لا تستخدم أي لغة غير العربية.
- لا تستخدم رموزاً أو أكواداً أو Markdown.
- لا تكرر الجمل.
- لا تخترع معلومات.
- استخدم أسلوباً موسوعياً احترافياً.
- اجعل النص مناسباً للنشر في مدونة طبية بيطرية.
- لا تضف مقدمة أو خاتمة إذا لم تكن مطلوبة.
- أعد النص فقط بدون أي ملاحظات إضافية.
"""

        return prompt.strip()

    def info(self):

        return {"engine": "Prompt Builder", "version": "2.0", "status": "production"}
