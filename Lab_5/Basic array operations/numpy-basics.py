import numpy as np

# Настройки
X = 15; y = 6; K = 6; M = 15

def task_1_2_3():
    # Задание 1: Создание вектора из нулей
    vec_zeros = np.zeros(X)
    print("\nВектор из нулей: ", vec_zeros)

    # Задание 2: Создание вектора из единиц
    vec_ones = np.ones(X)
    print("\nВектор из единиц: ", vec_ones)

    # Задание 3: Создание вектора с определенными значениями
    spec_vec = np.zeros(X)
    spec_vec[y + 2] = X
    spec_vec[y + 5] = X
    print("\nСпециальный вектор: ", spec_vec)

def task_4():
    # Задание 4: Изменение знаков элементов в массиве
    arr = np.arange(20)
    print("\nМассив: ", arr)
    arr[(arr >= K) & (arr <= M)] *= -1
    print("Массив с измененными знаками: ", arr)

def main_numpy_tasks():
    task_1_2_3()
    task_4()

main_numpy_tasks()