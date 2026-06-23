# STORIES.md – tech‑onramp

## Overview

`tech-onramp` is a **Curriculum Engine & Content Delivery** system.  
It loads course modules from Markdown files, parses front‑matter metadata, and publishes the modules via a lightweight API.  
The following backlog is grouped into three epics that reflect the natural build‑up of the product.  
Stories are ordered to deliver a Minimum Viable Product (MVP) that can be tested with `pytest` and used by downstream services.

---

## Epic 1 – Core Curriculum Engine

| # | User Story | Acceptance Criteria |
|---|------------|---------------------|
| **1.1** | **As a content author, I want the engine to discover Markdown files in `content/modules`, so that I can add new lessons without touching code.** | • The engine scans `content/modules` recursively.<br>• It returns a list of file paths.<br>• No hard‑coded file names are required. |
| **1.2** | **As a content author, I want the engine to parse YAML front‑matter into a `ModuleMetadata` dataclass, so that I can define title, slug, tags, and prerequisites.** | • Front‑matter is parsed correctly.<br>• Missing required fields raise a clear `MetadataError`.<br>• Optional fields default to sensible values. |
| **1.3** | **As a developer, I want the engine to expose a `load_modules()` method that returns a list of `Module` objects, so that the rest of the system can work with a consistent API.** | • `load_modules()` returns a list of `Module` instances.<br>• Each `Module` contains `metadata` and `content`.<br>• The method is deterministic and idempotent. |
| **1.4** | **As a QA engineer, I want unit tests for the parsing logic, so that regressions are caught early.** | • Tests cover valid and invalid front‑matter.<br>• Test coverage ≥ 90% for parsing module.<br>• Tests run with `pytest`. |

---

## Epic 2 – Content Delivery API

| # | User Story | Acceptance Criteria |
|---|------------|---------------------|
| **2.1** | **As a learner, I want a REST endpoint `/modules` that lists all published modules, so that I can browse the curriculum.** | • GET `/modules` returns JSON array of modules.<br>• Response includes `slug`, `title`, `tags`, `prerequisites`.<br>• Pagination is supported via `?page=` and `?size=`. |
| **2.2** | **As a learner, I want a REST endpoint `/modules/{slug}` that returns the full module content, so that I can view a lesson.** | • GET `/modules/{slug}` returns JSON with `title`, `content`, `metadata`.<br>• 404 is returned for unknown slugs.<br>• Content is sanitized (no raw HTML). |
| **2.3** | **As a developer, I want the API to support filtering by tag, so that I can build tag‑based navigation.** | • GET `/modules?tag=python` returns only modules tagged `python`.<br>• Multiple tags can be combined with `&tag=python&tag=ml`. |
| **2.4** | **As a system integrator, I want the API to expose a health‑check endpoint `/health`, so that monitoring tools can verify uptime.** | • GET `/health` returns 200 with JSON `{status: "ok"}`.<br>• The endpoint is lightweight and does not load all modules. |
| **2.5** | **As a DevOps engineer, I want the API to log request metadata, so that we can audit usage.** | • Each request logs method, path, status, and response time.<br>• Logs are written to stdout in JSON format. |

---

## Epic 3 – Admin & Analytics

| # | User Story | Acceptance Criteria |
|---|------------|---------------------|
| **3.1** | **As an admin, I want a CLI command `publish` that marks modules as published, so that only approved content is served.** | • `python -m tech_onramp.publish` reads modules and writes a `published.json` file.<br>• Published modules are the only ones returned by the API.<br>• The command is idempotent. |
| **3.2** | **As an admin, I want the engine to support versioning of modules, so that I can roll back to previous content.** | • Each module has a `version` field.<br>• `publish` writes a new version entry.<br>• API can fetch a specific version via `/modules/{slug}/v{n}`. |
| **3.3** | **As a product manager, I want analytics on module views, so that I can identify popular lessons.** | • Each module view increments a counter stored in `analytics.json`.<br>• Endpoint `/analytics/modules` returns view counts.<br>• Data is persisted across restarts. |
| **3.4** | **As a learner, I want to track my progress through modules, so that I can resume where I left off.** | • API supports POST `/progress` with `user_id`, `module_slug`, `status`.<br>• GET `/progress/{user_id}` returns a list of completed modules
