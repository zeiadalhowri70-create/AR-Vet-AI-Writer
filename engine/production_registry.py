# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Production Engine Registry

Central list of engines used in the production pipeline.
"""

PRODUCTION_ENGINES = [
    # AI Writing Layer
    "scientific_article_writer_engine",
    "scientific_prompt_engine",
    # Scientific Content Layer
    "article_real_content_builder_engine",
    "article_content_assembly_engine",
    # Quality Layer
    "article_quality_enhancement_engine",
    "article_quality_score_engine",
    "article_final_review_engine",
    # SEO Layer
    "article_seo_enhancement_engine",
    "article_seo_signals_engine",
    "article_seo_meta_engine",
    # Structure Layer
    "article_layout_engine",
    "article_schema_engine",
    "article_toc_engine",
    # References Layer
    "article_references_data_engine",
    "article_source_verification_engine",
    "article_source_quality_engine",
    "article_reference_ranking_engine",
    "article_citation_engine",
    # Export Layer
    "article_export_package_engine",
    "article_final_packaging_engine",
    "article_document_export_engine",
    "article_export_engine",
    # Publishing Layer
    "blogger_publishing_engine",
    # Media Layer
    "article_image_prompt_engine",
    "article_video_metadata_engine",
]


def get_production_engines():
    return PRODUCTION_ENGINES.copy()


def count():
    return len(PRODUCTION_ENGINES)


def info():
    return {
        "name": "AR-Vet Production Registry",
        "version": "1.0",
        "engines": len(PRODUCTION_ENGINES),
    }
