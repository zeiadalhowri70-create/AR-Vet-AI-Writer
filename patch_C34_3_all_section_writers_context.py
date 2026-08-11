from pathlib import Path
import shutil

writers = [
    "introduction_writer_engine.py",
    "definition_writer_engine.py",
    "diagnosis_writer_engine.py",
    "treatment_writer_engine.py",
    "prevention_writer_engine.py",
    "vaccine_writer_engine.py",
]

base = Path("engine")
backup_dir = Path("backups/C34_3_section_writers")
backup_dir.mkdir(parents=True, exist_ok=True)

changed = 0

for filename in writers:
    target = base / filename

    if not target.exists():
        print("MISSING:", target)
        continue

    backup = backup_dir / filename
    shutil.copy2(target, backup)

    txt = target.read_text(encoding="utf-8")

    original = txt

    # Add context argument
    txt = txt.replace(
        "def write(self, topic):",
        "def write(self, topic, context=None):"
    )

    # Inject scientific context placeholder after topic
    if "{brain_context}" not in txt:

        txt = txt.replace(
            "{topic}",
            "{topic}\n\nالمعلومات العلمية المساندة من نظام AR-Vet AI:\n{brain_context}",
            1
        )

    # Replace provider call safely
    if "prompt.format(brain_context=" not in txt:

        txt = txt.replace(
            "return self.provider.generate(prompt)",
            """
        if context:
            brain = context.get("veterinary_brain", {})
            knowledge = context.get("knowledge", {})
            profile = context.get("disease_profile", {})

            brain_context = (
                f"Veterinary Brain:\\n{brain}\\n"
                f"Knowledge:\\n{knowledge}\\n"
                f"Disease Profile:\\n{profile}"
            )
        else:
            brain_context = "لا توجد بيانات علمية إضافية."

        prompt = prompt.format(
            brain_context=brain_context
        )

        return self.provider.generate(prompt)
"""
        )

    if txt != original:
        target.write_text(txt, encoding="utf-8")
        changed += 1
        print("PATCHED:", filename)
    else:
        print("NO CHANGE:", filename)

print("C34.3 COMPLETED")
print("FILES CHANGED:", changed)
print("BACKUP:", backup_dir)
