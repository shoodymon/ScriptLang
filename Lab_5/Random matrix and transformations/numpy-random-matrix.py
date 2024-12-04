import numpy as np

# Настройки
X = 15; y = 6; K = 6; M = 15

def task7_random_matrix():
    # Задание 7: Создание случайной матрицы из нормального распределения
    random_matrix = np.random.normal(loc=0, scale=1.0, size=(3, 4))
    print("\nСлучайная матрица:\n", random_matrix)

    # Преобразование в одномерный массив
    flattened_matrix = random_matrix.flatten()
    print("Одномерный массив:\n", flattened_matrix)

def task8_matrix_operations():
    # Задание 8: Операции с матрицами
    A = np.arange(0, M+1)
    # Ошибка условия!
    C = A.reshape(4, 4)
    print("\nМатрица С:\n", C)

    # Транспонирование
    CT = C.T
    print("Матрица СТ:\n", CT)

    # Матричное умножение
    B = np.dot(C, CT)
    print("Матрица В:\n", B)

def task9_matrix_transposition():
    # Задание 9: Создание и транспонирование матрицы
    A = np.array([[2, 6], [3, 8], [4, 11], [5, 10], [6, 7]])
    print("\nМатрица А:\n", A)

    AT = A.T
    print("Транспонированная матрица АТ:\n", AT)

def main_random_matrix_tasks():
    task7_random_matrix()
    task8_matrix_operations()
    task9_matrix_transposition()

main_random_matrix_tasks()