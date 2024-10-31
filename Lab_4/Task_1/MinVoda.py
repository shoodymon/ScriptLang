class MinVoda:
    def __init__(self, water_type=None):
        self.water_type = water_type

    def show_my_drink(self):
        if self.water_type:
            print(f"Минеральная вода – {self.water_type}")
        else:
            print("Обычная минеральная вода")

if __name__ == "__main__":
    obj1 = MinVoda("тип1")
    obj1.show_my_drink()

    obj2 = MinVoda("тип2")
    obj2.show_my_drink()

    obj3 = MinVoda()
    obj3.show_my_drink()