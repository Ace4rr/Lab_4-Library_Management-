from book import Book
from bookcollection import BookCollection
from indexing import IndexDict
#from src.logger import logger
from typing import List, Optional

class Library:
    def __init__(self):
        self.index=IndexDict()
        self.books=BookCollection(indexer=self.index)

    def add_book(self,book:Book)->None:
        if book.isbn in self.index.by_isbn:
            print(f"Book with ISBN {book.isbn} already exists — skipping add")
            return
        self.books.add(book)
        print(f"Added book: {book}")
    
    def remove_book(self,isbn_or_book:str|Book)->bool:
        isbn=isbn_or_book.isbn if not isinstance(isbn_or_book, str) else isbn_or_book
        ok=self.books.remove(isbn)
        if ok:
            print(f"Removed book with ISBN {isbn}")
        else:
            print(f"Tried to remove missing ISBN {isbn}")
        return ok
    
    def find_by_author(self,author:str)->List[Book]:
        res=self.index.search_by_author(author)
        print(f"Search by author={author}: {len(res)} found")
        return res
    
    def find_by_year(self,year:int)->List[Book]:
        res=self.index.search_by_year(year)
        print(f"Search by year={year}: {len(res)} found")
        return res

    def find_by_genre(self,genre:str)->List[Book]:
        res=[b for b in self.books if b.genre.lower()==genre.lower()]
        print(f"Search by genre={genre}: {len(res)} found")
        return res
    
    def get_book(self,isbn:str)->Optional[Book]:
        b=self.index.search_by_isbn(isbn)
        print(f"Get by ISBN={isbn}: {'found' if b else 'NOT FOUND'}")
        return b
    
    def rebuild_index(self)->None:
        self.index.rebuild(self.books.as_list())
        print("Index rebuilt from current collection")