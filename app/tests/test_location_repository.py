from app.database.connection import SessionLocal
from app.repositories.location_repository import LocationRepository


def test_location_repository():

    session = SessionLocal()

    repo = LocationRepository(session)


    location = repo.create_location(
        latitude=23.8103,
        longitude=90.4125
    )


    print(
        location.id,
        location.latitude,
        location.longitude,
        location.point
    )


    session.close()


if __name__ == "__main__":
    test_location_repository()