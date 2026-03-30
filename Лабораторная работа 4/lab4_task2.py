import csv  # Импортируем модуль для работы с файлами csv
import json  # Импортируем модуль для работы с файлами json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as file:  # Открываем файл с исходными данными
        # Записываем в список словари, полученные из csv-строк методом DictReader
        # (DictReader возвращает каждую строку как словарь; перебирая циклом полученные словари, вносим их в список)
        # Используем List Comprehension, чтобы сделать это в 1 строку
        lines = [row for row in csv.DictReader(file)]

    # Открываем файл для записи результатов в режиме редактирования
    with open(OUTPUT_FILENAME, "w") as file:
        # Методом dump записываем данные в файл в формате json с отступами в 4 пробела
        json.dump(lines, file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
