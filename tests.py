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
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_get_book_rating_book_doesnt_exist_got_rating_is_none(self):
        collector = BooksCollector()
        assert collector.get_book_rating('Такой книги нет') is None

    def test_set_book_rating_rating_0_book_rating_is_1(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 0)
        assert collector.get_book_rating('Гордость и предубеждение и зомби')==1


    def test_get_books_with_rating_doesnt_exist_return_empty_list(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_rating('Гарри Поттер', 5)
        books_with_rating_3 = collector.get_books_with_specific_rating('3')
        assert len(books_with_rating_3) == 0


    def test_get_list_of_favorites_books_return_empty_list(self):
        collector = BooksCollector()
        favorites_count = len(collector.get_list_of_favorites_books())
        assert favorites_count == 0

    def test_add_book_in_favorites_return_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Мертвые души')
        collector.add_book_in_favorites('Мертвые души')
        assert ['Мертвые души'] not in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_add_nonexistent_book_favorite_books_list_empty(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Ревизор')
        assert "Ревизор" not in collector.get_list_of_favorites_books()


    def test_delete_book_from_favorites_add_and_delete_book_from_favorites_empty_favorite_list(self):
        collector = BooksCollector()
        collector.add_new_book('Вася')
        collector.add_book_in_favorites('Вася')
        collector.delete_book_from_favorites('Вася')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_delete_no_exists_book_from_favorites_empty_favorite_list(self):
        collector = BooksCollector()
        collector.delete_book_from_favorites('Вася')
        assert len(collector.get_list_of_favorites_books()) == 0
