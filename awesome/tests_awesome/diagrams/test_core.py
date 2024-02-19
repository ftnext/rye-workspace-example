from awesome.diagrams.core import AwesomeRectangle


def test_長方形の面積を計算できる() -> None:
    rectangle = AwesomeRectangle(5, 6)
    assert rectangle.area() == 30
