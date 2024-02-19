from abc import ABCMeta, abstractmethod


class ShapeInterface(metaclass=ABCMeta):
    @abstractmethod
    def area(self) -> int:
        """Calculate rectangle's area."""
