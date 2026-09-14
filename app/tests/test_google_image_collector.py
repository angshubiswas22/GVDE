import os

from app.collectors.google.google_image_collector import (
    GoogleImageCollector
)


def test_google_image_collector():

    collector = GoogleImageCollector()

    image_metadata = collector.download_image(
        panorama=None,
        output_directory="dataset/test"
    )

    print(image_metadata.file_path)
    print(image_metadata.width)
    print(image_metadata.height)

    assert os.path.exists(image_metadata.file_path)

    print("ImageMetadata returned successfully.")


if __name__ == "__main__":
    test_google_image_collector()