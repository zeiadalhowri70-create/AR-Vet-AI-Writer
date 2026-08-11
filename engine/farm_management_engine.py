# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Farm Management Engine

Production Final v1.0.0
Encyclopedia Scientific Engine
"""

from providers.provider_manager import ProviderManager


class FarmManagementEngine:

    VERSION = "1.0.0"

    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic, context=None):

        prompt = f"""
أنت خبير في إدارة مزارع الدواجن والإنتاج الحيواني والطب الوقائي البيطري.

اكتب قسم إدارة المزرعة (Farm Management)
لموسوعة بيطرية عالمية عن:

{topic}

يجب أن يتضمن:

1- إدارة القطيع أثناء وجود المرض.
2- إجراءات تقليل انتشار العدوى داخل المزرعة.
3- إدارة الكثافة العددية ومساحات التربية.
4- إدارة التهوية ودرجة الحرارة والرطوبة.
5- إدارة العلف والمياه أثناء المرض.
6- تقليل عوامل الإجهاد (Stress Factors).
7- تنظيم حركة العمال والمعدات.
8- برامج المتابعة والمراقبة الصحية.
9- العلاقة بين الإدارة الجيدة وتقليل الخسائر.
10- أخطاء الإدارة التي تزيد شدة المرض.

استخدم المصطلحات العربية والإنجليزية بين الأقواس.
اكتب بأسلوب موسوعة طبية بيطرية احترافية.
اجعل المحتوى عملياً وعلمياً.
"""

        if context:
            prompt += f"""

السياق العلمي:
{context}
"""

        content = self.provider.generate(prompt)

        return {
            "section": "farm_management",
            "engine": "FarmManagementEngine",
            "version": self.VERSION,
            "content": content,
            "evidence_required": False,
            "validation_required": True,
        }

    def info(self):
        return {
            "engine": "Farm Management Engine",
            "version": self.VERSION,
            "type": "Encyclopedia Scientific Engine",
        }
