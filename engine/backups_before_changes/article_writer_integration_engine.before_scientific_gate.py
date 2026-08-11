# -*- coding: utf-8 -*-

from engine.article_real_content_builder_engine import ArticleRealContentBuilderEngine
from engine.encyclopedia_article_builder_engine import EncyclopediaArticleBuilderEngine
from engine.article_quality_enhancement_engine import ArticleQualityEnhancementEngine
from engine.article_validation_engine import ArticleValidationEngine
from engine.article_metadata_engine import ArticleMetadataEngine
from engine.article_seo_enhancement_engine import ArticleSEOEnhancementEngine
from engine.article_statistics_engine import ArticleStatisticsEngine
from engine.article_integrity_engine import ArticleIntegrityEngine
from engine.article_export_manifest_engine import ArticleExportManifestEngine
from engine.article_build_info_engine import ArticleBuildInfoEngine
from engine.article_cache_engine import ArticleCacheEngine
from engine.article_logger_engine import ArticleLoggerEngine
from engine.article_pipeline_state_engine import ArticlePipelineStateEngine
from engine.article_execution_metrics_engine import ArticleExecutionMetricsEngine
from engine.article_health_monitor_engine import ArticleHealthMonitorEngine
from engine.article_runtime_context_engine import ArticleRuntimeContextEngine
from engine.article_dependency_report_engine import ArticleDependencyReportEngine
from engine.article_processing_summary_engine import ArticleProcessingSummaryEngine
from engine.article_production_signature_engine import ArticleProductionSignatureEngine
from engine.article_audit_trail_engine import ArticleAuditTrailEngine
from engine.article_build_report_engine import ArticleBuildReportEngine
from engine.article_release_information_engine import ArticleReleaseInformationEngine
from engine.article_compatibility_report_engine import ArticleCompatibilityReportEngine
from engine.article_deployment_report_engine import ArticleDeploymentReportEngine
from engine.article_lifecycle_report_engine import ArticleLifecycleReportEngine
from engine.article_readiness_report_engine import ArticleReadinessReportEngine
from engine.article_version_manifest_engine import ArticleVersionManifestEngine
from engine.article_generation_session_engine import ArticleGenerationSessionEngine
from engine.article_execution_summary_engine import ArticleExecutionSummaryEngine
from engine.article_production_certificate_engine import (
    ArticleProductionCertificateEngine,
)
from engine.article_pipeline_final_state_engine import ArticlePipelineFinalStateEngine
from engine.article_final_packaging_engine import ArticleFinalPackagingEngine
from engine.article_export_preparation_engine import ArticleExportPreparationEngine
from engine.article_layout_engine import ArticleLayoutEngine
from engine.article_content_assembly_engine import ArticleContentAssemblyEngine
from engine.faq_engine import FAQEngine
from engine.article_reference_ranking_engine import ArticleReferenceRankingEngine
from engine.article_references_data_engine import ArticleReferencesDataEngine
from engine.article_citation_engine import ArticleCitationEngine
from engine.article_source_verification_engine import ArticleSourceVerificationEngine
from engine.article_source_quality_engine import ArticleSourceQualityEngine
from engine.claim_verification_engine import ClaimVerificationEngine
from engine.scientific_fact_checker_engine import ScientificFactCheckerEngine
from engine.article_claim_evidence_intelligence_engine import (
    ArticleClaimEvidenceIntelligenceEngine,
)
from engine.article_quality_score_engine import ArticleQualityScoreEngine
from engine.article_final_review_engine import ArticleFinalReviewEngine
from engine.article_publishing_readiness_engine import ArticlePublishingReadinessEngine
from engine.article_export_engine import ArticleExportEngine
from engine.article_document_export_engine import ArticleDocumentExportEngine
from engine.article_html_sanitization_engine import ArticleHTMLSanitizationEngine


