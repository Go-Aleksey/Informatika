BYTES_ONE_CHAR = 4 # вес символа в байтах

disk_size = 1.44 # в мегабайтах
pages = 100
strings = 50
symbols = 25

count_of_numbers = int(disk_size // (pages * strings * symbols * BYTES_ONE_CHAR / 1024**2)) # поделили объём дискеты на вес
# всех символов книги в мегабайтах и привели к целочисленному формату

print("Количество книг, помещающихся на дискету:", count_of_numbers)
