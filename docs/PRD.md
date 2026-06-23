# Product Requirements Document (PRD) – Tech‑OnRamp

**Project:** Tech‑OnRamp  
**Repository:** `tech-onramp`  
**Owner:** Senior Product/Engineering Lead  
**Last Updated:** 2026‑06‑23  

---

## 1. Executive Summary

Tech‑OnRamp is a lightweight, open‑source curriculum engine that turns Markdown modules into a publishable learning experience. It is designed for technical teams, bootcamps, and internal training programs that need a fast, reproducible way to author, version, and deliver course content without a heavyweight LMS. The engine parses front‑matter metadata, validates module structure, and exposes a simple API for publishing modules to static sites or other downstream systems.

---

## 2. Problem Statement

- **Fragmented Content Management:** Technical teams often store training material in disparate Markdown files, spreadsheets, or wikis, leading to version drift and inconsistent delivery.
- **Manual Publishing Overhead:** Publishing new modules requires manual steps (copying files, updating navigation, regenerating static sites), which is error‑prone and slows iteration.
- **Lack of Metadata‑Driven Workflows:** Existing tools do not enforce a consistent schema for module metadata, making it hard to generate curriculum outlines, prerequisites, or progress tracking.
- **Limited Reusability:** Content is rarely packaged for reuse across multiple courses or teams, wasting effort and increasing maintenance costs.

Tech‑OnRamp solves these problems by providing a **single source of truth** for curriculum modules, automating validation, and exposing a publish API that can be integrated into CI/CD pipelines.

---

## 3. Target Users

| Persona | Role | Pain Points | How Tech‑OnRamp Helps |
|---------|------|-------------|-----------------------|
| **Learning & Development Lead** | Oversees internal training | Need to quickly assemble and update courses | Auto‑validation of modules, metadata consistency, publish‑ready output |
| **Bootcamp Instructor** | Creates curriculum for bootcamps | Time‑consuming manual publishing | One‑click publish to static site or LMS |
| **Engineering Manager** | Manages onboarding docs | Inconsistent documentation quality | Enforces metadata schema, version control |
| **Open‑Source Educator** | Publishes free courses | Limited tooling for Markdown curriculum | Easy integration with static site generators (Hugo, Jekyll) |

---

## 4. Goals & Success Metrics

| Goal | Success Metric | Target |
|------|----------------|--------|
| **Fast, repeatable publishing** | Time from commit to live module < 5 min | 95 % of commits < 5 min |
| **High content quality** | 0 critical validation errors per release | 100 % of modules pass validation |
| **Adoption by internal teams** | Number of teams using Tech‑OnRamp | ≥ 5 teams within 6 months |
| **Extensibility** | Number of custom plugins/extensions | ≥ 3 community‑contributed plugins |
| **User satisfaction** | NPS score | ≥ +50 |

---

## 5. Key Features (Prioritized)

| # | Feature | Description | Priority | Owner |
|---|---------|-------------|----------|-------|
| 1 | **Metadata Schema Enforcement** | Validate front‑matter against JSON‑Schema (title, slug, prerequisites, tags, difficulty). | Must‑have | Engineering |
| 2 | **Module Loader** | Recursively load Markdown files from `content/modules`, parse metadata, and build an in‑memory graph. | Must‑have | Engineering |
| 3 | **Publish API** | `CurriculumEngine.publish()` returns a JSON representation or writes to a target directory for static site generators. | Must‑have | Engineering |
| 4 | **CLI Tool** | `tech-onramp-cli` for local validation, preview, and publishing. | Nice‑to‑have | Engineering |
| 5 | **CI/CD Integration** | GitHub Actions template that runs tests, validation, and publishes to GitHub Pages or S3. | Nice‑to‑have | DevOps |
| 6 | **Progress Tracking Metadata** | Optional fields for `completed`, `next`, `previous` modules to enable linear learning paths. | Nice‑to‑have | Product |
| 7 | **Internationalization Support** | Load language‑specific modules and generate locale‑aware URLs. | Nice‑to‑have | Engineering |
| 8 | **Plugin System** | Allow custom processors (e.g., embed code snippets, generate quizzes). | Nice‑to‑have | Engineering |
| 9 | **Documentation & Examples** | Comprehensive README, example curriculum, and unit tests. | Must‑have | Technical Writer |
| 10 | **Open‑Source Licensing** | MIT license with contributor guidelines. | Must‑have | Legal |

