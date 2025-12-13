from abc import ABC, abstractmethod

class HeadLineBase(ABC):
    @abstractmethod
    def generate(self, title):
        pass