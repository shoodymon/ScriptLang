x_val = int(input("x = "))

def square(x):
    return x ** 2

print(f"x^2 = {square(x_val)}")

elem_list = [11,2,32,47,5]

def get_element(lst, index):
    try:
        return f"Элемент списка {lst[index]} по индексу {index}"
    except IndexError:
        return f"Ошибка: Индекс {index} выходит за пределы списка."

print(elem_list)
print(get_element(elem_list, 4))

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Ошибка: Файл '{filename}' не найден."

print(read_file("test.txt"))

def get_positive_float():
    while True:
        try:
            num = float(input("Введите положительное дробное число: "))
            if num <= 0:
                raise ValueError("Число должно быть положительным.")
            return num
        except ValueError as e:
            print(f"Ошибка: {e}")

positive_num = get_positive_float()
print(f"Введено положительное число: {positive_num}")

def write_list_to_file(filename, lst):
    try:
        with open(filename, 'w') as file:
            for item in lst:
                file.write(str(item) + '\n')
        return "Список успешно записан в файл."
    except IOError:
        return f"Ошибка: Не удалось записать в файл '{filename}'."

print(write_list_to_file("output.txt", elem_list))

def find_item_in_list(lst, item):
    try:
        index = lst.index(item)
        return f"Элемент '{item}' найден на позиции {index}."
    except ValueError:
        return f"Элемент '{item}' не найден в списке."

print(find_item_in_list(elem_list, 11))
print(find_item_in_list(elem_list, 12))

def get_valid_password():
    while True:
        password = input("Введите пароль (минимум 6 символов, цифры и буквы): ")
        if len(password) < 6:
            print("Ошибка: Пароль должен содержать минимум 6 символов.")
        elif not any(char.isdigit() for char in password):
            print("Ошибка: Пароль должен содержать хотя бы одну цифру.")
        elif not any(char.isalpha() for char in password):
            print("Ошибка: Пароль должен содержать хотя бы одну букву.")
        else:
            return password

valid_password = get_valid_password()
print(f"Введён валидный пароль - {valid_password}")

dict_elem = {
    "A": 1,
    "B": 2,
    "C": 3,
}

def get_value_from_dict(data, key):
    try:
        return data[key]
    except KeyError:
        return f"Ошибка: ключ '{key}' не найден в словаре"

print(get_value_from_dict(dict_elem, "B"))
print(get_value_from_dict(dict_elem, "D"))

def custom_exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return f"Ошибка: {str(e)}"
    return wrapper

class NegativeNumberError(Exception):
    """Пользовательское исключение для отрицательных чисел."""
    pass

@custom_exception_handler
def divide(a, b):
    if b < 0:
        raise NegativeNumberError("Делитель не может быть отрицательным")
    return a / b

print(divide(10, 2))
print(divide(10, 0))
print(divide(10, -2))