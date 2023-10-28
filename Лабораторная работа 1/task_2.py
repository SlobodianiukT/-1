# TODO Найдите количество книг, которое можно разместить на дискете
symbols_on_the_page = 25 * 50 * 4
symbols_in_the_book = symbols_on_the_page * 100
symbols_in_the_book_Mb = symbols_in_the_book / (1024 * 1024)
book_number = int(1.44/symbols_in_the_book_Mb)
print("Количество книг, помещающихся на дискету:", book_number)
