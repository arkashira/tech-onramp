# ROADMAP.md

## Project: tech‑onramp  
**Goal** – Deliver a lightweight, extensible curriculum engine that can load, parse, and publish educational modules from Markdown files.  
**Scope** – Start with a minimal, production‑ready MVP, then iterate with feature‑rich v1/v2 releases that enable richer content, analytics, and integration with external LMS platforms.

---

## 1. MVP (Must‑Have for Launch)

| Milestone | Description | Deliverables | Acceptance Criteria |
|-----------|-------------|--------------|---------------------|
| **1.1 Core Engine** | Load Markdown files, extract front‑matter metadata, and expose a simple API. | - `CurriculumEngine` class<br>- `Module` dataclass<br>- `load_modules()` and `publish_modules()` methods | - All unit tests pass (`python -m pytest`).<br>- Engine can read at least 10 sample modules. |
| **1.2 CLI Tool** | Quick command‑line interface to list and publish modules. | - `tech_onramp_cli.py` with `list`, `publish` commands | - CLI runs without errors.<br>- `publish` writes a JSON manifest to `output/`. |
| **1.3 Basic Tests** | Unit tests for parsing and publishing logic. | - `tests/test_engine.py` covering metadata extraction, error handling, and output format | - 100 % code coverage for core functions. |
| **1.4 Documentation** | README with usage, API reference, and contribution guide. | - Updated README<br>- `docs/` directory | - README contains clear steps to create modules and run tests. |
| **1.5 CI Pipeline** | GitHub Actions to run tests on every push. | - `.github/workflows/ci.yml` | - Pipeline passes on all branches. |

> **MVP‑Critical**: 1.1, 1.2, 1.3, 1.5

---

## 2. v1 – Feature‑Rich Release

| Theme | Feature | Owner | Target Release |
|-------|---------|-------|----------------|
| **Content Management** | • Rich metadata schema (title, author, tags, prerequisites, duration).<br>• Validation against JSON‑Schema. | Backend | Q3 2026 |
| **Publishing** | • Publish to static site generator (e.g., MkDocs).<br>• Generate per‑module HTML pages. | Backend | Q3 2026 |
| **CLI Enhancements** | • `create` command to scaffold new modules.<br>• `validate` command to lint metadata. | DevOps | Q4 2026 |
| **Testing** | • Integration tests for publishing pipeline.<br>• End‑to‑end test with a sample static site. | QA | Q4 2026 |
| **Documentation** | • Auto‑generate API docs from type hints.<br>• Add example modules in `content/modules`. | Docs | Q4 2026 |

---

## 3. v2 – Platform‑Ready Release

| Theme | Feature | Owner | Target Release |
|-------|---------|-------|----------------|
| **LMS Integration** | • REST API to push modules to external LMS (e.g., Canvas, Moodle). | Backend | Q1 2027 |
| **Analytics** | • Track module views and completion rates via embedded hooks. | Data | Q1 2027 |
| **UI Frontend** | • Minimal React app to browse and preview modules. | Frontend | Q2 2027 |
| **Security** | • Authentication for API endpoints.<br>• Role‑based access control for module publishing. | Security | Q2 2027 |
| **Performance** | • Caching layer for parsed modules.<br>• Parallel publishing. | Ops | Q3 2027 |
| **Internationalization** | • Support for multiple languages in metadata and content. | Localization | Q3 2027 |

---

## 4. Release Cadence

| Release | Type | Frequency | Notes |
|---------|------|-----------|-------|
| MVP | Initial | 1 month | Must be shipped before any external demo. |
| v1 | Major | 3 months | Adds core content features. |
| v2 | Major | 4 months | Platform‑ready with LMS integration. |

---

## 5. Dependencies & Risks

| Dependency | Impact | Mitigation |
|------------|--------|------------|
| Markdown parser | High | Use `markdown-it-py` (well‑maintained). |
| Static site generator | Medium | Abstract output format; allow custom generators. |
| External LMS APIs | High | Design API adapters; mock during development. |
| CI/CD pipeline | Medium | Leverage GitHub Actions; ensure caching. |

---

## 6. Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Unit test coverage | ≥ 95 % | Codecov |
| Publish latency | ≤ 2 s per module | Benchmark |
| User adoption | 100+ modules published in first 3 months | GitHub stats |
| LMS integration success | 90 % of modules successfully pushed | API logs |

---

## 7. Roadmap Timeline (2026‑2027)

```
2026-07   MVP (MVP‑Critical)
2026-09   v1 Feature‑Rich Release
2027-01   v2 Platform‑Ready Release
```

---

### Next Steps

1. **Finalize MVP scope** – Confirm all critical features with stakeholders.  
2. **Kick‑off sprint** – Allocate tasks to team members.  
3. **Set up CI** – Ensure automated tests run on every commit.  
4. **Document** – Keep `ROADMAP.md` updated with any scope changes.

---
