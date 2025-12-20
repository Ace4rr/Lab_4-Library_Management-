import random
from typing import Optional
from library import Library
from book import Book, RareBook, TextBook
#from logger import logger

SAMPLE_TITLES=[
    ("The Time Machine", "H.Wells", 1895, "Sci-Fi"),
    ("Pride and Prejudice", "J.Austen", 1813, "Romance"),
    ("Python 101", "A.Tutor", 2020, "Programming"),
    ("Modern Physics", "I.Scientist", 1999, "Science"),
    ("Философия", "Иванов", 2010, "Philosophy"),
]

GENRES = ["Sci-Fi", "Romance", "Programming", "Science", "Philosophy", "Fantasy"]

def _make_random_book(rnd: random.Random, idx: int=0):
    t,a,y,g=rnd.choice(SAMPLE_TITLES)
    isbn=f"ISBN-{rnd.randint(1000,9999)}-{idx}"
    r=rnd.random()
    if r<0.15:
        return RareBook(title=t,author=a,year=y,genre=g,isbn=isbn,est_value=rnd.uniform(100.0,2000.0))
    if r<0.35:
        return TextBook(title=t,author=a,year=y,genre=g,isbn=isbn,subject="AutoGen")
    return Book(title=t, author=a, year=y, genre=g, isbn=isbn)
    
def run_simulation(steps:int=20,seed:Optional[int]=None)->None:
    rnd=random.Random(seed)
    lib=Library()

    for i in range(5):
        b=_make_random_book(rnd,idx=1)
        lib.add_book(b)

    actions=[
        "add_book",
    "remove_random",
    "search_author",
    "search_genre",
    "search_year",
    "get_missing",
    "rebuild_index"
    ]

    for step in range(1,steps+1):
        action=rnd.choice(actions)
        print(f"Step {step}/{steps}: event -> {action}")

        if action=="add_book":
            b=_make_random_book(rnd,idx=step)
            lib.add_book(b)
        elif action=="remove_random":
            if len(lib.books)==0:
                print("No books to remove")
            else:
                book=rnd.choice(list(lib.books))
                lib.remove_book(book.isbn)
        elif action == "search_author":
            if rnd.random()<0.7 and len(lib.books)>0:
                author=rnd.choice(list({b.author for b in lib.books}))
            else:
                author="Nonexisting author"
            lib.find_by_author(author)
        elif action=="search_genre":
            genre=rnd.choice(GENRES)
            lib.find_by_genre(genre)
        elif action=="search_year":
            year=rnd.choice([b.year for b in lib.books]) if len(lib.books) else rnd.randint(1900,2025)
            lib.find_by_year(year)
        elif action=="get_missing":
            fake_isbn=f"ISBN-0000-{rnd.randint(10000,99999)}"
            lib.get_book(fake_isbn)
        elif action=="rebuild_index":
            lib.rebuild_index()
print("Simultaion finished")