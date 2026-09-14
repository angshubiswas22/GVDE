from dataclasses import dataclass
from typing import Optional


@dataclass
class ImageMetadata:

    file_path: str

    heading: Optional[float] = None

    pitch: Optional[float] = None

    field_of_view: Optional[float] = None

    width: Optional[int] = None

    height: Optional[int] = None

    image_hash: Optional[str] = None