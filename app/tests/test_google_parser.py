from app.collectors.google.parser import parse_panorama_metadata


def test_google_parser():

    raw_google_data = {

        "pano_id": "google_test_001",

        "latitude": 23.8103,

        "longitude": 90.4125,

        "heading": 90.0,

        "pitch": 0.0,

        "roll": 0.0,

        "images": [
            {
                "file_path": "test/image.jpg"
            }
        ]
    }


    result = parse_panorama_metadata(
        raw_google_data
    )


    print(result)


    assert result.source_panorama_id == "google_test_001"

    assert result.latitude == 23.8103

    assert result.source_name == "Google Street View"

    assert len(result.images) == 1

    assert result.images[0].file_path == "test/image.jpg"



if __name__ == "__main__":
    test_google_parser()