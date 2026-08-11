import os
from providers.provider_priority_engine import ProviderPriorityEngine
from providers.provider_factory import ProviderFactory
import config
import time


class ContentRecoveryProvider:
    VERSION = "1.0.0"

    def generate(self, prompt):
        return {
            "content": (
                "هذا القسم العلمي يشرح الموضوع البيطري بشكل موسوعي "
                "اعتماداً على المعرفة العلمية المتاحة. "
                "يشمل التعريف، الأسباب، الأعراض، التشخيص، العلاج، "
                "والوقاية مع التركيز على التطبيق العملي في المزارع."
            )
        }


# -*- coding: utf-8 -*-


class ProviderManager:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ProviderManager, cls).__new__(cls)
        return cls._instance

    def __init__(self, provider_name=None):

        if getattr(self, "_initialized", False):
            return

        if not provider_name:
            provider_name = getattr(config, "ACTIVE_PROVIDER", None)

        if not provider_name:
            if os.getenv("OPENROUTER_API_KEY"):
                provider_name = "openrouter"
            elif os.getenv("GROQ_API_KEY"):
                provider_name = "groq"
            elif os.getenv("GEMINI_API_KEY"):
                provider_name = "gemini"
            else:
                provider_name = "mock"

        self.provider_name = provider_name
        self.provider = ProviderFactory.create(provider_name)

        self._cache = {}
        self._failed_providers = {}
        self._provider_cooldown = {}
        self._cooldown_seconds = 300

        self._initialized = True

    def get_provider(self):
        return self.provider

    def set_provider(self, provider_name):

        self.provider_name = provider_name
        self.provider = ProviderFactory.create(provider_name)

    def generate(self, prompt):

        cache_key = str(hash(prompt))

        if cache_key in self._cache:
            print("♻️ Provider cache hit")
            return self._cache[cache_key]

        priority = ProviderPriorityEngine()

        providers = [self.provider_name]

        providers.extend(priority.priorities())

        providers = list(dict.fromkeys(providers))

        # Production mode: disable mock provider
        providers = [p for p in providers if p != "mock"]

        for name in providers:
            if (
                name in self._provider_cooldown
                and time.time() < self._provider_cooldown[name]
            ):
                continue

            try:

                provider = ProviderFactory.create(name)

                result = provider.generate(prompt)

                if isinstance(result, dict):

                    if result.get("success"):

                        content = result.get("content", "")

                        self._cache[cache_key] = content

                        return content

                    error = str(result.get("content", ""))

                    print(f"⚠️ Provider failed: {name} -> {error[:200]}")

                    self._failed_providers[name] = {"error": error, "status": "failed"}

                    if "429" in error or "rate" in error.lower():
                        self._provider_cooldown[name] = (
                            time.time() + self._cooldown_seconds
                        )
                        continue

                elif result:

                    self._cache[cache_key] = result
                    return result

            except Exception as e:

                error = str(e)

                print(f"⚠️ Provider exception {name}: {error}")

                self._failed_providers[name] = {"error": error, "status": "exception"}

                if "429" in error or "rate" in error.lower():
                    self._provider_cooldown[name] = time.time() + self._cooldown_seconds

        fallback = (
            "تعذر إنشاء المحتوى بواسطة مزودي الذكاء الاصطناعي حالياً. "
            "يجب إعادة المحاولة بعد توفر المزود."
        )

        self._cache[cache_key] = fallback

        return fallback

    def health(self):

        return self.provider.health()

    def info(self):

        return {
            "manager": "Stable Provider Manager",
            "active_provider_name": self.provider.__class__.__name__,
            "failed_providers": self._failed_providers,
            "provider_details": (
                self.provider.info() if hasattr(self.provider, "info") else {}
            ),
        }
