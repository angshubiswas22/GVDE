# GVDE Current Development Status

## Completed

### Database

- PostgreSQL configured
- PostGIS enabled

### SQLAlchemy

Completed models:

- Source
- Location
- Panorama
- Image
- Collection
- collection_images

Relationships verified.

---

### Repository Layer

Completed:

- SourceRepository
- LocationRepository
- PanoramaRepository
- ImageRepository
- CollectionRepository

Each repository has been tested successfully.

---

### Service Layer

Completed:

IngestionService

Verified working through end-to-end tests.

---

### Collector Framework

Completed:

BaseCollector

GoogleMetadataCollector (skeleton)

Google parser

---

### Schemas

Completed:

PanoramaMetadata

ImageMetadata

Parser now returns schema objects instead of dictionaries.

---

### Tests

Verified:

- Repository tests
- Service tests
- Parser tests
- Collector tests

All currently pass.

---

# Known Current Limitations

Current ingestion creates duplicate locations.

Panorama uniqueness is enforced by the database.

Future work should make ingestion idempotent by checking for existing panoramas before insertion.

This is intentionally postponed until after the collector is functional.

---

# Immediate Next Goal

Implement GoogleMetadataCollector.collect().

Initially use mocked Google responses.

After collector flow is verified:

Collector

↓

Parser

↓

PanoramaMetadata

↓

IngestionService

↓

Database

Only after this pipeline is stable should real Google metadata retrieval be implemented.

---

# Long-Term Goals

Build a scalable dataset generation engine capable of producing high-quality street-view image datasets.

Future functionality may include:

- Metadata collection
- Image downloading
- Dataset versioning
- Image filtering
- Image quality checks
- Collection generation
- Machine learning dataset export

Development should remain incremental.