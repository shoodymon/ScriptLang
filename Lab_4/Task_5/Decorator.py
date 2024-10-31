# def cache_decorator_function(func):
#
#     def wrapper():
#         print("Функция-обёртка")
#         print("Оборачиваемая функция: {}".format(func))
#         print("Выполняем обёрнутую функцию...")
#         func()
#         print("Выходим из обёртки")
#     return wrapper
#
# @cache_decorator_function
# def hello():
#     print("hello")
#
# hello()

# def cache_decorator(func):
#     cache = None
#     counter = 0
#
#     def wrapper(*args, **kwargs):
#         nonlocal cache, counter
#         # Без инструкции nonlocal программа считала бы
#         # cache и counter локальными переменными wrapper --> ошибка при попытке изменения
#
#         if counter >= 3 or cache is None:
#             cache = func(*args, **kwargs)
#             counter = 0
#
#         counter += 1
#         print (f"Вычисление {counter}")
#         return cache
#
#     return wrapper
#
# @cache_decorator
# def comp(n):
#     print("Выполнение сложного вычисления...")
#     return sum(range(n))
#
# if __name__ == "__main__":
#     print("\nВ буфер помещается 3 вычисления")
#     print(comp(1000))
#     print(comp(1000))
#     print(comp(1000))
#     print(comp(1000))
#     print(comp(1000))

def create_cache_decorator(buffer_size=3):
    def decorator(func):
        state = {
            'cache': None,
            'counter': 0
        }

        def wrapper(*args, **kwargs):
            if state['counter'] >= buffer_size or state['cache'] is None:
                if state['cache'] is not None:
                    print(f"Буфер на {buffer_size} вычисления переполнен!")
                print("\nВыполняется сложное вычисление...")
                state['cache'] = func(*args, **kwargs)
                state['counter'] = 0

            state['counter'] += 1
            print(f"Использование кеша. Попытка {state['counter']} из {buffer_size}")
            return state['cache']

        return wrapper

    return decorator


@create_cache_decorator(buffer_size=3)
def computation(n):
    return sum(range(n))

if __name__ == "__main__":
    print("\nТестирование функции-декоратора:")
    print("Результат:", computation(1000))
    print("Результат:", computation(1000))
    print("Результат:", computation(1000))
    print("Результат:", computation(1000))