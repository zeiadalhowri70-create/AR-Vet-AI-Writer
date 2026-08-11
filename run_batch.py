import subprocess

# قائمة الأمراض التي تريد إنتاج مقالات لها
diseases = [
    "مرض الجمبورو في الدواجن",
    "مرض إنفلونزا الطيور",
    "مرض الكوكسيديا",
    "التهاب الشعب الهوائية المعدي",
    "الأمن الحيوي في مزارع الدواجن",
]

for disease in diseases:
    print(f"🚀 جاري إنتاج ونشر مسودة: {disease}")
    subprocess.run(["python", "run_production.py", disease])
    print(f"✅ تم الانتهاء من: {disease}")

print("🎉 اكتملت عملية الإنتاج للدفعة الحالية.")
