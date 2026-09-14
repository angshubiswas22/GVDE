from app.collectors.base_collector import BaseCollector
import uuid


class GoogleMetadataCollector(BaseCollector):

    """
    Collector for Google Street View metadata.

    Responsible for retrieving and normalizing
    panorama metadata into GVDE format.
    """


    def __init__(self):

        pass



    def collect(
        self,
        latitude,
        longitude
    ):

        return {

            "pano_id": f"mock_{uuid.uuid4().hex}",

            "latitude": latitude,

            "longitude": longitude,

            "capture_time": "2026-07-27T00:00:00Z",

            "heading": 0.0,

            "pitch": 0.0,

            "roll": 0.0,

            "images": [
                {
                    "file_path": "dataset/test/mock_google_image.jpg",

                    "heading": 0.0,

                    "pitch": 0.0,

                    "field_of_view": 90.0,

                    "width": 1024,

                    "height": 512,

                    "image_hash": None
                }
            ]
        }