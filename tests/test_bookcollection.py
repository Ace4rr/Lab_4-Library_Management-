from book import Book
from bookcollection import BookCollection
import pytest 

@pytest.fixture
def sample_books():
    return [
        Book("A", "Author1", 2000, "Genre1", "ISBN-1"),
        Book("B", "Author2", 2001, "Genre2", "ISBN-2"),
        Book("C", "Author3", 2002, "Genre3", "ISBN-3"),]

def test_len_and_iter(sample_books):
    bc=BookCollection(sample_books)
    assert len(bc)==3
    titles=[b.title for b in bc]
    assert titles==["A", "B", "C"]

def test_getitem_index(sample_books):
    bc=BookCollection(sample_books)
    b=bc[0]
    assert isinstance(b, Book)
    assert b.title=="A"

def test_getitem_slice(sample_books):
    bc=BookCollection(sample_books)
    part=bc[1:3]
    assert isinstance(part, BookCollection)
    assert len(part)==2
    assert part[0].title=="B"

def test_add_book():
    bc=BookCollection()
    b=Book("A", "Author", 2000, "Genre", "ISBN-1")
    bc.add(b)
    assert len(bc)==1
    assert b in bc

def test_remove_by_isbn(sample_books):
    bc=BookCollection(sample_books)
    ok=bc.remove("ISBN-2")
    assert ok is True
    assert len(bc)==2
    assert "ISBN-2" not in bc

def test_remove_missing(sample_books):
    bc=BookCollection(sample_books)
    ok=bc.remove("ISBN-999")
    assert ok is False
    assert len(bc)==3

def test_contains(sample_books):
    bc=BookCollection(sample_books)
    assert "ISBN-1" in bc
    assert sample_books[0] in bc
    assert "ISBN-X" not in bc

def test_clear(sample_books):
    bc=BookCollection(sample_books)
    bc.clear()
    assert len(bc)==0

def test_add_collections(sample_books):
    bc1=BookCollection(sample_books[:2])
    bc2=BookCollection(sample_books[1:])
    merged=bc1 + bc2
    assert len(merged)==3