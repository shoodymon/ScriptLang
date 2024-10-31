class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_valid_triangle(self):
        return (self.a + self.b > self.c and
                self.a + self.c > self.b and
                self.b + self.c > self.a)

    def perimeter(self):
        return self.a + self.b + self.c

    def check_triangle(self):
        if self.is_valid_triangle():
            print("Треугольник можно построить")
            print(f"Периметр треугольника = {self.perimeter()}")
        else:
            print("Треугольник нельзя построить")

class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)

    def check_triangle(self):
        if self.is_valid_triangle():
            print("Можно построить треугольник!")
            print("Это равносторонний треугольник!")
            print(f"Периметр треугольника = {self.perimeter()}")
        else:
            print("Треугольник не сделать из этого")

if __name__ == "__main__":
    print("\nТреугольник 3-4-5")
    obj_tr1 = Triangle(3, 4, 5)
    obj_tr1.check_triangle()

    print("\nТреугольник 4-4-9")
    obj_tr2 = Triangle(4, 4, 9)
    obj_tr2.check_triangle()

    print("\nТреугольник 5-5-5")
    obj_tr3 = EquilateralTriangle(5)
    obj_tr3.check_triangle()