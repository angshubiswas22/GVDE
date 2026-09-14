from app.database.connection import SessionLocal
from app.repositories.image_repository import ImageRepository


def test_image_repository():

    session = SessionLocal()

    repo = ImageRepository(session)


    image = repo.create_image(
        panorama_id=1,
        file_path="dataset/test/image_001.jpg",
        heading=90.0,
        pitch=0.0,
        field_of_view=90.0,
        width=1024,
        height=1024,
        image_hash="abc123"
    )


    print(
        image.id,
        image.panorama_id,
        image.file_path,
        image.image_hash
    )


    session.close()


if __name__ == "__main__":
    test_image_repository()