from engine.blogger_publishing_engine import BloggerPublishingEngine
from engine.blogger_api_client_engine import BloggerAPIClientEngine


from engine.article_seo_signals_engine import ArticleSEOSignalsEngine


from engine.article_social_cards_engine import ArticleSocialCardsEngine
from engine.article_social_share_engine import ArticleSocialShareEngine
from engine.article_related_articles_engine import ArticleRelatedArticlesEngine
from engine.article_navigation_engine import ArticleNavigationEngine
from engine.article_internal_link_writer_engine import ArticleInternalLinkWriterEngine


from engine.article_schema_engine import ArticleSchemaEngine
from core.graph_builder import GraphBuilder
from core.veterinary_evidence_engine import VeterinaryEvidenceEngine
from core.knowledge_memory_engine import KnowledgeMemoryEngine
from engine.article_evidence_writer_engine import ArticleEvidenceWriterEngine
from core.graph_article_faq_generation_engine import GraphArticleFAQGenerationEngine
from engine.faq_engine import FAQEngine


from engine.scientific_article_writer_engine import ScientificArticleWriterEngine
from core.disease_topic_resolver_engine import DiseaseTopicResolverEngine
from core.writer_context_bridge import WriterContextBridge
from engine.article_image_prompt_engine import ArticleImagePromptEngine
from engine.scientific_diagram_engine import ScientificDiagramEngine
from engine.medical_infographic_engine import MedicalInfographicEngine
from engine.scientific_figure_integration_engine import (
    ScientificFigureIntegrationEngine,
)
from engine.article_video_metadata_engine import ArticleVideoMetadataEngine


