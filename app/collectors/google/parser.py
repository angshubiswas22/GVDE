from app.schemas.panorama_schema import PanoramaMetadata
from app.schemas.image_schema import ImageMetadata



def parse_panorama_metadata(raw_data):

    images = []

    for image in raw_data.get("images", []):

        images.append(
            ImageMetadata(
                file_path=image.get("file_path"),

                heading=image.get("heading"),

                pitch=image.get("pitch"),

                field_of_view=image.get(
                    "field_of_view"
                ),

                width=image.get("width"),

                height=image.get("height"),

                image_hash=image.get(
                    "image_hash"
                )
            )
        )


    return PanoramaMetadata(

        source_name="Google Street View",

        source_type="street_view",

        source_panorama_id=raw_data.get(
            "pano_id"
        ),

        latitude=raw_data.get(
            "latitude"
        ),

        longitude=raw_data.get(
            "longitude"
        ),

        capture_time=raw_data.get(
            "capture_time"
        ),

        heading=raw_data.get(
            "heading"
        ),

        pitch=raw_data.get(
            "pitch"
        ),

        roll=raw_data.get(
            "roll"
        ),

        images=images
    )