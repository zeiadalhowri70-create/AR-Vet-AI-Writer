# AR-Vet AI Writer — PROJECT LAW

**Status:** NON-NEGOTIABLE
**Authority:** Canonical project governance
**Scope:** Entire repository, runtime, production pipeline, tests, documentation, integrations, and release process.

## 1. Purpose

This document is the governing law of AR-Vet AI Writer. Its purpose is to prevent architectural drift, duplicate production paths, undocumented dependencies, unsafe cleanup, and provider-dependent production failure.

No implementation decision may override this document unless this document itself is formally amended through the controlled governance process.

## 2. Canonical Production Path

The project SHALL have exactly one canonical production path.

The target canonical flow is:

```text
TOPIC / DISEASE
  -> APPLICATION / RUNTIME ENTRY
  -> TOPIC RESOLUTION
  -> VETERINARY BRAIN + KNOWLEDGE GRAPH
  -> RESEARCH / EVIDENCE
  -> AI GENERATION RUNTIME
  -> SCIENTIFIC ARTICLE BUILDER
  -> ARABIC EDITORIAL / LANGUAGE LAYER
  -> ARTICLE ENRICHMENT
  -> MEDIA PIPELINE
  -> HTML PRODUCTION
  -> QUALITY + SCIENTIFIC VALIDATION + SAFETY
  -> PRODUCTION MANIFEST
  -> BLOGGER PRODUCTION / PUBLISHING
  -> POST-PUBLISH DISTRIBUTION
  -> ANALYTICS / MONITORING
```

This is an architectural target and becomes the only production path after each stage is verified against the repository's real implementation. Historical or experimental paths may exist temporarily, but they are not production paths and MUST be explicitly classified.

## 3. Approved Components Only

Only explicitly approved engines, files, modules, adapters, providers, contracts, commands, and workflows may participate in production.

The authoritative machine-readable registry is:

```text
.arvet/project_law.json
```

Until the registry is populated and verified by the architecture audit, production integration and release are BLOCKED. An existing file is not considered approved merely because it exists or previously worked.

## 4. Contract-First Rule

Production components MUST communicate through explicit, documented contracts. At minimum, the architecture SHALL converge on:

- TopicContract
- BrainKnowledgeContract
- EvidenceContract
- AIContentContract
- ScientificArticleContract
- EditorialContract
- MediaContract
- SEOContract
- HTMLContract
- PublishingContract
- ProductionManifest

A component that relies on undocumented dictionary keys, implicit object shapes, raw strings where a structured contract is required, or guessed downstream fields is non-compliant.

## 5. Knowledge and Writing Separation

Scientific knowledge is not an article.

The Veterinary Brain and Knowledge Graph SHALL produce structured knowledge. Evidence SHALL establish traceability. The scientific writer SHALL transform approved structured knowledge into article content. The Arabic editorial layer SHALL normalize terminology, language, readability, and final Arabic presentation.

No layer may silently replace another layer's responsibility.

## 6. AI Provider Independence

AI providers are optional execution dependencies, not the project's source of truth.

The project MUST retain a defined internal fallback path capable of continuing safe production when every external AI provider is unavailable, rate-limited, unauthorized, or otherwise failing.

Provider failure MUST NOT be interpreted as successful generation.

Provider failure MUST NOT silently produce fabricated scientific content.

The internal fallback SHALL be deterministic, bounded, auditable, and based on the project's verified internal knowledge/contracts/templates/rules. When the requested production quality cannot be safely achieved, the system SHALL produce a controlled degraded result or a clear blocked/revision state rather than falsely claiming success.

## 7. Single Responsibility and No Duplicate Production Ownership

Two production components MUST NOT independently own the same responsibility.

If duplicate engines exist, they SHALL be classified before any change:

- ACTIVE / CANONICAL
- ADAPTER
- LEGACY
- DUPLICATE
- EXPERIMENTAL
- UNUSED / UNREFERENCED

No duplicate may be promoted into production merely to fix an integration failure.

## 8. Cleanup and Removal Law

No file, engine, adapter, provider, test, workflow, or module may be deleted or moved out of the active tree until dependency verification proves that it is not required by the canonical path, approved tests, supported integrations, or documented operational workflows.

Required sequence:

```text
DISCOVER
  -> CLASSIFY
  -> MAP DEPENDENCIES
  -> SELECT CANONICAL REPLACEMENT
  -> MIGRATE CONSUMERS
  -> VALIDATE
  -> BACKUP / ARCHIVE
  -> REMOVE ONLY WHEN PROVEN SAFE
```

