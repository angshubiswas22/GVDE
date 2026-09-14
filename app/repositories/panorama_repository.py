from sqlalchemy.orm import Session

from app.database.models import Panorama


class PanoramaRepository:

    def __init__(self, session: Session):
        self.session = session


    def create_panorama(
        self,
        location_id: int,
        source_id: int,
        source_panorama_id: str,
        capture_time=None,
        heading=None,
        pitch=None,
        roll=None,
        width=None,
        height=None,
        metadata_json=None
    ):

        panorama = Panorama(
            location_id=location_id,
            source_id=source_id,
            source_panorama_id=source_panorama_id,
            capture_time=capture_time,
            heading=heading,
            pitch=pitch,
            roll=roll,
            width=width,
            height=height,
            metadata_json=metadata_json
        )


        self.session.add(panorama)
        self.session.commit()
        self.session.refresh(panorama)

        return panorama


    def get_panorama_by_id(
        self,
        panorama_id: int
    ):

        return (
            self.session.query(Panorama)
            .filter(Panorama.id == panorama_id)
            .first()
        )


    def get_panorama_by_source_id(
        self,
        source_panorama_id: str
    ):

        return (
            self.session.query(Panorama)
            .filter(
                Panorama.source_panorama_id == source_panorama_id
            )
            .first()
        )


    def get_all_panoramas(self):

        return (
            self.session.query(Panorama)
            .all()
        )


    def get_panoramas_by_location(
        self,
        location_id: int
    ):

        return (
            self.session.query(Panorama)
            .filter(
                Panorama.location_id == location_id
            )
            .all()
        )


    def get_panoramas_by_source(
        self,
        source_id: int
    ):

        return (
            self.session.query(Panorama)
            .filter(
                Panorama.source_id == source_id
            )
            .all()
        )


    def delete_panorama(
        self,
        panorama_id: int
    ):

        panorama = self.get_panorama_by_id(panorama_id)

        if panorama:

            self.session.delete(panorama)
            self.session.commit()

            return True

        return False