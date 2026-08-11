import json
import importlib
from pathlib import Path


CHAIN = {
    "bootstrap": "platform_core.integration.platform_bootstrap.PlatformBootstrap",
    "runtime": "platform_core.runtime.article_generation_runtime.ArticleGenerationRuntime",
    "provider": "platform_core.ai.provider_manager.ProviderManager",
    "registry": "platform_core.services.registry.service_registry_engine.ServiceRegistryEngine",
    "graph": "core.graph_builder.GraphBuilder",
    "brain": "core.veterinary_brain_integration_engine.VeterinaryBrainIntegrationEngine",
    "publishing": "platform_core.services.publishing.publishing_service.PublishingService",
}


report = {}

for name, target in CHAIN.items():

    module_name, class_name = target.rsplit(".", 1)

    item = {
        "target": target,
        "importable": False,
        "class_exists": False,
        "status": "UNKNOWN"
    }

    try:
        module = importlib.import_module(module_name)
        item["importable"] = True

        if hasattr(module, class_name):
            item["class_exists"] = True
            item["status"] = "AVAILABLE"
        else:
            item["status"] = "MISSING_CLASS"

    except Exception as e:
        item["status"] = "IMPORT_ERROR"
        item["error"] = str(e)

    report[name] = item


output = Path("AR_VET_PRODUCTION_RUNTIME_CHAIN_AUDIT.json")

output.write_text(
    json.dumps(
        report,
        indent=2,
        ensure_ascii=False
    ),
    encoding="utf-8"
)


print("PRODUCTION RUNTIME CHAIN AUDIT COMPLETE")
print("REPORT: AR_VET_PRODUCTION_RUNTIME_CHAIN_AUDIT.json")
