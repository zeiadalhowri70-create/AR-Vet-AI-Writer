from pathlib import Path
import json

file = Path("knowledge/disease_profiles/newcastle_disease.json")

data = json.loads(file.read_text(encoding="utf-8"))

sp = data["scientific_profile"]

sp["clinical_signs"] = [
    "respiratory_signs",
    "coughing",
    "sneezing",
    "nervous_signs",
    "green_diarrhea",
    "drop_in_egg_production",
    "high_mortality",
]

sp["lesions"] = ["hemorrhages", "intestinal_lesions", "tracheal_mucus", "organ_damage"]

sp["diagnosis"] = {
    "field": ["clinical_signs", "flock_history"],
    "laboratory": ["PCR", "virus_isolation"],
    "advanced_tests": ["sequencing", "pathogenicity_test"],
}

sp["differential_diagnosis"] = [
    "avian_influenza",
    "infectious_bronchitis",
    "infectious_laryngotracheitis",
]

sp["treatment"] = {
    "specific": "",
    "supportive": ["electrolytes", "vitamins", "secondary_infection_control"],
}

sp["prevention"] = {
    "biosecurity": ["farm_disinfection", "movement_control", "wild_bird_control"],
    "vaccination": ["live_newcastle_vaccine", "inactivated_newcastle_vaccine"],
}

data["ai_analysis"]["comparison_tags"] = [
    "respiratory_disease",
    "high_mortality",
    "viral_disease",
    "vaccination_control",
]

data["references"] = ["WOAH", "FAO"]

file.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

print("NEWCASTLE PROFILE UPDATED")
