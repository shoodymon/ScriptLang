surnames = [
    "Иванов", "Петров", "Сидоров", "Скворцов", "Глушаков", "Зинченко",
    "Потапов", "Слонов", "Дударь", "Кузнецов", "Попов", "Смирнов",
    "Морозов", "Волков", "Романов"
]

with open("task_37_surnames", "w", encoding="utf-8") as file:
    # i используется как начальный индекс для каждой группы из трех фамилий,
    # i+3 - как конечный индекс (не включается в срез).
    for i in range(0, len(surnames), 3):
        line = "-".join(surnames[i:i+3])
        file.write(line + "\n")

print("Файл с фамилиями преподавателей подгруппы успешно создан :)")