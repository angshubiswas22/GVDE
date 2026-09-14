from abc import ABC, abstractmethod


class BaseCollector(ABC):

    """
    Base interface for all GVDE collectors.
    Every collector must implement collect().
    """


    @abstractmethod
    def collect(self, *args, **kwargs):
        pass