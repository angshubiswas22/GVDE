import os

from app.database.connection import SessionLocal

from app.collectors.google.metadata_collector import (
    GoogleMetadataCollector
)

from app.collectors.google.parser import (
    parse_panorama_metadata
)
from app.collectors.google.google_image_collector import (
    GoogleImageCollector
)

from app.services.ingestion_service import IngestionService


def test_end_to_end_ingestion():

    session = SessionLocal()

    service = IngestionService(session)

    metadata_collector = GoogleMetadataCollector()

    image_collector = GoogleImageCollector()

    #
    # 1. Collect raw metadata
    #

    raw_metadata = metadata_collector.collect(
        latitude=23.8103,
        longitude=90.4125
    )

    #
    # 2. Parse metadata
    #

    panorama_metadata = parse_panorama_metadata(
        raw_metadata
    )


    #
    # 3. Store panorama + parsed images
    #

    result = service.ingest_panorama(
        source_name=panorama_metadata.source_name,
        source_type=panorama_metadata.source_type,

        latitude=panorama_metadata.latitude,
        longitude=panorama_metadata.longitude,

        source_panorama_id=panorama_metadata.source_panorama_id,

        images=panorama_metadata.images,

        capture_time=panorama_metadata.capture_time,
        heading=panorama_metadata.heading,
        pitch=panorama_metadata.pitch,
        roll=panorama_metadata.roll)

    panorama = result["panorama"]

    #
    # 4. Download image
    #

    downloaded_image = image_collector.download_image(
        panorama,
        "dataset/test"
    )

    #
    # 5. Store downloaded image
    #

    image = service.ingest_image(
        panorama.id,
        downloaded_image
    )

    #
    # 6. Verify
    #

    assert panorama.id is not None

    assert image.id is not None

    assert os.path.exists(
        downloaded_image.file_path
    )

    print()

    print("========== END TO END SUCCESS ==========")

    print(
        "Location ID:",
        result["location"].id
    )

    print(
        "Panorama ID:",
        panorama.id
    )

    print(
        "Image ID:",
        image.id
    )

    print(
        "Image:",
        downloaded_image.file_path
    )

    session.close()


if __name__ == "__main__":
    test_end_to_end_ingestion()