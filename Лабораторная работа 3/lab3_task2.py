# Вводим функцию, принимающую две строки и необязательный разделитель (запятая по умолчанию)
def find_common_participants(first_group, second_group, separator=','):
    clear_first_group = first_group.split(separator)  # Разбили строку по разделителю методом split()
    clear_second_group = second_group.split(separator)  # Аналогично и для второй группы

    # Создаём список общих участников, поэтому использем list();
    # intersection работает с множествами, поэтому используем set():
    common_participants = list(set(clear_first_group).intersection(clear_second_group))
    common_participants.sort()  # Отсортировали полученный список по алфавиту

    return common_participants  # Возвращаем полученный список


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Проверяем функцию для нестандартного разделителя (|)
participants = find_common_participants(participants_first_group, participants_second_group, '|')
print('Общие участники:', participants)  # Выводим результат
