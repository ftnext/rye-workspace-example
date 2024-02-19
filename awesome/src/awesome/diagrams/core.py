from awesome.diagrams.base import ShapeInterface


class AwesomeRectangle(ShapeInterface):
    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height = height

    def area(self) -> int:
        return self._width * self._height
