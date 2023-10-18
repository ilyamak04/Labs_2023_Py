amount_of_memory = 1.44 * 1024 * 1024
amount_of_page = 100
amount_of_string_in_page = 50
amount_of_char_in_string = 25
memory_for_char = 4

amount_of_book = amount_of_memory // \
                 (amount_of_page * amount_of_string_in_page *
                  amount_of_char_in_string * memory_for_char)

print("Количество книг, помещающихся на дискету:", int(amount_of_book))
