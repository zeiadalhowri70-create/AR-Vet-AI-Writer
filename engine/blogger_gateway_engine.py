# -*- coding: utf-8 -*-

from engine.blogger_publishing_engine import BloggerPublishingEngine
from engine.blogger_validation_engine import BloggerValidationEngine
from engine.blogger_rollback_engine import BloggerRollbackEngine
from engine.blogger_publish_state_engine import BloggerPublishStateEngine
from engine.blogger_publish_audit_engine import BloggerPublishAuditEngine
from engine.blogger_duplicate_guard_engine import BloggerDuplicateGuardEngine
from engine.blogger_article_production_adapter import BloggerArticleProductionAdapter
from engine.blogger_persistent_storage_engine import BloggerPersistentStorageEngine
from engine.blogger_publish_queue_engine import BloggerPublishQueueEngine
from engine.blogger_retry_manager_engine import BloggerRetryManagerEngine
from engine.blogger_recovery_engine import BloggerRecoveryEngine
from engine.blogger_health_check_engine import BloggerHealthCheckEngine
from engine.blogger_oauth_safety_engine import BloggerOAuthSafetyEngine
from engine.blogger_workflow_controller_engine import BloggerWorkflowControllerEngine
from engine.blogger_release_gate_engine import BloggerReleaseGateEngine


class BloggerGatewayEngine:

    VERSION = "1.0"

    def __init__(self):

        self.publisher = BloggerPublishingEngine()
        self.validator = BloggerValidationEngine()
        self.rollback_engine = BloggerRollbackEngine()
        self.state_engine = BloggerPublishStateEngine()
        self.audit = BloggerPublishAuditEngine()
        self.duplicate_guard = BloggerDuplicateGuardEngine()
        self.production_adapter = BloggerArticleProductionAdapter()
        self.storage = BloggerPersistentStorageEngine()
        self.queue = BloggerPublishQueueEngine()
        self.retry_manager = BloggerRetryManagerEngine()
        self.recovery = BloggerRecoveryEngine()
        self.health = BloggerHealthCheckEngine()
        self.oauth = BloggerOAuthSafetyEngine()
        self.workflow = BloggerWorkflowControllerEngine()
        self.release_gate = BloggerReleaseGateEngine()

    def prepare(self, article):

        duplicate = self.duplicate_guard.check(article)

        if duplicate.get("duplicate"):
            return {
                "platform": "Blogger",
                "status": "duplicate_blocked",
                "duplicate": duplicate,
            }

        state = self.state_engine.create()

        production = self.production_adapter.process(article)

        if not production.get("valid", True):
            return {
                "platform": "Blogger",
                "status": "seo_blocked",
                "production_report": production,
            }

        article = production.get("article", article)

        validation = self.validator.validate(article)

        if not validation["valid"]:

            return {
                "platform": "Blogger",
                "status": "blocked",
                "validation": validation,
            }

        state = self.state_engine.transition(state, "VALIDATED")

        result = self.publisher.prepare(article)

        state = self.state_engine.transition(state, "DRAFT_CREATED")

        result["publish_state"] = state

        self.storage.add(result)

        result["queue"] = self.queue.enqueue(result)

        result["audit"] = self.audit.log("draft_created", result)

        result["production_report"] = production

        result["blogger_status"] = {
            "validated": True,
            "published": False,
            "draft_created": bool(result.get("api_draft")),
        }

        return result

    def health_check(self):

        health = self.health.check(self)

        oauth = self.oauth.check(self.publisher.api_client)

        return self.release_gate.evaluate(health, oauth)

    def rollback(self, draft):

        return self.rollback_engine.rollback(draft)

    def info(self):

        return {
            "engine": "Blogger Gateway Engine",
            "version": self.VERSION,
            "status": "production",
        }
