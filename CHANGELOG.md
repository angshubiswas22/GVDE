# Changelog

All notable project milestones are documented here.

---

## 2026-07-27

### Database

- Designed PostgreSQL/PostGIS schema.
- Added SQLAlchemy ORM models.
- Added collection_images association table.

### Repository Layer

- Implemented SourceRepository.
- Implemented LocationRepository.
- Implemented PanoramaRepository.
- Implemented ImageRepository.
- Implemented CollectionRepository.

### Service Layer

- Implemented IngestionService.

### Collector Framework

- Added BaseCollector abstraction.
- Added GoogleMetadataCollector skeleton.
- Added Google metadata parser.

### Schemas

- Added PanoramaMetadata schema.
- Added ImageMetadata schema.

### Testing

- Repository tests completed.
- Service tests completed.
- Parser tests completed.
- Collector tests completed.

Current development milestone:

Collector → Parser → Schema → Ingestion pipeline operational using mocked data.