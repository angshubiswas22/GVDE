from app.repositories.source_repository import SourceRepository
from app.repositories.location_repository import LocationRepository
from app.repositories.panorama_repository import PanoramaRepository
from app.repositories.image_repository import ImageRepository
from app.repositories.collection_repository import CollectionRepository



class IngestionService:

    def __init__(self, session):

        self.source_repo = SourceRepository(session)

        self.location_repo = LocationRepository(session)

        self.panorama_repo = PanoramaRepository(session)

        self.image_repo = ImageRepository(session)

        self.collection_repo = CollectionRepository(session)



    def ingest_panorama(
        self,
        source_name,
        source_type,
        latitude,
        longitude,
        source_panorama_id,
        images,
        collection_id=None,
        capture_time=None,
        heading=None,
        pitch=None,
        roll=None,
        width=None,
        height=None
    ):
        source = self.source_repo.get_source_by_name(
    source_name
    )

        if source is None:

            source = self.source_repo.create_source(
                name=source_name,
                source_type=source_type
        )


        # 1. Create location

        location = self.location_repo.create_location(
            latitude=latitude,
            longitude=longitude
        )


        # 2. Create panorama

        panorama = self.panorama_repo.create_panorama(
            location_id=location.id,
            source_id=source.id,
            source_panorama_id=source_panorama_id,
            capture_time=capture_time,
            heading=heading,
            pitch=pitch,
            roll=roll,
            width=width,
            height=height
        )


        # 3. Create images

        created_images = []


        for image_metadata in images:

            image = self.ingest_image(
                panorama_id=panorama.id,
                image_metadata=image_metadata,
                collection_id=collection_id
            )

            created_images.append(image)



            # 4. Attach image to collection if provided

            if collection_id:

                self.collection_repo.add_image_to_collection(
                    collection_id=collection_id,
                    image_id=image.id
                )


        return {
            "location": location,
            "panorama": panorama,
            "images": created_images
        }

    def ingest_image(
    self,
    panorama_id,
    image_metadata,
    collection_id=None
):

        image = self.image_repo.create_image(
            panorama_id=panorama_id,
            file_path=image_metadata.file_path,
            heading=image_metadata.heading,
            pitch=image_metadata.pitch,
            field_of_view=image_metadata.field_of_view,
            width=image_metadata.width,
            height=image_metadata.height,
            image_hash=image_metadata.image_hash,
            metadata_json=None
        )

        if collection_id:

            self.collection_repo.add_image_to_collection(
                collection_id=collection_id,
                image_id=image.id
            )

        return image