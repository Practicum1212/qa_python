from main import BooksCollector

# Первый тест

from conftest import collector


class TestBooksCollector:



    def test_add_new_book_add_the_same_book_once_true(self):

        collector.add_new_book('Преступление и наказание')
        collector.add_new_book('Преступление и наказание')

        assert len(collector.books_genre) == 1

# Второй тест :

    def test_add_book_and_add_genre_true(self):


        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')

        assert collector.books_genre == {'Шерлок Холмс': 'Детективы'}

    # Третий тест

    def test_list_contains_selected_books(self):
        book = 'Война и Мир'

        collector.add_new_book(book)
        collector.add_book_in_favorites(book)

        assert book in collector.get_list_of_favorites_books()

    # Четвёртый тест

    def test_list_contains_available_genre_true(self):


        for g in collector.genre:
            assert g in collector.genre

        collector.add_new_book("Новая книга")

        collector.set_book_genre("Новая книга", "Фантастика")

        assert collector.get_book_genre("Новая книга") == "Фантастика"

    # Пятый тест

    def test_list_contains_available_genre_true_age_rating_true():

        collector.add_new_book("Книга1")
        collector.set_book_genre("Книга1", "Фантастика")
        collector.add_new_book("Книга2")
        collector.set_book_genre("Книга2", "Ужасы")
        collector.add_new_book("Книга3")
        collector.set_book_genre("Книга3", "Комедии")

        books_for_children = collector.get_books_for_children()
        assert "Книга1" in books_for_children and "Книга3" in books_for_children and "Книга2" not in books_for_children

    # Шестой тест


    def test_set_book_genre():

        collector.add_new_book("Книга1")
        collector.set_book_genre("Книга1", "Фантастика")
        assert collector.books_genre["Книга1"] == "Фантастика"




# Седьмой тест

    def test_get_book_genre():

        collector.add_new_book("Книга2")
        collector.set_book_genre("Книга2", "Ужасы")
        assert collector.get_book_genre("Книга2") == "Ужасы"



# Восьмой тест




    def test_get_books_with_specific_genre():

        collector.books_genre = {"Книга1": "Фантастика", "Книга2": "Ужасы", "Книга3": "Детективы",
                                 "Книга4": "Мультфильмы"}
        genre = "Ужасы"
        expected_result = ["Книга2"]
        assert collector.get_books_with_specific_genre(genre) == expected_result

# Девятый тест




    def test_get_books_genre():

        collector.add_new_book("Книга1")
        collector.set_book_genre("Книга1", "Фантастика")
        collector.add_new_book("Книга2")
        collector.set_book_genre("Книга2", "Ужасы")
        expected_dict = {"Книга1": "Фантастика", "Книга2": "Ужасы"}
        assert collector.get_books_genre() == expected_dict

# Десятый тест




    def test_get_books_for_children():

        collector.books_genre = {"Книга1": "Фантастика", "Книга2": "Ужасы", "Книга3": "Мультфильмы",
                                 "Книга4": "Комедии"}
        assert collector.get_books_for_children() == ["Книга1", "Книга3", "Книга4"]

# 11 тест




    @pytest.mark.parametrize("name, expected", [
        ("Книга1", True),
        ("Книга2", True),
        ("ОченьДлинноеНазваниеКнигиКотороеПревышаетДопустимуюДлину", False),
        ("", False)
    ])
    def test_add_new_book(name, expected):

        collector.add_new_book(name)
        assert (name in collector.books_genre) == expected

# 12 тест



    @pytest.mark.parametrize("name, expected", [
        ("Книга1", True),
        ("Книга2", False),
    ])
    def test_add_book_in_favorites(name, expected):

        collector.add_new_book("Книга1")
        collector.add_new_book("Книга2")
        collector.add_book_in_favorites("Книга1")
        assert (name in collector.get_list_of_favorites_books()) == expected

# 13 тест




    def test_delete_book_from_favorites(self):

        collector.add_book_in_favorites("Книга1")
        collector.delete_book_from_favorites("Книга1")
        assert "Книга1" not in collector.favorites

# 14 тест:




    def test_get_list_of_favorites_books(self):

        collector.add_book_in_favorites("Книга1")
        collector.add_book_in_favorites("Книга2")
        expected_result = ["Книга1", "Книга2"]
        assert collector.get_list_of_favorites_books() == expected_result

# 15 тест




    def test_add_new_book_genre_is_empty():

        book_name = "Новая книга"
        collector.add_new_book(book_name)
        assert collector.get_book_genre(book_name) == ''