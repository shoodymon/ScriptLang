appliances = ["Холодильник", "Стиральная машина", "Пылесос", "Микроволновка", "Посудомойка"]

with open("task_11_appliances", "w", encoding="utf-8") as file:
    file.write("-".join(appliances))

print("Файл бытовой техники успешно создан :)")