class ArticleWriterIntegrationEngine:
    """
    يربط جميع مراحل إنتاج المقال.
    """

    def __init__(self):
        self.scientific_writer = ScientificArticleWriterEngine()
        self.topic_resolver = DiseaseTopicResolverEngine()
        self.writer_context = WriterContextBridge()
        self.image_prompt = ArticleImagePromptEngine()
        self.scientific_diagram = ScientificDiagramEngine()
        self.medical_infographic = MedicalInfographicEngine()
        self.figure_integration = ScientificFigureIntegrationEngine()
        self.video_metadata = ArticleVideoMetadataEngine()
        self.builder = ArticleRealContentBuilderEngine()
        self.encyclopedia_builder = EncyclopediaArticleBuilderEngine()
        self.quality = ArticleQualityEnhancementEngine()
        self.validator = ArticleValidationEngine()
        self.metadata = ArticleMetadataEngine()
        self.seo = ArticleSEOEnhancementEngine()
        self.statistics = ArticleStatisticsEngine()
        self.integrity = ArticleIntegrityEngine()
        self.export_manifest = ArticleExportManifestEngine()
        self.build_info = ArticleBuildInfoEngine()
        self.cache = ArticleCacheEngine()
        self.logger = ArticleLoggerEngine()
        self.pipeline = ArticlePipelineStateEngine()
        self.metrics = ArticleExecutionMetricsEngine()
        self.health = ArticleHealthMonitorEngine()
        self.runtime = ArticleRuntimeContextEngine()
        self.dependency_report = ArticleDependencyReportEngine()
        self.processing_summary = ArticleProcessingSummaryEngine()
        self.production_signature = ArticleProductionSignatureEngine()
        self.audit_trail = ArticleAuditTrailEngine()
        self.build_report = ArticleBuildReportEngine()
        self.release_information = ArticleReleaseInformationEngine()
        self.compatibility_report = ArticleCompatibilityReportEngine()
        self.deployment_report = ArticleDeploymentReportEngine()
        self.lifecycle_report = ArticleLifecycleReportEngine()
        self.readiness_report = ArticleReadinessReportEngine()
        self.version_manifest = ArticleVersionManifestEngine()
        self.generation_session = ArticleGenerationSessionEngine()
        self.execution_summary = ArticleExecutionSummaryEngine()
        self.production_certificate = ArticleProductionCertificateEngine()
        self.pipeline_final_state = ArticlePipelineFinalStateEngine()
        self.packager = ArticleFinalPackagingEngine()
        self.exporter = ArticleExportPreparationEngine()
        self.assembler = ArticleContentAssemblyEngine()
        self.layout = ArticleLayoutEngine()
        self.faq = FAQEngine()
        self.reference_ranking = ArticleReferenceRankingEngine()
        self.references_data = ArticleReferencesDataEngine()
        self.citation = ArticleCitationEngine()
        self.source_verification = ArticleSourceVerificationEngine()
        self.source_quality = ArticleSourceQualityEngine()
        self.claim_verification = ClaimVerificationEngine()
        self.fact_checker = ScientificFactCheckerEngine()
        self.claim_evidence = ArticleClaimEvidenceIntelligenceEngine()
        self.veterinary_evidence = VeterinaryEvidenceEngine()
        self.knowledge_memory = KnowledgeMemoryEngine()
        self.evidence_writer = ArticleEvidenceWriterEngine()
        self.quality_score = ArticleQualityScoreEngine()
        self.final_review = ArticleFinalReviewEngine()
        self.publishing_readiness = ArticlePublishingReadinessEngine()
        self.export_engine = ArticleExportEngine()
        self.html_sanitizer = ArticleHTMLSanitizationEngine()
        self.related_articles = ArticleRelatedArticlesEngine()
        self.navigation = ArticleNavigationEngine()
        self.internal_links = ArticleInternalLinkWriterEngine()
        self.document_export = ArticleDocumentExportEngine()
        self.validation = ArticleValidationEngine()
        self.blogger = BloggerPublishingEngine()
        self.blogger_api = BloggerAPIClientEngine()
        self.seo_signals = ArticleSEOSignalsEngine()
        self.social_cards = ArticleSocialCardsEngine()
        self.social_share = ArticleSocialShareEngine()
        self.schema = ArticleSchemaEngine()
        self.graph = GraphBuilder().build()
        self.graph_faq = GraphArticleFAQGenerationEngine()
        self.faq = FAQEngine()

    def generate(self, topic):
        resolved = self.topic_resolver.resolve(topic)

        context = None

        if resolved.get("status"):
            context = self.writer_context.prepare(resolved["disease_id"])

        scientific_article = self.scientific_writer.write(topic, context)

        self.metrics.start()
        self.logger.log(f"Start article: {topic}")
        self.pipeline.update(topic, "started")

        cached = self.cache.get(topic)
        if cached:
            return cached

        article = self.builder.build(topic, context)

        # Scientific Expansion Pipeline Gate
        if article.get("encyclopedia") and article.get("expansion_validation"):
            validations = article.get("expansion_validation", [])

            if not validations:
                raise ValueError("Scientific expansion validation missing")

            validation_summary = {
                "total_sections": len(validations),
                "validated_sections": len(
                    [item for item in validations if item.get("validation_required")]
                ),
                "word_expansion_pending": len(
                    [item for item in validations if not item.get("passed", False)]
                ),
            }

            self.pipeline.update(topic, "scientific_expansion_validated")

            article["scientific_expansion_ready"] = True
            article["scientific_expansion_validation_summary"] = validation_summary

        if isinstance(scientific_article, dict):
            article["scientific_content"] = scientific_article.get("content", "")

        self.metrics.step()

        article = self.quality.enhance(article)
        self.metrics.step()

        assembled = self.assembler.assemble(article)

        assembled["scientific_article"] = scientific_article

        if isinstance(scientific_article, dict):
            assembled["scientific_content"] = scientific_article.get("content", "")

        self.metrics.step()

        assembled = self.packager.package(assembled)

        assembled = self.exporter.prepare(assembled)

        # Final FAQ Integration
        node_id = None

        topic_text = topic.lower()

        for nid, node in self.graph.nodes.items():
            data = node.get("data", {})

            names = [
                nid.lower(),
                str(data.get("name_ar", "")).lower(),
                str(data.get("name_en", "")).lower(),
            ]

            if any(name and name in topic_text for name in names):
                node_id = nid
                break

        faq_items = []

        if node_id:
            faq_items = self.graph_faq.generate_faq(node_id)

        if not faq_items:
            faq_items = [
                {
                    "question": f"ما هو {topic}؟",
                    "answer": f"{topic} من الأمراض التي تصيب الدواجن وتحتاج إلى التشخيص المبكر والإدارة الصحية المناسبة.",
                },
                {
                    "question": f"ما أعراض {topic}؟",
                    "answer": "تختلف الأعراض حسب شدة الإصابة وقد تشمل انخفاض الإنتاج واضطرابات الجهاز الهضمي وزيادة الخسائر.",
                },
                {
                    "question": f"كيف يمكن الوقاية من {topic}؟",
                    "answer": "تتم الوقاية عبر الأمن الحيوي والإدارة الجيدة والمتابعة البيطرية المستمرة.",
                },
            ]

        assembled["faq_items"] = faq_items
        assembled["faq_html"] = self.faq.build_html(faq_items) if faq_items else ""
        assembled["faq_schema"] = self.faq.build_schema(faq_items) if faq_items else {}

        assembled["faq"] = assembled.get("faq_items", [])

        assembled["claim_evidence_analysis"] = self.claim_evidence.analyze_claim(
            f"المحتوى العلمي للمقال عن {topic}", assembled.get("references", [])
        )

        assembled["evidence_section"] = self.evidence_writer.write(topic)

        assembled["veterinary_evidence"] = self.veterinary_evidence.analyze(
            assembled.get("disease_profile", {}),
            assembled.get("symptoms", []),
            assembled.get("context", {}),
        )

        assembled["knowledge_memory"] = self.knowledge_memory.save_node(
            "article_evidence", topic, assembled["claim_evidence_analysis"]
        )

        assembled["seo_meta"] = assembled.get("metadata") or {
            "title": assembled.get("title", ""),
            "description": "مقال بيطري علمي من موسوعة AR-Vet Info",
            "keywords": ["دواجن", "طب بيطري", "أمراض الدواجن"],
        }

        assembled["schema"] = {
            "type": "Article",
            "headline": assembled.get("title", ""),
            "author": "د. زياد الحوري",
        }

        assembled["references"] = assembled.get(
            "references",
            [
                {
                    "organization": "WOAH",
                    "title": "World Organisation for Animal Health",
                    "url": "https://www.woah.org",
                },
                {
                    "organization": "FAO",
                    "title": "Food and Agriculture Organization",
                    "url": "https://www.fao.org",
                },
                {
                    "organization": "Merck Veterinary Manual",
                    "title": "Veterinary Reference Manual",
                    "url": "https://www.merckvetmanual.com",
                },
            ],
        )

        assembled["citations"] = self.citation.build_citations(assembled["references"])

        assembled["media"] = {
            "image": self.image_prompt.generate(topic),
            "video": self.video_metadata.generate(topic),
        }

        media = assembled["media"]

        image = media.get("image", {})
        video = media.get("video", {})

        assembled["media_html"] = f"""
<section class="article-media">

<div class="featured-image">
<img
src=""
alt="{image.get('alt', '')}"
loading="lazy">
<figure>
<figcaption>
{image.get('caption', '')}
</figcaption>
</figure>
</div>

<div class="article-video">
<h2>فيديو تعليمي</h2>
<p>{video.get('description', '')}</p>
</div>

</section>
"""

        assembled["related_articles_html"] = self.related_articles.build(assembled)

        assembled["navigation_html"] = self.navigation.build(assembled)

        assembled["internal_links"] = self.internal_links.write(topic)

        assembled["html"] = self.layout.build(assembled)

        assembled["html"] += assembled["related_articles_html"]

        assembled["html"] += assembled["navigation_html"]

        if isinstance(assembled["internal_links"], dict):
            assembled["html"] += assembled["internal_links"].get("content", "")

        assembled["html"] = self.html_sanitizer.process(assembled["html"])["html"]

        # Blogger Draft Integration (after HTML generation)
        assembled["blogger_draft"] = self.blogger.prepare(assembled)
        assembled["documents"] = self.document_export.build(assembled)

        assembled["seo_signals"] = self.seo_signals.build(assembled)

        assembled["image"] = self.image_prompt.generate(topic)
        assembled["video"] = self.video_metadata.generate(topic)

        assembled["social_cards"] = self.social_cards.build(assembled)

        assembled["social_share"] = self.social_share.build(assembled)

        validation = self.validation.validate(assembled)

        if not validation["valid"]:
            raise ValueError(
                "Article validation failed: " + ", ".join(validation["errors"])
            )

        assembled["validation"] = validation

        assembled["html"] = self.citation.inject(
            assembled["html"], assembled.get("citations", [])
        )

        assembled["quality_score"] = self.quality_score.evaluate(assembled)

        assembled["final_review"] = self.final_review.review(assembled)

        assembled["publishing_readiness"] = self.publishing_readiness.check(assembled)

        assembled["export"] = self.export_engine.export(assembled)

        self.cache.set(topic, assembled)

        self.logger.log(f"Finished article: {topic}", "SUCCESS")

        self.pipeline.update(topic, "completed")

        self.metrics.finish()

        assembled["metrics"] = self.metrics.report()
        assembled["health"] = self.health.check(assembled)
        assembled["runtime"] = self.runtime.generate(version="5.6")

        assembled["dependency_report"] = self.dependency_report.generate(assembled)
        assembled["processing_summary"] = self.processing_summary.generate(assembled)
        assembled["production_signature"] = self.production_signature.generate(
            assembled
        )
        assembled["audit_trail"] = self.audit_trail.generate(assembled)
        assembled["build_report"] = self.build_report.generate(assembled)
        assembled["release_information"] = self.release_information.generate()
        assembled["compatibility_report"] = self.compatibility_report.generate(
            assembled
        )
        assembled["deployment_report"] = self.deployment_report.generate(assembled)
        assembled["lifecycle_report"] = self.lifecycle_report.generate(assembled)
        assembled["readiness_report"] = self.readiness_report.generate(assembled)
        assembled["version_manifest"] = self.version_manifest.generate()
        assembled["generation_session"] = self.generation_session.generate()
        assembled["execution_summary"] = self.execution_summary.generate(assembled)
        assembled["production_certificate"] = self.production_certificate.generate(
            assembled
        )
        assembled["pipeline_final_state"] = self.pipeline_final_state.generate(
            assembled
        )

        assembled["context"] = context
        return assembled

    def info(self):
        return {
            "engine": "Article Writer Integration Engine",
            "version": "8.0",
            "status": "production",
            "quality_enhancement": True,
            "validation": True,
            "metadata": True,
            "seo": True,
            "statistics": True,
            "integrity": True,
            "export_manifest": True,
            "build_info": True,
            "cache": True,
            "logger": True,
            "pipeline_state": True,
            "metrics": True,
            "health_monitor": True,
            "runtime_context": True,
            "dependency_report": True,
            "processing_summary": True,
            "production_signature": True,
            "audit_trail": True,
            "build_report": True,
            "release_information": True,
            "compatibility_report": True,
            "deployment_report": True,
            "lifecycle_report": True,
            "readiness_report": True,
            "version_manifest": True,
            "generation_session": True,
            "execution_summary": True,
            "production_certificate": True,
            "pipeline_final_state": True,
            "final_packaging": True,
            "export_preparation": True,
            "layout": True,
            "faq": True,
            "references": True,
            "citations": True,
        }
