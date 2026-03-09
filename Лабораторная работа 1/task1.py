numbers = [
    2, -93, -2, 8, None, -44, -1, -85, -14, 90,
    -22, -90, -100, -8, 38, -92, -45, 67, 53, 25
    ]

index_missing_item = 4  # Нашли номер пропущенного элемента

sum_of_numbers = sum(numbers[:index_missing_item] + numbers[index_missing_item+1:])
count_of_numbers = len(numbers)  # Нашли количество элементов всего списка

# Заменяем None на среднее арифметическое
numbers[index_missing_item] = sum_of_numbers / count_of_numbers

print("Измененный список:", numbers)
