# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Platform Runtime Manager

Canonical Production Runtime Composition Root
Stage C.4.5 Upgrade

Production Final
"""

from platform_core.ai.provider_manager import ProviderManager
from platform_core.ai.generation_service import AIGenerationService
from platform_core.ai.generation_integration import AIGenerationIntegration
from platform_core.ai.providers.groq_provider import GroqProvider
from platform_core.ai.providers.openrouter_provider import OpenRouterProvider
from platform_core.ai.providers.gemini_provider import GeminiProvider
from platform_core.runtime.article_generation_runtime import (
    ArticleGenerationRuntime,
)


from platform_core.services.writer import WriterService, WriterPipelineBridge
from engine.article_writer_integration_engine import ArticleWriterIntegrationEngine


class PlatformRuntimeManager:

    VERSION = "2.0.0"

    def __init__(
        self,
        integration_engine=None,
        service_registry=None,
    ):

        self.integration_engine = integration_engine

        # Production Writer Runtime Wiring
        self.article_writer_engine = ArticleWriterIntegrationEngine()
        self.writer_service = WriterService(
            writer_engine=self.article_writer_engine
        )
        self.writer_pipeline = WriterPipelineBridge(
            self.writer_service
        )
        self.service_registry = service_registry

        self.provider_manager = ProviderManager()
        self._initialize_providers()

        # Production Provider Registration
        self.provider_manager.register_provider(
            "groq",
            GroqProvider()
        )

        self.provider_manager.register_provider(
            "openrouter",
            OpenRouterProvider()
        )

        self.provider_manager.register_provider(
            "gemini",
            GeminiProvider()
        )

        # Provider Priority Selection
        self.provider_manager.set_active_provider("groq")


        self.generation_service = AIGenerationService(
            self.provider_manager
        )

        self.generation_integration = AIGenerationIntegration(
            self.generation_service
        )

        self.article_runtime = ArticleGenerationRuntime(
            self.generation_integration,
            writer_pipeline=self.writer_pipeline
        )

        self._register_runtime()


    def _register_runtime(self):

        if self.service_registry:

            try:
                self.service_registry.register(
                    self.article_runtime
                )
            except Exception:
                pass



    def _initialize_providers(self):

        providers = [
            ("groq", GroqProvider()),
            ("openrouter", OpenRouterProvider()),
            ("gemini", GeminiProvider()),
        ]

        for name, provider in providers:
            self.provider_manager.register_provider(
                name,
                provider
            )

        for name, provider in providers:
            health = provider.health()

            if health.get("api_key_available"):
                self.provider_manager.set_active_provider(name)
                return

        # fallback selection for internal pipeline tests
        if providers:
            self.provider_manager.set_active_provider(
                providers[0][0]
            )


    def get_runtime(self):

        return self.article_runtime


    def start(self):

        return self.article_runtime.start()


    def status(self):

        if self.integration_engine:
            return self.integration_engine.health()

        return {
            "status": False,
            "message": "Integration engine unavailable",
        }


    def info(self):

        return {
            "name": "PlatformRuntimeManager",
            "version": self.VERSION,
        }


    def health(self):

        return {

            "status": True,

            "manager":
                "PlatformRuntimeManager",

            "version":
                self.VERSION,

            "runtime":
                self.article_runtime.health(),

            "provider":
                self.provider_manager.health(),

            "generation_service":
                self.generation_service.health(),

            "generation_integration":
                self.generation_integration.health(),

        }
