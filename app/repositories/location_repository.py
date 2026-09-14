from sqlalchemy.orm import Session
from geoalchemy2 import WKTElement

from app.database.models import Location


class LocationRepository:

    def __init__(self, session: Session):
        self.session = session


    def create_location(
        self,
        latitude: float,
        longitude: float
    ):

        point = WKTElement(
            f"POINT({longitude} {latitude})",
            srid=4326
        )


        location = Location(
            latitude=latitude,
            longitude=longitude,
            point=point
        )


        self.session.add(location)
        self.session.commit()
        self.session.refresh(location)

        return location


    def get_location_by_id(
        self,
        location_id: int
    ):

        return (
            self.session.query(Location)
            .filter(Location.id == location_id)
            .first()
        )


    def get_all_locations(self):

        return (
            self.session.query(Location)
            .all()
        )


    def delete_location(
        self,
        location_id: int
    ):

        location = self.get_location_by_id(location_id)

        if location:

            self.session.delete(location)
            self.session.commit()

            return True

        return False