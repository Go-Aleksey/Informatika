list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

middle_index = len(list_players) // 2  # Нашли индекс середины

first_team = list_players[:middle_index]  # Взяли слайс первые полсписка
second_team = list_players[middle_index:]  # Взяли слайс вторые полсписка

print(first_team)
print(second_team)
