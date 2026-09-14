from abc import ABC, abstractmethod


class BaseImageCollector(ABC):

    @abstractmethod
    def download_image(
        self,
        panorama,
        output_directory
    ):
        """
        Download one image from a panorama.

        Returns
        -------
        ImageMetadata
        """
        pass