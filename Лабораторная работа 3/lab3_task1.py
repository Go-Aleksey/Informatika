def searcher(fruits_list, fruit):  # Создали функцию, принимающую 2 аргумента
    for index, current_fruit in enumerate(fruits_list):  # Перебираем элементы пронумерованного списка
        if current_fruit is fruit:  # Проверяем, является ли фрукт из списка тем, который мы ищем
            return index  # Возвращаем индекс найденного товара


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = searcher(items_list, find_item)  # Вызвали созданую функцию
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
