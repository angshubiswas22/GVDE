from sqlalchemy.orm import Session

from app.database.models import Source


class SourceRepository:

    def __init__(self, session: Session):
        self.session = session


    def create_source(
        self,
        name,
        source_type,
        base_url=None,
        metadata_json=None
    ):
        source = Source(
            name=name,
            source_type=source_type,
            base_url=base_url,
            metadata_json=metadata_json
        )

        self.session.add(source)
        self.session.commit()
        self.session.refresh(source)

        return source


    def get_source_by_id(self, source_id):

        return (
            self.session.query(Source)
            .filter(Source.id == source_id)
            .first()
        )


    def get_source_by_name(self, name):

        return (
            self.session.query(Source)
            .filter(Source.name == name)
            .first()
        )


    def get_all_sources(self):

        return (
            self.session.query(Source)
            .all()
        )


    def delete_source(self, source_id):

        source = self.get_source_by_id(source_id)

        if source:
            self.session.delete(source)
            self.session.commit()

            return True

        return False
    