import os

from PIL import Image

from app.collectors.base_image_collector import BaseImageCollector
from app.schemas.image_schema import ImageMetadata


class GoogleImageCollector(BaseImageCollector):

    def download_image(
    self,
    panorama,
    output_directory
    ):

        os.makedirs(
            output_directory,
            exist_ok=True
        )

        file_name = "mock_google_image.jpg"

        file_path = os.path.join(
            output_directory,
            file_name
        )

        image = Image.new(
            mode="RGB",
            size=(1024, 512),
            color=(120, 180, 255)
        )

        image.save(
            file_path,
            format="JPEG"
        )

        return ImageMetadata(
            file_path=file_path,
            heading=None,
            pitch=None,
            field_of_view=None,
            width=1024,
            height=512,
            image_hash=None
        )
