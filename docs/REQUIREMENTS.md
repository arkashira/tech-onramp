# REQUIREMENTS.md – Tech‑OnRamp

## 1. Overview

Tech‑OnRamp is a **Curriculum Engine & Content Delivery** system that:

* Loads learning modules written in Markdown from a designated directory.
* Parses module metadata (YAML front‑matter) and validates it against a schema.
* Publishes modules to a target output (static files, JSON API, or a CMS endpoint).
* Provides a Python API (`CurriculumEngine`) for integration into larger systems.

The product is intended to be a core component of the Axentx portfolio, enabling rapid creation and deployment of validated, pay‑willing learning paths without duplicating existing releases.

---

## 2. Functional Requirements

| ID | Description | Acceptance Criteria |
|----|-------------|---------------------|
| **FR‑1** | **Module Discovery** | The engine scans `content/modules` recursively and identifies all `.md` files. |
| **FR‑2** | **Metadata Extraction** | Each Markdown file must contain YAML front‑matter. The engine extracts fields: `title`, `description`, `tags`, `prerequisites`, `author`, `published_at`. |
| **FR‑3** | **Metadata Validation** | Extracted metadata is validated against a JSON schema. Invalid modules are logged and skipped. |
| **FR‑4** | **Content Parsing** | The Markdown body is parsed into HTML using a safe markdown renderer (e.g., `mistune` or `markdown`). |
| **FR‑5** | **Module Object Model** | The engine exposes a `Module` dataclass with attributes: `id`, `metadata`, `content_html`, `path`. |
| **FR‑6** | **Publishing – Static Files** | The engine writes each module to `output/<module-id>/index.html` and generates a `modules.json` index. |
| **FR‑7** | **Publishing – API** | Optionally, the engine can POST module data to a REST endpoint (`/api/modules`). |
| **FR‑8** | **Incremental Build** | On subsequent runs, only changed modules are re‑processed. |
| **FR‑9** | **CLI Interface** | Provide a `python -m tech_onramp.cli` command that accepts `--watch`, `--output`, `--api-url`. |
| **FR‑10** | **Unit & Integration Tests** | All functionality is covered by `pytest` tests. |
| **FR‑11** | **Logging** | The engine logs actions at INFO level and errors at ERROR level. |
| **FR‑12** | **Extensibility** | The engine supports plugin hooks for custom metadata fields or output formats. |

---

## 3. Non‑Functional Requirements

| Category | Requirement | Target |
|----------|-------------|--------|
| **Performance** | **Load Time** | All modules are processed in ≤ 2 s on a standard laptop (8 GB RAM). |
| | **Memory Footprint** | Peak memory usage ≤ 200 MB. |
| | **Concurrency** | Engine can run in a multi‑threaded mode (`--workers`) without data races. |
| **Security** | **Input Sanitization** | Markdown rendering must escape HTML to prevent XSS. |
| | **File Permissions** | Only read access to `content/modules`; write access to `output`. |
| | **API Security** | Optional API publishing requires a bearer token. |
| **Reliability** | **Error Handling** | Invalid modules are logged and skipped; the engine continues processing. |
| | **Idempotency** | Re‑running the engine yields identical output given unchanged inputs. |
| | **Crash Recovery** | On crash, the engine resumes from the last processed file. |
| **Maintainability** | **Code Quality** | PEP‑8 compliant, type‑annotated, with docstrings. |
| | **Documentation** | Public API docs generated via Sphinx. |
| | **Test Coverage** | ≥ 90 % line coverage. |
| **Scalability** | **Large Catalogs** | Engine supports > 10 000 modules with linear scaling. |
| | **Plugin System** | New output formats can be added without modifying core logic. |

---
