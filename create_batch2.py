from pathlib import Path
import json

base = Path("knowledge/import_queue_batch2")
base.mkdir(parents=True, exist_ok=True)

diseases = {
    "avian_metapneumovirus": (
        "الفيروس الميتابنوموي للطيور",
        "Avian Metapneumovirus",
        "Avian metapneumovirus",
    ),
    "inclusion_body_hepatitis": (
        "التهاب الكبد ذو الأجسام الاحتوائية في الدواجن",
        "Inclusion Body Hepatitis",
        "Fowl adenovirus",
    ),
    "avian_encephalomyelitis": (
        "التهاب الدماغ والنخاع الطيري",
        "Avian Encephalomyelitis",
        "Avian encephalomyelitis virus",
    ),
    "reovirus_infection": (
        "عدوى الريو فيروس في الدواجن",
        "Avian Reovirus Infection",
        "Avian reovirus",
    ),
    "runting_stunting_syndrome": (
        "متلازمة التقزم والتأخر في النمو",
        "Runting Stunting Syndrome",
        "Avian enteric viruses",
    ),
    "hydropericardium_hepatitis_syndrome": (
        "متلازمة التهاب الكبد والاستسقاء التاموري",
        "Hydropericardium Hepatitis Syndrome",
        "Fowl adenovirus",
    ),
    "spirochetosis": (
        "داء اللولبيات في الدواجن",
        "Avian Spirochetosis",
        "Brachyspira species",
    ),
    "erysipelas": ("الحمرة في الدواجن", "Erysipelas", "Erysipelothrix rhusiopathiae"),
    "botulism": (
        "التسمم الوشيقي في الدواجن",
        "Avian Botulism",
        "Clostridium botulinum toxin",
    ),
}

for disease, (ar, en, pathogen) in diseases.items():

    data = {
        "id": disease,
        "name_ar": ar,
        "name_en": en,
        "category": "poultry_diseases",
        "animal": "poultry",
        "scientific_profile": {
            "pathogen": {"name": pathogen},
            "clinical_signs": ["depression", "weight_loss", "mortality"],
            "diagnosis": {
                "field": ["clinical_signs", "flock_history"],
                "laboratory": ["pcr"],
                "advanced_tests": ["laboratory_confirmation"],
            },
            "treatment": {"specific": "", "supportive": ["vitamins", "electrolytes"]},
            "prevention": {
                "biosecurity": ["farm_disinfection", "movement_control"],
                "vaccination": [],
            },
        },
        "references": ["WOAH", "FAO"],
    }

    (base / f"{disease}.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )

print("BATCH2 FILES CREATED")
