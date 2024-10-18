cities = ["Минск", "Гомель", "Витебск", "Могилев", "Гродно", "Брест"]

with open("task_29_cities", "w", encoding="utf-8") as file:
    file.write("\n".join(cities))

print("Файл с названиями городов Беларуси успешно создан :)")