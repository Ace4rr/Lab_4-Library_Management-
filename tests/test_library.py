import pytest
from book import Book
from library import Library

@pytest.fixture
def library_with_books():
    lib=Library()
    lib.add_book(Book("A", "Author1", 2000, "Genre1", "ISBN-1"))
    lib.add_book(Book("B", "Author1", 2001, "Genre2", "ISBN-2"))
    lib.add_book(Book("C", "Author2", 2000, "Genre1", "ISBN-3"))
    return lib

def test_add_book(library_with_books):
    lib=library_with_books
    assert lib.get_book("ISBN-1") is not None

def test_remove_book(library_with_books):
    lib=library_with_books
    ok=lib.remove_book("ISBN-2")
    assert ok is True
    assert lib.get_book("ISBN-2") is None

def test_find_by_author(library_with_books):
    res=library_with_books.find_by_author("Author1")
    assert len(res)==2

def test_find_by_year(library_with_books):
    res=library_with_books.find_by_year(2000)
    assert len(res)==2

def test_find_by_genre(library_with_books):
    res=library_with_books.find_by_genre("Genre1")
    assert len(res)==2

def test_rebuild_index(library_with_books):
    library_with_books.rebuild_index()
    assert library_with_books.get_book("ISBN-1") is not None