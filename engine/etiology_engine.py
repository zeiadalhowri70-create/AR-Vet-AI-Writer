# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Etiology Engine

Production Final v1.0.0
Encyclopedia Scientific Engine
"""

from providers.provider_manager import ProviderManager


class EtiologyEngine:

    VERSION = "1.0.0"

    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic, context=None):

        prompt = f"""
أنت أستاذ متخصص في الأمراض البيطرية وعلم المسببات المرضية.

اكتب قسم المسبب المرضي (Etiology)
لموسوعة بيطرية عالمية عن:

{topic}

يجب أن يتضمن القسم:

1- العامل المسبب للمرض (Causative Agent).
2- طبيعة العامل الممرض (فيروس، بكتيريا، طفيلي، فطر أو غير ذلك).
3- الخصائص البيولوجية الأساسية للمسبب.
4- التركيب أو البنية العامة للعامل الممرض.
5- عوامل الضراوة (Virulence Factors).
6- قدرة العامل على البقاء والانتشار.
7- العلاقة بين المسبب والعائل.
8- الاختلافات بين السلالات (Strains) إن وجدت.
9- أهمية خصائص المسبب في التشخيص والوقاية والسيطرة.

استخدم المصطلحات العربية والإنجليزية بين الأقواس.
اكتب بأسلوب مرجع طبي بيطري عالمي.
تجنب الحشو والمعلومات غير المؤكدة.
"""

        if context:
            prompt += f"""

السياق العلمي:
{context}
"""

        content = self.provider.generate(prompt)

        return {
            "section": "etiology",
            "engine": "EtiologyEngine",
            "version": self.VERSION,
            "content": content,
            "evidence_required": True,
            "validation_required": True,
        }

    def info(self):
        return {
            "engine": "Etiology Engine",
            "version": self.VERSION,
            "type": "Encyclopedia Scientific Engine",
        }
