class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getXY(self):
        return [self.x, self.y]

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def show(self):
        print(f"Координаты точек ({self.x}, {self.y})")

if __name__ == "__main__":
    print("\nObj1 - (x;y)")
    obj1 = Point(1,3)
    obj1.show()

    print("\nObj2 - (x;y)")
    obj2 = Point(4, 2)
    obj2.show()

    print("\nObj3 - (x;y)")
    obj3 = obj1 + obj2
    obj3.show()