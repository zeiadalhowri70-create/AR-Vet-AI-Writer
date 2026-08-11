from pathlib import Path

target = Path("engine/symptoms_writer_engine.py")
backup = Path("backups/symptoms_writer_engine_before_C34_2.py")

backup.parent.mkdir(exist_ok=True)
backup.write_text(target.read_text(encoding="utf-8"), encoding="utf-8")

txt = target.read_text(encoding="utf-8")

txt = txt.replace(
    "def write(self, topic):",
    "def write(self, topic, context=None):"
)

txt = txt.replace(
    'اكتب قسم "الأعراض والعلامات السريرية" للمرض التالي:',
    '''اكتب قسم "الأعراض والعلامات السريرية" للمرض التالي:

المعلومات العلمية المساعدة من نظام AR-Vet AI:
{brain_context}

'''
)

txt = txt.replace(
    '        return self.provider.generate(prompt)',
    '''        if context:
            brain = context.get("veterinary_brain", {})
            knowledge = context.get("knowledge", {})
            brain_context = f"{brain}\\n{knowledge}"
        else:
            brain_context = "لا توجد بيانات إضافية."

        prompt = prompt.format(brain_context=brain_context)

        return self.provider.generate(prompt)'''
)

target.write_text(txt, encoding="utf-8")

print("C34.2 SYMPTOMS WRITER CONTEXT PATCH CREATED")
