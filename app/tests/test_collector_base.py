from app.collectors.base_collector import BaseCollector



def test_base_collector():

    try:

        collector = BaseCollector()

        print("ERROR: BaseCollector should not instantiate")

    except TypeError:

        print("BaseCollector correctly enforced abstraction")



if __name__ == "__main__":
    test_base_collector()