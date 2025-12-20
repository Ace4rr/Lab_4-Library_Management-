from book import Book, RareBook, TextBook

def test_book_creation():
    b=Book(
        title="1984",
        author="George Orwell",
        year=1949,
        genre="Dystopia",
        isbn="ISBN-1")
    assert b.title=="1984"
    assert b.author=="George Orwell"
    assert b.year==1949
    assert b.genre=="Dystopia"
    assert b.isbn=="ISBN-1"

def test_book_str():
    b=Book("1984", "Orwell", 1949, "Dystopia", "ISBN-1")
    assert str(b)=="1984 by Orwell (1949) [ISBN-1]"

def test_book_repr():
    b=Book("1984", "Orwell", 1949, "Dystopia", "ISBN-1")
    r=repr(b)
    assert "Book(" in r
    assert "ISBN-1" in r

def test_book_contains():
    b=Book("1984", "Orwell", 1949, "Dystopia", "ISBN-1")
    assert "ISBN-1" in b
    assert "ISBN-2" not in b

def test_rarebook_is_book():
    rb=RareBook("Old Book", "Author", 1900, "History", "ISBN-2", est_value=1000.0)
    assert isinstance(rb, Book)
    assert rb.est_value==1000.0

def test_textbook_subject():
    tb=TextBook("Math", "Teacher", 2020, "Education", "ISBN-3", subject="Algebra")
    assert tb.subject=="Algebra"
    assert isinstance(tb, Book)