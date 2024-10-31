import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_start(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def getPoint(self):
        return [self.x, self.y]

class PointColor(Point):
    def __init__(self, x, y, color):
        super().__init__(x, y)
        self.color = color

    def getColor(self):
        return self.color


if __name__ == "__main__":
    print("\nObj1")
    obj1 = Point(3, 4)
    print(f"Координаты точки (х;у) - {obj1.getPoint()}")
    print(f"Расстояния от точки до начала координат = {obj1.distance_to_start()}")

    print("\nObj2")
    obj2 = PointColor(6, 8, "blue")
    print(f"Координаты точки (х;у) - {obj2.getPoint()}")
    print(f"Расстояния от точки до начала координат = {obj2.distance_to_start()}")
    print(f"Цвет точки - {obj2.getColor()}")