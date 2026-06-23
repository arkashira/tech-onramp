# TECH_SPEC.md – Tech‑OnRamp

> **Project**: Tech‑OnRamp  
> **Purpose**: A lightweight curriculum engine that loads course modules from Markdown files, parses metadata, and publishes them to a target (static site, API, or LMS).  
> **Scope**: Core engine, CLI, and optional FastAPI web interface.  
> **Audience**: Engineering, QA, DevOps, and Product teams.

---

## 1. Architecture Overview

```
┌───────────────────────┐
│  Content Repository   │
│  ──────────────────── │
│  content/modules/      │
│  ├─ intro.md           │
│  ├─ advanced.md        │
│  └─ ...                │
└─────────────┬─────────┘
              │
              ▼
┌───────────────────────┐   ┌───────────────────────┐
│  CurriculumEngine      │   │  CLI / FastAPI Layer   │
│  ──────────────────── │   │  ──────────────────── │
│  - load_modules()      │   │  - publish()          │
│  - publish_module()    │   │  - list_modules()     │
│  - get_module()        │   │  - get_module()       │
│  - list_modules()      │   │  - health()           │
└─────────────┬─────────┘   └─────────────┬─────────┘
              │                        │
              ▼                        ▼
┌───────────────────────┐   ┌───────────────────────┐
│  Module Store (DB)    │   │  Publisher (Static,   │
│  ──────────────────── │   │  API, LMS, etc.)      │
│  - SQLite / Postgres  │   │  ──────────────────── │
│  - ORM (SQLAlchemy)   │   │  - Render templates   │
│  - Migration (Alembic)│   │  - Push to S3 / API   │
└───────────────────────┘   └───────────────────────┘
```

* **Content Repository** – Markdown files with YAML front‑matter.  
* **CurriculumEngine** – Core business logic.  
* **CLI / FastAPI** – User interface for manual publishing or programmatic access.  
* **Module Store** – Persistent storage of parsed modules.  
* **Publisher** – Handles output to the chosen destination.

---

## 2. Core Components

| Component | Responsibility | Key Classes / Functions |
|-----------|----------------|-------------------------|
| **ModuleLoader** | Reads Markdown files, extracts metadata & body. | `load_file(path: Path) -> Module` |
| **MetadataParser** | Parses YAML front‑matter into `ModuleMetadata`. | `parse_metadata(text: str) -> ModuleMetadata` |
| **CurriculumEngine** | Orchestrates loading, validation, and publishing. | `CurriculumEngine.load_modules()`, `publish_module(id)`, `get_module(id)`, `list_modules()` |
| **ModuleStore** | Persists modules. | `ModuleRepository` (SQLAlchemy) |
| **Publisher** | Renders modules to target format. | `StaticPublisher`, `APIPublisher` |
| **CLI** | Command‑line interface. | `cli.py` (click) |
| **FastAPI** | Optional web API. | `api.py` |

---

## 3. Data Model

```python
# models.py
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field

class ModuleMetadata(BaseModel):
    title: str
    description: Optional[str] = None
    author: str
    tags: List[str] = []
    version: str = "1.0.0"
    published_at: Optional[datetime] = None
    draft: bool = False

class Module(BaseModel):
    id: str  # UUID
    metadata: ModuleMetadata
    content: str  # Markdown body
    created_at: datetime
    updated_at: datetime
```

* **`id`** – UUID4 string.  
* **`metadata`** – Parsed YAML front‑matter.  
* **`content`** – Raw Markdown body (excluding front‑matter).  
* **`created_at / updated_at`** – Timestamps.

---

## 4. Key APIs / Interfaces

| Method | Signature | Description |
|--------|-----------|-------------|
| `CurriculumEngine.load_modules(directory: Path)` | `None` | Scans `directory`, loads all Markdown files, validates, and stores them. |
| `CurriculumEngine.get_module(module_id: str)` | `Module` | Retrieves a module by ID. |
| `CurriculumEngine.list_modules(filter: Optional[dict] = None)` | `List[Module]` | Returns all modules, optionally filtered by tags, author, etc. |
| `CurriculumEngine.publish_module(module_id: str, publisher: Publisher)` | `None` | Publishes a single module using the supplied publisher. |
| `CurriculumEngine.publish_all(publisher: Publisher)` | `None` | Publishes all non‑draft modules. |
| `Publisher.publish(module: Module)` | `PublishResult` | Renders and outputs the module. |

**PublishResult**

```python
class PublishResult(BaseModel):
    module_id:
