from main import BooksCollector
import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    @pytest.fixture(autouse=True)
    def collector(self):
        self.collector = BooksCollector()

    @pytest.mark.parametrize('name', ['1', 'B' * 10, 'b' * 40])
    def test_add_new_book_valid_name(self, name):
        self.collector.add_new_book(name)
        assert self.collector.books_genre == {name: ''}

    @pytest.mark.parametrize('name', ['', 'b' * 41])
    def test_add_new_book_invalid_name(self, name):
        self.collector.add_new_book(name)
        assert self.collector.books_genre == {}

    @pytest.mark.parametrize('name', ['book1'])
    def test_set_book_genre_valid_genre(self, name):
        genre = self.collector.genre[0]
        self.collector.add_new_book(name)
        self.collector.set_book_genre(name, genre)
        assert self.collector.books_genre == {name: genre}

    @pytest.mark.parametrize('name', ['book1'])
    def test_set_book_genre_invalid_genre(self, name):
        genre = self.collector.genre[0] + '1'
        self.collector.add_new_book(name)
        self.collector.set_book_genre(name, genre)
        assert self.collector.books_genre == {name: ''}

    @pytest.mark.parametrize('name', ['book1'])
    def test_get_book_genre(self, name):
        genre = self.collector.genre[0]
        self.collector.add_new_book(name)
        self.collector.set_book_genre(name, genre)
        assert self.collector.get_book_genre(name) == genre

    @pytest.mark.parametrize('name', ['book1'])
    def test_get_books_genre(self, name):
        genre = self.collector.genre[0]
        self.collector.add_new_book(name)
        self.collector.set_book_genre(name, genre)
        assert self.collector.get_books_genre() == {name: genre}

    @pytest.mark.parametrize('name', ('book1', 'book2'))
    def test_get_books_with_specific_genre_valid_genre(self, name):
        self.collector.add_new_book(name[0])
        self.collector.set_book_genre(name[0], self.collector.genre[0])
        self.collector.add_new_book(name[1])
        self.collector.set_book_genre(name[1], self.collector.genre[1])
        assert self.collector.get_books_with_specific_genre(self.collector.genre[0]) == [name[0]]

    @pytest.mark.parametrize('name', ['book1'])
    def test_get_books_with_specific_genre_invalid_genre(self, name):
        genre = self.collector.genre[0] + '1'
        self.collector.add_new_book(name)
        self.collector.set_book_genre(name, genre)
        assert self.collector.get_books_with_specific_genre(genre) == []

    @pytest.mark.parametrize('name', ('book1', 'book2'))
    def test_get_books_for_children(self, name):
        self.collector.add_new_book(name[0])
        self.collector.set_book_genre(name[0], self.collector.genre[0])
        self.collector.add_new_book(name[1])
        self.collector.set_book_genre(name[1], self.collector.genre_age_rating[0])
        assert self.collector.get_books_for_children() == [name[0]]

    @pytest.mark.parametrize('name', ['book1'])
    def test_add_book_in_favorites_valid_book_name(self, name):
        self.collector.add_new_book(name)
        self.collector.add_book_in_favorites(name)
        assert self.collector.favorites == [name]
        # If book name already in favorites, there is no doubling
        self.collector.add_book_in_favorites(name)
        assert self.collector.favorites == [name]

    @pytest.mark.parametrize('name', ['book1'])
    def test_add_book_in_favorites_invalid_book_name(self, name):
        self.collector.add_new_book(name)
        self.collector.add_book_in_favorites(name + '1')
        assert self.collector.favorites == []

    @pytest.mark.parametrize('name', ['book1'])
    def test_delete_book_from_favorites_valid_book_name(self, name):
        self.collector.add_new_book(name)
        self.collector.add_book_in_favorites(name)
        assert self.collector.favorites == [name]
        self.collector.delete_book_from_favorites(name)
        assert self.collector.favorites == []

    @pytest.mark.parametrize('name', ['book1'])
    def test_delete_book_from_favorites_invalid_book_name(self, name):
        self.collector.add_new_book(name)
        self.collector.add_book_in_favorites(name)
        assert self.collector.favorites == [name]
        self.collector.delete_book_from_favorites(name + '1')
        assert self.collector.favorites == [name]

    @pytest.mark.parametrize('name', ['book1'])
    def test_get_list_of_favorites_books(self, name):
        self.collector.add_new_book(name)
        assert self.collector.get_list_of_favorites_books() == []
        self.collector.add_book_in_favorites(name)
        assert self.collector.get_list_of_favorites_books() == [name]
