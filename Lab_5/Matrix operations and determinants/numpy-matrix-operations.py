import numpy as np

# Настройки
X = 15; y = 6; K = 6; M = 15

def task5_determinant_solve():
    # Задание 5: Вычисление детерминанта и решение систем линейных уравнений
    square_matrix = np.array([[1, 2], [3, 4]])
    determinant = np.linalg.det(square_matrix )
    print("\nДетерминант матрицы:", determinant)

    # Пример решения системы линейных уравнений
    coefficient_matrix = np.array([[1, 2], [3, 5]])
    constant_vector = np.array([1, 2])
    linear_system_solution = np.linalg.solve(coefficient_matrix, constant_vector)
    print("Решение системы линейных уравнений:", linear_system_solution)

def task6_array_transformations():
    # Задание 6: Создание массивов различной формы
    sequence_array = np.arange(K, K + X)
    print("\nОдномерный массив последовательности:", sequence_array)

    # Двумерные массивы
    # Убеждаемся, что reshape возможен
    if len(sequence_array) == 15:
        twodim_array_1 = sequence_array.reshape(5, 3)
        twodim_array_2 = sequence_array.reshape(3, 5)
        print("2D-массив 1:\n", twodim_array_1)
        print("2D-массив 2:\n", twodim_array_2)

        # Трехмерные массивы
        # Проверяем, что можно создать трехмерный массив
        try:
            threedim_array_1 = sequence_array.reshape(3, 5, 1)
            threedim_array_2 = sequence_array.reshape(5, 3, 1)
            print("3D-массив 1:\n", threedim_array_1)
            print("3D-массив 2:\n", threedim_array_2)
        except ValueError as e:
            print("Ошибка при создании 3D массива:", e)


def main_matrix_tasks():
    task5_determinant_solve()
    task6_array_transformations()


main_matrix_tasks()