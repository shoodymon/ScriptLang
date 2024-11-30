import random

rows = 45 - 20
seats_per_row = 15

# Создаем файл со случайной занятостью мест
with open("task_53_auditorium.txt", "w") as file:
    # Значение этой переменной не будет использоваться в теле цикла
    # Выполняем цикл определенное количество раз, но нам не важно текущее значение счетчика
    # В цикле - нам важно только количество итераций, но не конкретное значение счетчика
    # В генераторе списка - нам важно только количество сгенерированных символов, а не их индексы
    for _ in range(rows):
        row = ''.join(random.choice("01") for _ in range(seats_per_row))
        file.write(row + "\n")

def count_free_seats():
    with open("task_53_auditorium.txt", "r") as file:
        return sum(row.count('0') for row in file)

def check_seat(row, seat):
    with open("task_53_auditorium.txt", "r") as file:
        seats = file.readlines()
    # Проверка корректности введенных ряда и места
    # 1 <= row <= len(seats) - проверка, что ряд существует
    # 1 <= seat <= len(seats[0].strip()) - проверка, что место существует
    # len(seats) - общее количество рядов
    # len(seats[0].strip()) - количество мест в ряду (убираем '\n' в конце строки)
    if 1 <= row <= len(seats) and 1 <= seat <= len(seats[0].strip()):
        # seats[row-1] - выбираем нужный ряд (индексация с 0, поэтому row-1)
        # [seat-1] - выбираем нужное место в ряду
        # seats[row-1][seat-1] == '0' - проверка, свободно ли место
        return "Свободно" if seats[row-1][seat-1] == '0' else "Занято"
    else:
        return "Некорректный номер места"

# Основной цикл программы
while True:
    print(f"\nСвободных мест: {count_free_seats()}")
    choice = input("Введите номер ряда и места через пробел (или 'q' для выхода): ")
    if choice.lower() == 'q':
        break
    try:
        # map(int, ...) - преобразование каждого элемента в целое число
        # map() - замена for для каждого элемента итерируемого объекта
        row, seat = map(int, choice.split())
        print(f"Место {row}-{seat}: {check_seat(row, seat)}")
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите два числа, разделенные пробелом.")
