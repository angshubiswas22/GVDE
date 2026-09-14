from sqlalchemy.orm import Session

from app.database.models import Image


class ImageRepository:

    def __init__(self, session: Session):
        self.session = session


    def create_image(
        self,
        panorama_id: int,
        file_path: str,
        heading=None,
        pitch=None,
        field_of_view=None,
        width=None,
        height=None,
        image_hash=None,
        metadata_json=None
    ):

        image = Image(
            panorama_id=panorama_id,
            file_path=file_path,
            heading=heading,
            pitch=pitch,
            field_of_view=field_of_view,
            width=width,
            height=height,
            image_hash=image_hash,
            metadata_json=metadata_json
        )


        self.session.add(image)
        self.session.commit()
        self.session.refresh(image)

        return image


    def get_image_by_id(
        self,
        image_id: int
    ):

        return (
            self.session.query(Image)
            .filter(Image.id == image_id)
            .first()
        )


    def get_images_by_panorama(
        self,
        panorama_id: int
    ):

        return (
            self.session.query(Image)
            .filter(
                Image.panorama_id == panorama_id
            )
            .all()
        )


    def get_image_by_hash(
        self,
        image_hash: str
    ):

        return (
            self.session.query(Image)
            .filter(
                Image.image_hash == image_hash
            )
            .first()
        )


    def get_all_images(self):

        return (
            self.session.query(Image)
            .all()
        )


    def delete_image(
        self,
        image_id: int
    ):

        image = self.get_image_by_id(image_id)

        if image:

            self.session.delete(image)
            self.session.commit()

            return True

        return False