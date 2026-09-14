# GeoVision Data Engine (GVDE)

## Project Overview

GVDE (GeoVision Data Engine) is a long-term project for building a scalable geospatial image dataset generation pipeline.

The primary objective is to automatically collect, organize, and prepare large-scale street-view imagery for future computer vision and machine learning tasks.

This is NOT a university thesis. The project is intended to become a robust software system that can evolve over time.

---

# Primary Data Source

Current primary source:

- Google Street View

Do NOT design around:

- Mapillary
- KartaView

Those platforms are intentionally excluded because they do not meet the desired imagery quality.

---

# Technology Stack

Backend:
- Python

Database:
- PostgreSQL
- PostGIS

ORM:
- SQLAlchemy

Architecture:

Database
↓
Repositories
↓
Services
↓
Collectors
↓
Schemas

---

# Current Folder Structure

app/

database/
- connection.py
- models.py

repositories/

services/

collectors/
    base_collector.py

    google/
        metadata_collector.py
        parser.py

schemas/
    panorama_schema.py
    image_schema.py

tests/

---

# Development Philosophy

Follow incremental development.

Do NOT rewrite working code.

Do NOT refactor simply because code could be cleaner.

Avoid unnecessary abstractions.

Prefer stable progress over perfect architecture.

If an improvement is optional, discuss it before implementing.

---

# Coding Style

- Keep functions focused.
- Use SQLAlchemy ORM.
- Keep repository layer responsible for database access.
- Keep service layer responsible for business logic.
- Collectors should never write directly to the database.
- Parsers convert external data into GVDE schema objects.

---

# Internal Pipeline

External Metadata
↓

Collector
↓

Parser
↓

PanoramaMetadata / ImageMetadata
↓

IngestionService
↓

Repositories
↓

PostgreSQL

---

# Development Rule

Before modifying architecture:

1. Explain why.
2. Explain benefits.
3. Wait for confirmation if the change is significant.

Avoid introducing unnecessary complexity.

The project values maintainability over cleverness.