import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        # Добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # Проверяем, что добавилось именно две
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize("title", [
        'A' * 40,  # 40 символов
        'Книга с заглавием'  # менее 40 символов
    ])
    def test_add_new_book_title_length_success(self, title):
        collector = BooksCollector()
        collector.add_new_book(title)
        assert title in collector.get_books_genre()  # Проверяем, что книга добавлена

    @pytest.mark.parametrize("title", [
        'A' * 41,  # 41 символ
        'Заглавие, которое слишком длинное и не должно быть добавлено в коллекцию книг'  # более 40 символов
    ])
    def test_add_new_book_title_length_failure(self, title):
        collector = BooksCollector()
        collector.add_new_book(title)
        assert title not in collector.get_books_genre()  # Проверяем, что книга не добавлена

    @pytest.mark.parametrize("book_name, genre, expected", [
        ('Книга 1', 'Фантастика', 'Фантастика'),
        ('Книга 1', 'Не существующий жанр', '')
    ])
    def test_set_book_genre(self, book_name, genre, expected):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == expected

    @pytest.mark.parametrize("book_name, expected", [
        ('Книга 1', None),  # не добавлена
        ('Книга 2', None),  # несуществующая
        ('Книга 3', 'Фантастика'),  # успешно добавлена
    ])
    def test_get_book_genre(self, book_name, expected):
        collector = BooksCollector()
        if book_name == 'Книга 3':
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, 'Фантастика')
        assert collector.get_book_genre(book_name) == expected

    @pytest.mark.parametrize("genre, expected_count", [
        ('Фантастика', 2),  # две книги в жанре "Фантастика"
        ('Не существующий жанр', 0)  # ничего нет
    ])
    def test_get_books_with_specific_genre(self, genre, expected_count):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.set_book_genre('Книга 1', 'Фантастика')
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 2', 'Фантастика')
        books = collector.get_books_with_specific_genre(genre)
        assert len(books) == expected_count

    @pytest.mark.parametrize("book_name, genre, expected_count", [
        ('Книга для детей', 'Фантастика', 1),  # подходит для детей
        ('Книга для взрослых', 'Ужасы', 0)      # не подходит для детей
    ])
    def test_get_books_for_children(self, book_name, genre, expected_count):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        books = collector.get_books_for_children()
        assert len(books) == expected_count

    @pytest.mark.parametrize("book_name, should_be_favorite", [
        ('Книга 1', True),  # добавляем в избранное
        ('Не существующая книга', False)  # несуществующая книга
    ])
    def test_add_book_in_favorites(self, book_name, should_be_favorite):
        collector = BooksCollector()
        if should_be_favorite:
            collector.add_new_book(book_name)
            collector.add_book_in_favorites(book_name)
            assert book_name in collector.get_list_of_favorites_books()
        else:
            collector.add_book_in_favorites(book_name)
            assert book_name not in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize("book_name, should_exist", [
        ('Книга 1', True),  # удаляем из избранного
        ('Не существующая книга', False)  # несуществующая книга
    ])
    def test_delete_book_from_favorites(self, book_name, should_exist):
        collector = BooksCollector()
        if should_exist:
            collector.add_new_book(book_name)
            collector.add_book_in_favorites(book_name)  # добавляем в избранное
            collector.delete_book_from_favorites(book_name)
            assert book_name not in collector.get_list_of_favorites_books()  # проверяем удаление
        else:
            collector.delete_book_from_favorites(book_name)
            assert len(collector.get_list_of_favorites_books()) == 0  # избранное должно быть пустым

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_book_in_favorites('Книга 1')  # добавляем в избранное
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 1  # ожидаем одну книгу в избранном

    def test_get_list_of_favorites_books_empty(self):
        collector = BooksCollector()
        favorites = collector.get_list_of_favorites_books()
        assert favorites == []  # ожидаем, что избранное пустое
