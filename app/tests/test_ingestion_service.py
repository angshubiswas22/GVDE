from app.database.connection import SessionLocal
from app.services.ingestion_service import IngestionService


def test_ingestion_service():

    session = SessionLocal()

    service = IngestionService(session)


    result = service.ingest_panorama(

        source_name="Google Street View",

        source_type="street_view",

        latitude=23.8103,

        longitude=90.4125,

        source_panorama_id="service_test_panorama_003",


        images=[
            {
                "file_path": "dataset/service_test/image_001.jpg",
                "heading": 0.0,
                "pitch": 0.0,
                "field_of_view": 90.0,
                "width": 2048,
                "height": 1024,
                "image_hash": "service_hash_001"
            },

            {
                "file_path": "dataset/service_test/image_002.jpg",
                "heading": 90.0,
                "pitch": 0.0,
                "field_of_view": 90.0,
                "width": 2048,
                "height": 1024,
                "image_hash": "service_hash_002"
            }
        ],


        collection_id=1
    )


    print(
        "Location:",
        result["location"].id
    )


    print(
        "Panorama:",
        result["panorama"].id
    )


    print(
        "Images:"
    )


    for image in result["images"]:
        print(
            image.id,
            image.file_path
        )


    session.close()



if __name__ == "__main__":
    test_ingestion_service()