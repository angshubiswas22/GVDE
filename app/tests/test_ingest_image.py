from app.database.connection import SessionLocal

from app.services.ingestion_service import IngestionService

from app.collectors.google.google_image_collector import (
    GoogleImageCollector
)

from app.repositories.panorama_repository import PanoramaRepository


def test_ingest_image():

    session = SessionLocal()

    service = IngestionService(session)

    panorama_repo = PanoramaRepository(session)

    panorama = panorama_repo.get_panorama_by_id(1)

    collector = GoogleImageCollector()

    image_metadata = collector.download_image(
        panorama=panorama,
        output_directory="dataset/test"
    )

    image = service.ingest_image(
        panorama_id=panorama.id,
        image_metadata=image_metadata
    )

    print(image.id)
    print(image.file_path)
    print(image.width)
    print(image.height)

    session.close()


if __name__ == "__main__":
    test_ingest_image()