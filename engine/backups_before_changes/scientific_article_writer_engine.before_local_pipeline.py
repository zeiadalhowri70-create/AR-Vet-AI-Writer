# -*- coding: utf-8 -*-
from providers.provider_manager import ProviderManager
from engine.scientific_prompt_engine import ScientificPromptEngine


class ScientificArticleWriterEngine:

    def __init__(self):
        self.provider = ProviderManager()
        self.prompt_engine = ScientificPromptEngine()

    def write(self, topic, context=None):
        # بناء بروتوكول توجيهي صارم جداً ينافس أعتى الموسوعات الطبية العالمية

        context_text = context if context else ""
        prompt = f"""
أنت بروفيسور وعالم فيروسات بيطري خبير ومستشار دولي في أمراض الدواجن والمواشي. اكتب مقالاً أكاديمياً موسعاً، عميقاً جداً، ومفصلاً بالكامل عن موضوع: ({topic}).

يجب أن يلتزم النص بالمعايير الصارمة التالية للتفوق على موسوعات مثل Merck Veterinary Manual و WOAH ولضمان التوافق المطلق مع تحديثات محرك بحث جوجل (EEAT) وجوجل أدسنس:

1. الدقة العلمية المطلقة:
- تأكد من المسبب بدقة (مثلاً: فيروس النيوكاسل هو RNA أحادي الخيط سالب الشحنة ينتمي لعائلة Paramyxoviridae، وليس DNA أبداً). أي خطأ علمي يعتبر كارثة.

2. الهيكلية والعمق المقالي (اكتب بغزارة وتفصيل شديد):
- مقدمة طبية وبائية: سياق المرض عالمياً وأهميته الاقتصادية والإنتاجية.
- المسبب المرضي والتصنيف (Etiology): العترات (Velogenic, Mesogenic, Lentogenic) والخصائص الفيزيائية.
- الوبائيات وطرق الانتقال (Epidemiology): الانتشار العفوي، الإفرازات، دور الطيور البرية، ومقاومة الفيروس في البيئة.
- الإمراضية والآفات التشريحية (Pathogenesis & Necropsy): التغيرات والنزوف في المعدة الغدية (Proventriculus)، غدد بيير، واللوزتين الأعوريتين (Cecal Tonsils) بالتفصيل.
- الأعراض الإكلينيكية (Clinical Signs): التمييز بين الشكل العصبي، التنفسي، والهضمي.
- التشخيص والتفريق الإكلينيكي والمختبري: (ELISA, PCR, HA/HI) والتشخيص التفريقي (Differential Diagnosis) مع إنفلونزا الطيور (AI)، والتهاب الحنجرة والرغامي المعدي (ILT).
- بروتوكولات الوقاية والأمن الحيوي (Biosecurity) والتحصين: اذكر استراتيجيات اللقاحات الحية والميتة (مثل عترات LaSota, Hitchner B1, Clone 30) والتوقيتات الحقلية الشائعة.

3. أسلوب صياغة النص (مهم جداً للـ SEO وأدسنس):
- اذكر المصطلحات العلمية الطبية باللغة الإنجليزية واللاتينية بين أقواس بجانب مرادفها العربي.
- تجنب تماماً التكرار السطحي، واكتب بنبرة جافة، أكاديمية، وتحليلية دقيقة.
- استخدم التنسيق المتقدم: عناوين واضحة باستخدام (##) للعناوين الرئيسية و (###) للعناوين الفرعية، وقوائم نقطية غنية بالمعلومات الدسمة.
- لا تنهي المقال بعبارات تلخيصية ركيكة أو عامة، بل اختمه بتوصيات حقلية صارمة للأطباء والمربين.
"""
        if context_text:
            prompt += f"""

السياق العلمي الإضافي المعتمد:
{context_text}
"""

        prompt = self.prompt_engine.build(prompt)
        response = self.provider.generate(prompt)

        return {"title": topic, "content": response, "section": "scientific_article"}

    def info(self):
        return {
            "engine": "Scientific Article Writer Engine",
            "version": "3.0 - High Definition Clinical Content",
            "type": "AI Powered",
        }
