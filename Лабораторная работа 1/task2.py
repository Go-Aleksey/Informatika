BYTES_ONE_CHAR = 4  # Вес одного символа в байтах

disk_size = 1.44  # Размер дискеты в мегабайтах
pages = 100
strings = 50
symbols = 25

book_size = pages * strings * symbols * BYTES_ONE_CHAR  # Вес книги в байтах

# Делим объём дискеты в мегабайтах на размер одной книги в мегабайтах
count_of_books = int(disk_size // (book_size / 1024**2))

print("Количество книг, помещающихся на дискету:", count_of_books)
