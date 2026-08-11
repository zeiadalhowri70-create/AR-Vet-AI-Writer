import os

def suggest_fix(engine_name):
    name = engine_name.lower()
    if "image" in name or "photo" in name or "figure" in name:
        return "engine/article_media_integration_engine.py", "يجب استدعاؤه ضمن خط إنتاج الوسائط لتوليد وتضمين الصور."
    elif "video" in name or "youtube" in name:
        return "engine/article_media_integration_engine.py", "يجب ربطه بمدير الوسائط لإضافة الفيديوهات للمقال."
    elif "seo" in name or "meta" in name or "schema" in name:
        return "engine/article_seo_integration_engine.py", "يجب إضافته إلى مصفوفة تحسين محركات البحث."
    elif "writer" in name or "generator" in name or "engine" in name:
        return "engine/encyclopedia_engine_registry.py", "يجب تسجيله في السجل العام لكي يتعرف عليه النظام."
    else:
        return "engine/article_writer_integration_engine.py", "يجب إضافته كخطوة تابعة في مفسر خط الإنتاج الرئيسي."

def audit_and_suggest():
    print("=" * 80)
    print(" تقرير الفحص الذكي وحلول ربط المحركات المعزولة (AR-Vet Auto-Fix Advisor)")
    print("=" * 80)
    
    engine_dir = "engine"
    if not os.path.exists(engine_dir):
        print("مجلد الـ engine غير موجود!")
        return

    py_files = [f[:-3] for f in os.listdir(engine_dir) if f.endswith(".py") and f != "__init__.py"]
    
    integration_file = os.path.join(engine_dir, "article_writer_integration_engine.py")
    with open(integration_file, "r", encoding="utf-8") as f:
        integration_content = f.read()

    registry_file = os.path.join(engine_dir, "encyclopedia_engine_registry.py")
    with open(registry_file, "r", encoding="utf-8") as f:
        registry_content = f.read()

    isolated_count = 0

    for eng in sorted(py_files):
        if eng in integration_content or eng in registry_content or "registry" in eng or "integration" in eng:
            continue
        
        isolated_count += 1
        target_file, recommendation = suggest_fix(eng)
        print(f"[معزول] المحرك: {eng}")
        print(f"   -> أين يربط؟: {target_file}")
        print(f"   -> الحل المقترح: {recommendation}")
        print("-" * 80)

    print(f"إجمالي المحركات التي تحتاج إلى توجيه وربط: {isolated_count}")

if __name__ == "__main__":
    audit_and_suggest()
