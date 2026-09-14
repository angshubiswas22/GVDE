from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey,
    Text,
    Table
)

from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from geoalchemy2 import Geography

from .connection import Base

collection_images = Table(
    "collection_images",
    Base.metadata,

    Column(
        "collection_id",
        Integer,
        ForeignKey("collections.id"),
        primary_key=True
    ),

    Column(
        "image_id",
        Integer,
        ForeignKey("images.id"),
        primary_key=True
    )
)


class Source(Base):
    __tablename__ = "sources"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String,
        nullable=False
    )

    source_type = Column(
        String,
        nullable=False
    )

    base_url = Column(
        String,
        nullable=True
    )

    metadata_json = Column(
        JSONB,
        nullable=True
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )


    panoramas = relationship(
        "Panorama",
        back_populates="source"
    )



class Location(Base):
    __tablename__ = "locations"

    id = Column(
        Integer,
        primary_key=True
    )

    latitude = Column(
        Float,
        nullable=False
    )

    longitude = Column(
        Float,
        nullable=False
    )

    point = Column(
        Geography(
            geometry_type="POINT",
            srid=4326
        ),
        nullable=False
    )

    country = Column(
        String,
        nullable=True
    )

    region = Column(
        String,
        nullable=True
    )

    city = Column(
        String,
        nullable=True
    )

    metadata_json = Column(
        JSONB,
        nullable=True
    )


    panoramas = relationship(
        "Panorama",
        back_populates="location"
    )



class Panorama(Base):
    __tablename__ = "panoramas"

    id = Column(
        Integer,
        primary_key=True
    )

    location_id = Column(
        Integer,
        ForeignKey("locations.id"),
        nullable=False
    )

    source_id = Column(
        Integer,
        ForeignKey("sources.id"),
        nullable=False
    )

    source_panorama_id = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    capture_time = Column(
        DateTime(timezone=True),
        nullable=True
    )

    heading = Column(
        Float,
        nullable=True
    )

    pitch = Column(
        Float,
        nullable=True
    )

    roll = Column(
        Float,
        nullable=True
    )

    width = Column(
        Integer,
        nullable=True
    )

    height = Column(
        Integer,
        nullable=True
    )

    metadata_json = Column(
        JSONB,
        nullable=True
    )


    location = relationship(
        "Location",
        back_populates="panoramas"
    )


    source = relationship(
        "Source",
        back_populates="panoramas"
    )


    images = relationship(
        "Image",
        back_populates="panorama"
    )



class Image(Base):
    __tablename__ = "images"

    id = Column(
        Integer,
        primary_key=True
    )

    panorama_id = Column(
        Integer,
        ForeignKey("panoramas.id"),
        nullable=False
    )

    file_path = Column(
        String,
        nullable=False
    )

    heading = Column(
        Float,
        nullable=True
    )

    pitch = Column(
        Float,
        nullable=True
    )

    field_of_view = Column(
        Float,
        nullable=True
    )

    width = Column(
        Integer,
        nullable=True
    )

    height = Column(
        Integer,
        nullable=True
    )

    image_hash = Column(
        String,
        nullable=True,
        index=True
    )

    metadata_json = Column(
        JSONB,
        nullable=True
    )


    panorama = relationship(
        "Panorama",
        back_populates="images"
    )


    collections = relationship(
    "Collection",
    secondary=collection_images,
    back_populates="images"
    )



class PanoramaNeighbor(Base):
    __tablename__ = "panorama_neighbors"

    id = Column(
        Integer,
        primary_key=True
    )

    panorama_id = Column(
        Integer,
        ForeignKey("panoramas.id"),
        nullable=False
    )

    neighbor_id = Column(
        Integer,
        ForeignKey("panoramas.id"),
        nullable=False
    )

    distance_meters = Column(
        Float,
        nullable=True
    )

    direction = Column(
        String,
        nullable=True
    )

    metadata_json = Column(
        JSONB,
        nullable=True
    )



class Collection(Base):
    __tablename__ = "collections"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String,
        nullable=False
    )

    version = Column(
        String,
        nullable=False
    )

    description = Column(
        Text,
        nullable=True
    )

    sampling_strategy = Column(
        JSONB,
        nullable=True
    )

    metadata_json = Column(
        JSONB,
        nullable=True
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    images = relationship(
    "Image",
    secondary=collection_images,
    back_populates="collections"
    )