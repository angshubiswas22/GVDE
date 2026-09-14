from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class PanoramaMetadata:

    source_name: str

    source_type: str

    source_panorama_id: str

    latitude: float

    longitude: float

    capture_time: Optional[str] = None

    heading: Optional[float] = None

    pitch: Optional[float] = None

    roll: Optional[float] = None

    images: List = field(
        default_factory=list
    )