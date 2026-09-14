from app.database.connection import SessionLocal
from app.repositories.source_repository import SourceRepository


def test_source_repository():

    session = SessionLocal()

    repo = SourceRepository(session)


    source = repo.create_source(
        name="Test Source",
        source_type="test"
    )


    print(
        source.id,
        source.name,
        source.source_type
    )


    session.close()


if __name__ == "__main__":
    test_source_repository()