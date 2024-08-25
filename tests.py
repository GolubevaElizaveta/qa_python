from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_title_length_success(self):
        collector = BooksCollector()

        # Добавляем книгу с названием, длина которого меньше 41 символа
        collector.add_new_book('Хрупкое равновесие')

        # Проверяем, что книга добавилась
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_title_length_failure(self):
        collector = BooksCollector()

        # Добавляем книгу с названием, длина которого больше 40 символов
        collector.add_new_book('Удивительное путешествие Нильса Хольгерссона с дикими гусями по Швеции')

        # Проверяем, что книга не добавилась
        assert len(collector.get_books_genre()) == 0

    def test_set_existing_genre_success(self):
        collector = BooksCollector()

        # Добавляем книгу
        collector.add_new_book('1984')

        # Устанавливаем жанр для книги
        collector.set_book_genre('1984', 'Фантастика')

        # Проверяем, что жанр был установлен корректно
        assert collector.get_book_genre('1984') == 'Фантастика'

    def test_set_non_existing_genre_failure(self):
        collector = BooksCollector()

        # Добавляем книгу
        collector.add_new_book('1985')

        # Устанавливаем жанр для книги, который не в списке
        collector.set_book_genre('1985', 'Неверный жанр')

        # Проверяем, что жанр не был установлен
        assert collector.get_book_genre('1985') == ''  # Жанр должен остаться пустым

        # Добавляем книгу и устанавливаем жанр
    def test_get_book_genre_success(self):
        collector = BooksCollector()

        # Добавляем книгу и устанавливаем жанр
        collector.add_new_book('Смешные истории')
        collector.set_book_genre('Смешные истории', 'Комедии')  # Устанавливаем жанр 'Комедия'

        # Проверяем, что жанр книги возвращается корректно
        assert collector.get_book_genre('Смешные истории') == 'Комедии'

    def test_get_book_genre_failure(self):
        collector = BooksCollector()

        # Добавляем книгу, но не устанавливаем жанр
        collector.add_new_book('Преступление и наказание')

        # Проверяем, что метод возвращает пустую строку для несуществующей книги
        assert collector.get_book_genre('Несуществующая книга') is None

    def test_get_books_with_specific_genre_success(self):
        collector = BooksCollector()

        # Добавляем книги и устанавливаем их жанры
        collector.add_new_book('451° по Фаренгейту')
        collector.set_book_genre('451° по Фаренгейту', 'Фантастика')

        collector.add_new_book('Мертвые души')
        collector.set_book_genre('Мертвые души', 'Роман')

        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')

        # Проверяем, что метод возвращает правильный список книг с жанром 'Фантастика'
        assert collector.get_books_with_specific_genre('Фантастика') == ['451° по Фаренгейту', 'Дюна']

    def test_get_books_with_specific_genre_failure(self):
        collector = BooksCollector()

        # Добавляем книги и устанавливаем их жанры
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')

        collector.add_new_book('Преступление и наказание')
        collector.set_book_genre('Преступление и наказание', 'Роман')

        # Проверяем, что метод возвращает пустой список для жанра, для которого нет книг
        assert collector.get_books_with_specific_genre('Ужасы') == []

    def test_get_books_genre_success(self):
        collector = BooksCollector()

        # Добавляем книги и устанавливаем их жанры
        collector.add_new_book('Смешные истории')
        collector.set_book_genre('Смешные истории', 'Комедии')  # Устанавливаем жанр 'Комедия'

        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')  # Устанавливаем жанр 'Фантастика'

        # Проверяем, что метод возвращает правильный словарь с книгами и их жанрами
        expected_genre_dict = {
            'Смешные истории': 'Комедии',
            '1984': 'Фантастика'
        }
        assert collector.get_books_genre() == expected_genre_dict

    def test_get_books_genre_empty(self):
        collector = BooksCollector()

        # Проверяем, что метод возвращает пустой словарь, когда не добавлено ни одной книги
        assert collector.get_books_genre() == {}

    def test_get_books_for_children_success(self):
        collector = BooksCollector()

        # Добавляем книги и устанавливаем их жанры
        collector.add_new_book('Приключения Алисы в Стране Чудес')
        collector.set_book_genre('Приключения Алисы в Стране Чудес', 'Мультфильмы')  # Без возрастного рейтинга

        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Роман')  # С возрастным рейтингом

        collector.add_new_book('Муму')
        collector.set_book_genre('Муму', 'Детективы')  # С возрастным рейтингом

        # Проверяем, что метод возвращает правильный список книг, подходящих детям
        assert collector.get_books_for_children() == ['Приключения Алисы в Стране Чудес']

    def test_get_books_for_children_empty(self):
        collector = BooksCollector()

        # Добавляем книги и устанавливаем их жанры, все с возрастным рейтингом
        collector.add_new_book('Ужасы на улице Вязов')
        collector.set_book_genre('Ужасы на улице Вязов', 'Ужасы')  # С возрастным рейтингом

        collector.add_new_book('Детектив по вызову')
        collector.set_book_genre('Детектив по вызову', 'Детективы')  # С возрастным рейтингом

        # Проверяем, что метод возвращает пустой список для книг, неподходящих детям
        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()

        # Добавляем книгу
        collector.add_new_book('Гарри Поттер и философский камень')

        # Добавляем книгу в избранное
        collector.add_book_in_favorites('Гарри Поттер и философский камень')

        # Проверяем, что книга добавилась в избранное
        assert 'Гарри Поттер и философский камень' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_already_exists(self):
        collector = BooksCollector()

        # Добавляем книгу
        collector.add_new_book('Гарри Поттер и философский камень')

        # Добавляем книгу в избранное
        collector.add_book_in_favorites('Гарри Поттер и философский камень')

        # Пытаемся добавить книгу в избранное повторно
        collector.add_book_in_favorites('Гарри Поттер и философский камень')

        # Проверяем, что книга в избранном только один раз
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()

        # Добавляем книгу и добавляем её в избранное
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.add_book_in_favorites('Гарри Поттер и философский камень')

        # Удаляем книгу из избранного
        collector.delete_book_from_favorites('Гарри Поттер и философский камень')

        # Проверяем, что книга была удалена из избранного
        assert 'Гарри Поттер и философский камень' not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_not_in_favorites(self):
        collector = BooksCollector()

        # Добавляем книгу, но не добавляем её в избранное
        collector.add_new_book('Гарри Поттер и философский камень')

        # Пытаемся удалить книгу из избранного, хотя она там не находится
        collector.delete_book_from_favorites('Гарри Поттер и философский камень')

        # Проверяем, что список избранных книг остается пустым
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_success(self):
        collector = BooksCollector()

        # Добавляем книги и добавляем одну из них в избранное
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.add_book_in_favorites('Гарри Поттер и философский камень')

        collector.add_new_book('Война и мир')
        collector.add_book_in_favorites('Война и мир')

        # Проверяем, что метод возвращает правильный список избранных книг
        assert collector.get_list_of_favorites_books() == ['Гарри Поттер и философский камень', 'Война и мир']

    def test_get_list_of_favorites_books_empty(self):
        collector = BooksCollector()

        # Проверяем, что метод возвращает пустой список, когда избранное пусто
        assert collector.get_list_of_favorites_books() == []