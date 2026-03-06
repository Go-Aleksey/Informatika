numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index_missing_item = 4 # нашли пропущенный элемент

numbers[index_missing_item] = (sum(numbers[:index_missing_item] + numbers[index_missing_item+1:])) / len(numbers) # Заменили None на среднее арифметическое

print("Измененный список:", numbers)
