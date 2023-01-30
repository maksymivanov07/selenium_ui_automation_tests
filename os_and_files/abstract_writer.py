from abc import ABC, abstractmethod


class Writer(ABC):

    @abstractmethod
    def write_file(self):
        pass
