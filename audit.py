import importlib
import os


def audit_engine():
    engine_path = "engine"
    print(f"--- تقييم محركات النظام (Engine Audit) ---")

    for filename in os.listdir(engine_path):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]
            try:
                importlib.import_module(f"engine.{module_name}")
                print(f"[PASS] Engine {module_name} loaded.")
            except Exception as e:
                print(f"[FAIL] Engine {module_name} error: {e}")


if __name__ == "__main__":
    audit_engine()
