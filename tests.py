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

    # Первый тест


class TestBooksCollector:

    def test_add_new_book_add_the_same_book_once_true(self):
        collector = BooksCollector()
        collector.add_new_book('Преступление и наказание')
        collector.add_new_book('Преступление и наказание')

        assert len(collector.books_genre) == 1

    # Второй тест :


class TestBooksCollector:

    def test_add_book_and_add_genre_true(self):
        collector = BooksCollector()
        collector.books_genre['Шерлок Холмс'] = 'Детективы'

        assert collector.books_genre == {'Шерлок Холмс': 'Детективы'}

    # Третий тест


class TestBooksCollector:

    def test_list_contains_selected_books(self):
        collector = BooksCollector()
        book = 'Война и Мир'
        collector.favorites.append(book)

        assert book in collector.favorites

    # Четвёртый тест


class TestBooksCollector:

    def test_list_contains_available_genre_true(self):
        collector = BooksCollector()
        genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

        for g in genre:
            assert g in collector.genre

    # Пятый тест


class TestBooksCollector:

    def test_list_contains_available_genre_true_age_rating_true(self):
        collector = BooksCollector()
        genre_age_rating = ['Ужасы', 'Детективы']

        assert collector.genre_age_rating == genre_age_rating

    # Шестой тест


class TestBooksCollector:

    def test_set_book_genre():
        collector = BooksCollector()
        collector.add_new_book("Книга1")
        collector.set_book_genre("Книга1", "Фантастика")
        assert collector.get_book_genre("Книга1") == "Фантастика"

    # Седьмой тест


class TestBooksCollector:

    def test_get_book_genre():
        collector = BooksCollector()
        collector.add_new_book("Книга1")
        collector.set_book_genre("Книга1", "Фантастика")
        assert collector.get_book_genre("Книга1") == "Фантастика"

    # Восьмой тест


class TestBooksCollector:

    def test_get_books_with_specific_genre():
        collector = BooksCollector()
        collector.books_genre = {"Книга1": "Фантастика", "Книга2": "Ужасы", "Книга3": "Детективы",
                                 "Книга4": "Мультфильмы"}
        genre = "Ужасы"
        expected_result = ["Книга2"]
        assert collector.get_books_with_specific_genre(genre) == expected_result

    # Девятый тест


class TestBooksCollector:

    def test_get_books_genre():
        collector = BooksCollector()
        collector.add_new_book("Книга1")
        collector.set_book_genre("Книга1", "Фантастика")
        collector.add_new_book("Книга2")
        collector.set_book_genre("Книга2", "Ужасы")
        expected_dict = {"Книга1": "Фантастика", "Книга2": "Ужасы"}
        assert collector.get_books_genre() == expected_dict

    # Десятый тест


class TestBooksCollector:

    def test_get_books_for_children():
        collector = BooksCollector()
        collector.books_genre = {"Книга1": "Фантастика", "Книга2": "Ужасы", "Книга3": "Мультфильмы",
                                 "Книга4": "Комедии"}
        assert collector.get_books_for_children() == ["Книга1", "Книга3", "Книга4"]

    # 11 тест


class TestBooksCollector:

    @pytest.mark.parametrize("name, expected", [
        ("Книга1", True),
        ("Книга2", True),
        ("ОченьДлинноеНазваниеКнигиКотороеПревышаетДопустимуюДлину", False),
        ("", False)
    ])
    def test_add_new_book(name, expected):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert (name in collector.books_genre) == expected

    # 12 тест


class TestBooksCollector:
    @pytest.mark.parametrize("name, expected", [
        ("Книга1", True),
        ("Книга2", False),
    ])
    def test_add_book_in_favorites(name, expected):
        collector = BooksCollector()
        collector.add_new_book("Книга1")
        collector.add_new_book("Книга2")
        collector.add_book_in_favorites("Книга1")
        assert (name in collector.get_list_of_favorites_books()) == expected

    # 13 тест


class TestBooksCollector:

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_book_in_favorites("Книга1")
        collector.delete_book_from_favorites("Книга1")
        assert "Книга1" not in collector.favorites

    # 14 тест:


class TestBooksCollector:

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_book_in_favorites("Книга1")
        collector.add_book_in_favorites("Книга2")
        expected_result = ["Книга1", "Книга2"]
        assert collector.get_list_of_favorites_books() == expected_result

    # 15 тест


class TestBooksCollector:

    def test_add_new_book_genre_is_empty():
        collector = BooksCollector()
        book_name = "Новая книга"
        collector.add_new_book(book_name)
        assert collector.get_book_genre(book_name) == ''