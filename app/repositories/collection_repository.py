from sqlalchemy.orm import Session

from app.database.models import Collection, Image


class CollectionRepository:

    def __init__(self, session: Session):
        self.session = session


    def create_collection(
        self,
        name: str,
        version: str,
        description=None,
        sampling_strategy=None,
        metadata_json=None
    ):

        collection = Collection(
            name=name,
            version=version,
            description=description,
            sampling_strategy=sampling_strategy,
            metadata_json=metadata_json
        )

        self.session.add(collection)
        self.session.commit()
        self.session.refresh(collection)

        return collection


    def get_collection_by_id(
        self,
        collection_id: int
    ):

        return (
            self.session.query(Collection)
            .filter(
                Collection.id == collection_id
            )
            .first()
        )


    def get_all_collections(self):

        return (
            self.session.query(Collection)
            .all()
        )


    def add_image_to_collection(
        self,
        collection_id: int,
        image_id: int
    ):

        collection = self.get_collection_by_id(collection_id)

        image = (
            self.session.query(Image)
            .filter(
                Image.id == image_id
            )
            .first()
        )


        if collection and image:

            collection.images.append(image)

            self.session.commit()

            return True


        return False


    def remove_image_from_collection(
        self,
        collection_id: int,
        image_id: int
    ):

        collection = self.get_collection_by_id(collection_id)

        image = (
            self.session.query(Image)
            .filter(
                Image.id == image_id
            )
            .first()
        )


        if collection and image:

            collection.images.remove(image)

            self.session.commit()

            return True


        return False


    def get_images_in_collection(
        self,
        collection_id: int
    ):

        collection = self.get_collection_by_id(collection_id)

        if collection:
            return collection.images

        return []