from app.collectors.google.metadata_collector import GoogleMetadataCollector



def test_google_metadata_collector():

    collector = GoogleMetadataCollector()


    try:

        collector.collect(
            latitude=23.8103,
            longitude=90.4125
        )


    except NotImplementedError:

        print(
            "GoogleMetadataCollector structure ready"
        )



if __name__ == "__main__":
    test_google_metadata_collector()