import pandas as pd
import numpy as np


def task10_index_selection():
    # Задание 10: Выбор значения для определенного значения первого индекса серии
    series = pd.Series([10, 20, 30, 40, 50],
                       index=['a', 'b', 'c', 'd', 'e'])

    # Выбор значения по первому индексу
    result = series['b']
    print("Выбор по индексу 'b':", result)

    # Альтернативный способ
    result_alt = series.loc['b']
    print("Альтернативный выбор:", result_alt)


def task11_specific_value_selection():
    # Задание 11: Выбор конкретного значения серии
    series = pd.Series([10, 20, 30, 40, 50],
                       index=['a', 'b', 'c', 'd', 'e'])

    # Выбор конкретного значения
    result = series.iloc[2]
    print("Выбор третьего элемента:", result)

    # Дополнительный пример выбора
    result_alt = series.iat[2]
    print("Альтернативный выбор:", result_alt)


def task12_hierarchical_index_conversion():
    # Задание 12: Преобразование Series с иерархическими индексами в DataFrame
    multi_index_series = pd.Series(
        [1, 2, 3, 4, 5, 6],
        index=[['a', 'a', 'b', 'b', 'c', 'c'], [1, 2, 1, 2, 1, 2]]
    )

    print("Исходная Series с иерархическими индексами:\n", multi_index_series)

    # Преобразование в DataFrame с использованием unstack()
    df = multi_index_series.unstack()
    print("\nПреобразованный DataFrame:\n", df)


def main_pandas_tasks():
    print("\nЗадание 10: Выбор значения по индексу")
    task10_index_selection()

    print("\nЗадание 11: Выбор конкретного значения")
    task11_specific_value_selection()

    print("\nЗадание 12: Преобразование Series с иерархическими индексами")
    task12_hierarchical_index_conversion()


main_pandas_tasks()