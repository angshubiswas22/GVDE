from app.database.connection import SessionLocal
from app.repositories.panorama_repository import PanoramaRepository


def test_panorama_repository():

    session = SessionLocal()

    repo = PanoramaRepository(session)


    panorama = repo.create_panorama(
        location_id=1,
        source_id=1,
        source_panorama_id="test_panorama_001",
        heading=90.0,
        pitch=0.0,
        roll=0.0,
        width=4096,
        height=2048
    )


    print(
        panorama.id,
        panorama.source_panorama_id,
        panorama.location_id,
        panorama.source_id
    )


    session.close()


if __name__ == "__main__":
    test_panorama_repository()