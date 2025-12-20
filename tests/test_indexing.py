import pytest
from book import Book
from indexing import IndexDict

@pytest.fixture
def sample_books():
    return [
        Book("A", "Author1", 2000, "Genre1", "ISBN-1"),
        Book("B", "Author1", 2001, "Genre2", "ISBN-2"),
        Book("C", "Author2", 2000, "Genre3", "ISBN-3")]

def test_add_and_search_by_isbn(sample_books):
    idx=IndexDict()
    idx.add(sample_books[0])
    book=idx.search_by_isbn("ISBN-1")
    assert book is sample_books[0]

def test_search_by_author(sample_books):
    idx=IndexDict()
    for b in sample_books:
        idx.add(b)
    res=idx.search_by_author("Author1")
    assert len(res)==2
    assert all(b.author=="Author1" for b in res)

def test_search_by_year(sample_books):
    idx=IndexDict()
    for b in sample_books:
        idx.add(b)
    res=idx.search_by_year(2000)
    assert len(res)==2
    assert all(b.year==2000 for b in res)

def test_remove_book(sample_books):
    idx=IndexDict()
    for b in sample_books:
        idx.add(b)
    idx.remove("ISBN-2")
    assert idx.search_by_isbn("ISBN-2") is None
    assert len(idx.search_by_author("Author1"))==1

def test_clear(sample_books):
    idx=IndexDict()
    for b in sample_books:
        idx.add(b)
    idx.clear()
    assert idx.by_isbn=={}
    assert idx.by_author=={}
    assert idx.by_year=={}

def test_rebuild(sample_books):
    idx=IndexDict()
    idx.rebuild(sample_books)
    assert idx.search_by_isbn("ISBN-1") is sample_books[0]
    assert len(idx.search_by_author("Author1"))==2

def test_getitem_access(sample_books):
    idx=IndexDict()
    for b in sample_books:
        idx.add(b)
    assert idx["ISBN-1"].title=="A"
    assert len(idx["Author1"])==2
    assert len(idx[2000])==2