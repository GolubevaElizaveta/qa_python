# qa_python

test_add_new_book_add_two_books - проверяем, что добавили именно 2 книги в коллекцию
test_add_new_book_title_length_success - добавляем книгу с названием, длина которого меньше 41 символа
test_add_new_book_title_length_failure - пытаемся добавить книгу с названием, длина которого больше 40 символов
test_set_existing_genre_success - проверяем, что жанр для книги устанавливается корректно
test_set_non_existing_genre_failure - пытаемся установить жанр не из списка
test_get_book_genre_success - проверяем, что установленный жанр возвращается корректно
test_get_book_genre_failure - проверяем, что метод возвращает пустую строку для книги без жанра
test_get_books_with_specific_genre_success - проверяем, что метод возвращает правильный список книг с жанром 'Фантастика'
test_get_books_with_specific_genre_failure - проверяем, что метод возвращает пустой список для жанра, для которого нет книг
test_get_books_genre_success - проверяем, что метод возвращает правильный словарь с книгами и их жанрами
test_get_books_genre_empty - проверяем, что метод возвращает пустой словарь, когда не добавлено ни одной книги
test_get_books_for_children_success - проверяем, что метод возвращает правильный список книг, подходящих детям
test_get_books_for_children_empty - проверяем, что метод возвращает пустой список для книг, неподходящих детям
test_add_book_in_favorites_success - проверяем, что книга добавилась в избранное
test_add_book_in_favorites_already_exists - проверяем, что книга в избранном только один раз
test_delete_book_from_favorites_success - проверяем, что книга была удалена из избранного
test_delete_book_from_favorites_not_in_favorites - проверяем, что список избранных книг остается пустым, хотя ее там и не было
test_get_list_of_favorites_books_success - проверяем, что метод возвращает правильный список избранных книг
test_get_list_of_favorites_books_empty - проверяем, что метод возвращает пустой список, когда избранное пусто
