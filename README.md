# GeoVision Data Engine (GVDE)

## Overview

GeoVision Data Engine (GVDE) is a Python-based geospatial dataset generation engine designed to collect, organize, and manage large-scale street-view imagery.

The project focuses on building a reliable and extensible pipeline that transforms geographic metadata into structured datasets suitable for computer vision and machine learning applications.

GVDE emphasizes clean architecture, incremental development, and maintainability.

---

## Goals

- Build a scalable geospatial image dataset generation engine using high-quality street-view imagery
- Organize metadata using PostgreSQL + PostGIS.
- Maintain a clean layered architecture.
- Support automated dataset generation.
- Produce versioned datasets for future AI and computer vision projects.

---

## Technology Stack

Backend

- Python

Database

- PostgreSQL
- PostGIS

ORM

- SQLAlchemy

---

## Current Architecture

External Metadata

↓

Collectors

↓

Parsers

↓

Schemas

↓

Services

↓

Repositories

↓

PostgreSQL

---

## Current Project Status

The project currently includes:

- Database schema
- SQLAlchemy models
- Repository layer
- Service layer
- Collector framework
- Google parser
- Internal schemas

The next milestone is implementing metadata collection and integrating it with the ingestion pipeline.

---

## Repository Structure

app/

database/

repositories/

services/

collectors/

schemas/

tests/

---

## Development Philosophy

- Build incrementally.
- Avoid unnecessary abstraction.
- Do not rewrite working code without a clear benefit.
- Test every layer before progressing.# GeoVision Data Engine (GVDE)

## Overview

GeoVision Data Engine (GVDE) is a Python-based geospatial dataset generation engine designed to collect, organize, and manage large-scale street-view imagery.

The project focuses on building a reliable and extensible pipeline that transforms geographic metadata into structured datasets suitable for computer vision and machine learning applications.

GVDE emphasizes clean architecture, incremental development, and maintainability.

---

## Goals

- Build a scalable street-view dataset generation engine.
- Organize metadata using PostgreSQL + PostGIS.
- Maintain a clean layered architecture.
- Support automated dataset generation.
- Produce versioned datasets for future AI and computer vision projects.

---

## Technology Stack

Backend

- Python

Database

- PostgreSQL
- PostGIS

ORM

- SQLAlchemy

---

## Current Architecture

External Metadata

↓

Collectors

↓

Parsers

↓

Schemas

↓

Services

↓

Repositories

↓

PostgreSQL

---

## Current Project Status

The project currently includes:

- Database schema
- SQLAlchemy models
- Repository layer
- Service layer
- Collector framework
- Google parser
- Internal schemas

The next milestone is implementing metadata collection and integrating it with the ingestion pipeline.

---

## Repository Structure

app/

database/

repositories/

services/

collectors/

schemas/

tests/

---

## Development Philosophy

- Build incrementally.
- Avoid unnecessary abstraction.
- Do not rewrite working code without a clear benefit.
- Test every layer before progressing.