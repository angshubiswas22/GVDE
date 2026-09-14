from app.database.connection import SessionLocal
from app.repositories.collection_repository import CollectionRepository


def test_collection_repository():

    session = SessionLocal()

    repo = CollectionRepository(session)


    collection = repo.create_collection(
        name="GVDE Test Dataset",
        version="v1",
        description="Initial test collection",
        sampling_strategy={
            "method": "random"
        }
    )


    print(
        collection.id,
        collection.name,
        collection.version
    )


    added = repo.add_image_to_collection(
        collection_id=collection.id,
        image_id=1
    )


    print(
        "Image added:",
        added
    )


    images = repo.get_images_in_collection(
        collection.id
    )


    for image in images:
        print(
            image.id,
            image.file_path
        )


    session.close()


if __name__ == "__main__":
    test_collection_repository()