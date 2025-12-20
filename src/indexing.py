from typing import Dict, Set, List, Optional
from book import Book

class IndexDict:
    def __init__(self):
        self.by_isbn: Dict[str,Book]={}
        self.by_author: Dict[str,Set[str]]={}
        self.by_year: Dict[int,Set[str]]={}

    def add(self,book:Book):
        self.by_isbn[book.isbn]=book
        self.by_author.setdefault(book.author,set()).add(book.isbn)
        self.by_year.setdefault(book.year,set()).add(book.isbn)


    def remove(self,isbn_or_book: str|Book)->None:
        isbn=isbn_or_book.isbn if not isinstance(isbn_or_book,str) else isbn_or_book
        book=self.by_isbn.pop(isbn,None)
        if not book:
            return
        aset=self.by_author.get(book.author) #author set
        if aset:
            aset.discard(isbn)
            if not aset:
                self.by_author.pop(book.author,None)
        yset=self.by_year.get(book.year) #year set
        if yset:
            yset.discard(isbn)#discardd безопаснее remove (в плохом случае не выдаст ошибку и заигнорит)
            if not yset:
                self.by_year.pop(book.year,None)

    def search_by_isbn(self,isbn:str)->Optional[Book]:
        return self.by_isbn.get(isbn)

    def search_by_author(self,author:str)->List[Book]:
        isbns=self.by_author.get(author,set())
        return [self.by_isbn[i] for i in isbns if i in self.by_isbn]
    
    def search_by_year(self,year:int)->List[Book]:
        isbns=self.by_year.get(year,set())
        return [self.by_isbn[i] for i in isbns if i in self.by_isbn]
    
    def clear(self)-> None:
        self.by_isbn.clear()
        self.by_author.clear()
        self.by_year.clear()

    def rebuild(self,books:List[Book])->None:
        self.clear()
        for b in books:
            self.add(b)

    def __getitem__(self,key):
        if isinstance(key,str):
            if key in self.by_isbn:
                return self.by_isbn[key]
            return self.search_by_author(key)
        if isinstance(key,int):
            return self.search_by_year(key)
        raise KeyError("Unsupported key type for indexDict")
