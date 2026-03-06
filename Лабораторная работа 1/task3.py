list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
middle_index = len(list_players) // 2 # нашли индекс середины

first_team = list_players[:middle_index] # первая команда - от начала до середины, т е взяли слайс полсписка
second_team = list_players[middle_index:] # вторая команда - с середины до конца, т е взяли слайс вторых полсписка

print(first_team)
print(second_team)