---

## 6. Success Criteria

1. **Zero critical validation failures** in the first 10 production releases.
2. **At least 3 distinct use‑cases** documented (e.g., internal onboarding, bootcamp, open‑source course) within 3 months.
3. **Community engagement**: ≥ 20 GitHub stars, ≥ 5 forks, ≥ 2 pull requests merged.
4. **Performance**: Module loading < 200 ms for 100 modules on a standard laptop.

---

## 7. Scope

| Category | Included | Excluded |
|----------|----------|----------|
| **Core Engine** | Parsing, validation, publishing | Full LMS features (quizzes, analytics) |
| **CLI** | Basic commands (`validate`, `preview`, `publish`) | Advanced UI, web interface |
| **CI/CD** | GitHub Actions template | GitLab CI, Azure DevOps |
| **Documentation** | README, usage guide, API docs | Full API reference (to be added later) |
| **Testing** | Unit tests for core logic | End‑to‑end integration tests with external LMS |
| **Internationalization** | Basic locale support | Full i18n framework integration |

---

## 8. Out‑of‑Scope

- Building a full Learning Management System (user accounts, progress tracking dashboards).
- Real‑time collaboration or live editing of modules.
- Integration with proprietary LMS platforms (unless requested by a specific customer).
- Mobile app or native client.

---

## 9. Dependencies

| Dependency | Purpose | Version |
|------------|---------|---------|
| `pytest` | Unit testing | ≥ 7.0 |
| `PyYAML` | Front‑matter parsing | ≥ 6.0 |
| `jsonschema` | Metadata validation | ≥ 4.0 |
| `click` | CLI interface | ≥ 8.0 |
| `mkdocs` (optional) | Preview static site | ≥ 1.0 |

---

## 10. Roadmap

| Phase | Milestone | Timeframe |
|-------|-----------|-----------|
| **Phase 1** | Core engine + validation | 1‑month |
| **Phase 2** | CLI + publish API | 1‑month |
| **Phase 3** | CI/CD template + docs | 1‑month |
| **Phase 4** | Plugin system + i18n | 2‑months |
| **Phase 5** | Community outreach & marketing | Ongoing |

---

## 11. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| **Schema changes break existing modules** | High | Provide migration scripts and backward‑compatibility layer. |
| **Limited adoption due to lack of UI** | Medium | Offer a simple web preview tool as a future enhancement. |
| **Security of published content** | Low | Enforce content sanitization; recommend hosting on trusted platforms. |

---

## 12. Acceptance Criteria

1. **All unit tests pass** (`pytest -q` returns 0 failures).
2. **Metadata validation** rejects any module missing required fields.
3. **Publish output** matches the expected JSON structure and can be consumed by a static site generator.
4. **CLI commands** (`validate`, `preview`, `publish`) work as documented.
5. **Documentation** includes a working example curriculum and clear usage instructions.

---

### Appendix

- **Sample Module Front‑Matter**

```markdown
---
title: "Introduction to Git"
slug: "git-intro"
difficulty: "beginner"
tags: ["git", "version-control"]
prerequisites: []
---
# Introduction to Git

Content goes here...
```

- **Example Publish Output**

```json
{
  "modules": [
    {
      "title": "Introduction to Git",
      "slug": "git-intro",
      "path": "content/modules/git-intro.md",
      "metadata": { ... }
    }
  ]
}
```

---
