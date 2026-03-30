import json  # Импортируем библиотеку для работы с json-файлами


def task() -> float:
    with open('input.json') as file:  # Открываем файл с исходными данными (чтение по умолч.)
        data = json.load(file)  # Десериализуем данные из json-файла в объект Python

    # Записываем сумму (sum()) произведений значений словарей по ключам "score" и "weight"
    # Используем встроенный модуль List Comprehension для создания списка на основе итерируемой последовательности
    # (в 1 строку объединили цикл for с записью в список произведений):
    list_values = sum([(item["score"] * item["weight"]) for item in data])

    return round(list_values, 3)  # Возвращаем округлённое до 3-х знаков значение


print(task())  # Выводим результат выполнения функции task()