"Looks unused" is not sufficient evidence for removal.

## 9. No Manual Editing

All repository modifications SHALL be performed through reproducible commands, scripts, repository tooling, or controlled automation.

Manual editor changes are prohibited for governed project work.

Every change MUST be reproducible and MUST be followed by appropriate syntax, contract, integration, or runtime validation.

## 10. Change Discipline

Every architectural change SHALL follow:

```text
INSPECT
  -> BACKUP / CHECKPOINT
  -> DECIDE
  -> AUTOMATED CHANGE
  -> COMPILE / STATIC VALIDATION
  -> TARGETED TEST
  -> INTEGRATION TEST
  -> RECORD RESULT
```

No implementation begins merely because a file name appears relevant.

## 11. One Canonical Entry Point

The project SHALL expose one documented production entry point. Internal engines may be numerous, but production orchestration MUST have one owner and one documented invocation path.

A legacy entry point may remain temporarily only when explicitly classified and excluded from the canonical production path.

## 12. Production Manifest

Every production run SHALL converge on one authoritative `ProductionManifest` containing, as applicable:

- production identity
- topic
- knowledge state
- evidence state
- article state
- media state
- video state
- HTML state
- SEO/schema state
- quality state
- safety state
- approval state
- publishing state
- distribution state
- analytics state
- version
- timestamps
- errors and degraded-mode information

No downstream stage may fabricate a missing upstream state.

## 13. Quality, Safety, and Approval Gate

Publishing is prohibited unless the canonical quality, scientific validation, and safety gates approve the production manifest.

A provider outage, missing media item, failed citation check, invalid HTML, or other failed dependency MUST remain visible in the manifest and MUST NOT be converted into an artificial success state.

## 14. Documentation and Ownership

Every approved production component SHALL have a clear owner/responsibility and dependency position in the architecture registry.

A future engineer must be able to determine from the repository:

1. what the canonical production path is;
2. which files are approved;
3. which contracts are authoritative;
4. which components are legacy or experimental;
5. how provider failure is handled;
6. what command runs production;
7. what command validates governance.

## 15. Governance Violations Block Integration and Release

Any of the following is a release blocker:

- more than one undocumented production path;
- an unapproved component used by production;
- a contract violation;
- unsafe or unverified deletion;
- manual governed edits;
- provider failure treated as success;
- missing internal fallback;
- bypassing quality/safety approval;
- undocumented production entry points;
- tests or workflows that validate a non-canonical path as if it were production.

A governance violation MUST block integration and release until corrected or the law is formally amended.

## 16. Architecture Freeze Rule

While the architecture is being stabilized, no new engine, bridge, pipeline, manager, wrapper, duplicate validator, or duplicate publisher may be introduced unless the architecture decision explicitly proves that an existing approved component cannot own the responsibility.

## 17. Amendments

This law is intentionally strict. Amendments require:

1. a documented reason;
2. impact/dependency analysis;
3. explicit architecture decision;
4. automated validation;
5. update of `.arvet/project_law.json`;
6. update of the affected architecture documentation;
7. a new repository checkpoint/commit.

An amendment is not valid merely because code was changed.

## 18. Current Stabilization State

The repository is currently in **ARCHITECTURE STABILIZATION / GOVERNANCE BOOTSTRAP**.

Therefore:

- the canonical architecture is defined at the responsibility level;
- the exact approved file/engine registry is NOT yet considered complete;
- dependency mapping and classification MUST be completed before cleanup;
- release remains BLOCKED until governance validation passes;
- no cleanup deletion is authorized by this document at bootstrap time.

## 19. Non-Negotiable Project Principles

```text
ONE CANONICAL PRODUCTION PATH
ONE OWNER PER RESPONSIBILITY
EXPLICIT CONTRACTS
KNOWLEDGE IS NOT RAW ARTICLE TEXT
EVIDENCE IS TRACEABLE
AI PROVIDERS ARE NOT THE SOURCE OF TRUTH
INTERNAL FALLBACK IS REQUIRED
NO PROVIDER FAILURE = SUCCESS
NO MANUAL GOVERNED EDITS
NO UNVERIFIED DELETIONS
NO DUPLICATE PRODUCTION PATHS
QUALITY + SAFETY GATE PUBLISHING
GOVERNANCE VIOLATION = INTEGRATION/RELEASE BLOCK
```

**This document governs the project.**
