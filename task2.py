size_mb = 1.44
size_bytes = size_mb * 1024 * 1024
pages = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4
total = pages * lines_per_page * chars_per_line
book_size_bytes = total * bytes_per_char
books = int(size_bytes // book_size_bytes)
print("Количество книг, помещающихся на дискету:", books)
