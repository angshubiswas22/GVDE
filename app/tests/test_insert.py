from app.database.connection import SessionLocal
from app.database.models import Panorama


db = SessionLocal()


try:
    panorama = Panorama(
        source_provider="test",
        source_id="dhaka_001",
        image_path="images/test.jpg",
        location="SRID=4326;POINT(90.4125 23.8103)"
    )

    db.add(panorama)
    db.commit()
    db.refresh(panorama)

    print("Inserted panorama:")
    print("ID:", panorama.id)
    print("Source ID:", panorama.source_id)

finally:
    db.close()