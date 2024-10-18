import json


def load_phonebook():
    try:
        with open("phonebook.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# ensure_ascii позволяет сохранять кириллицу без экранирования
# indent - отступы
def save_phonebook(phonebook):
    with open("phonebook.json", "w", encoding="utf-8") as file:
        json.dump(phonebook, file, ensure_ascii=False, indent=2)


def search_by_number(phonebook, number):
    return [name for name, data in phonebook.items() if number in data["numbers"]]


def search_by_name(phonebook, name):
    return phonebook.get(name, None)


def add_contact(phonebook, name, number):
    if name not in phonebook:
        phonebook[name] = {"numbers": []}
    if number not in phonebook[name]["numbers"]:
        phonebook[name]["numbers"].append(number)


def delete_contact(phonebook, name):
    if name in phonebook:
        del phonebook[name]
        return True
    return False


def delete_number(phonebook, name, number):
    if name in phonebook and number in phonebook[name]["numbers"]:
        phonebook[name]["numbers"].remove(number)
        # Если у контакта не осталось номеров, удаляем весь контакт
        if not phonebook[name]["numbers"]:
            del phonebook[name]
        return True
    return False


def main():
    phonebook = load_phonebook()
    while True:
        print("\n1. Поиск по номеру")
        print("2. Поиск по имени")
        print("3. Добавить контакт")
        print("4. Удалить контакт")
        print("5. Удалить номер")
        print("6. Сохранить и выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            number = input("Введите номер: ")
            print(search_by_number(phonebook, number))
        elif choice == "2":
            name = input("Введите имя: ")
            print(search_by_name(phonebook, name))
        elif choice == "3":
            name = input("Введите имя: ")
            number = input("Введите номер: ")
            add_contact(phonebook, name, number)
        elif choice == "4":
            name = input("Введите имя для удаления: ")
            if delete_contact(phonebook, name):
                print("Контакт удален")
            else:
                print("Контакт не найден")
        elif choice == "5":
            name = input("Введите имя: ")
            number = input("Введите номер для удаления: ")
            if delete_number(phonebook, name, number):
                print("Номер удален")
            else:
                print("Номер не найден")
        elif choice == "6":
            save_phonebook(phonebook)
            print("Справочник сохранен")
            break
        else:
            print("Неверный выбор")


if __name__ == "__main__":
    main()