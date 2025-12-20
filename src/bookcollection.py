from typing import Iterable, List, Union, overload
from book import Book
from indexing import IndexDict

class BookCollection:

    def __init__(self,books: Iterable[Book]|None=None, indexer: IndexDict|None=None):
        self._books: List[Book]=list(books) if books else []
        self ._indexer=indexer 

    def __len__(self)->int:
        return len(self._books)

    def __iter__(self):
        return iter(self._books)
    
    @overload#позволяет считать mypy и прекоммиту при обращении к Book[1] - Book а при Book[1:4] - Book collection
    def __getitem__(self, idx: int)-> Book: ...

    @overload
    def __getitem__(self, s: slice)-> "BookCollection": ...

    def __getitem__(self, key: Union[int, slice])->Union[Book, "BookCollection"]:#означает что параметр key может быть как и Int так и срезом
        if isinstance(key, slice):#проверяет является ли key срезом
            return BookCollection(self._books[key], indexer=self._indexer)
        return self._books[key]
    
    def add(self, book: Book)->None:
        self._books.append(book)
        if self._indexer is not None:
            self._indexer.add(book)

    def remove(self,book_or_isbn: Union[Book, str])->bool:
        """Удаляет книгу по обьекту или isbn"""
        isbn=book_or_isbn.isbn if isinstance(book_or_isbn,Book) else book_or_isbn
        for i,b in enumerate(self._books):
            if b.isbn==isbn:
                removed=self._books.pop(i)
                if self._indexer is not None:
                    self._indexer.remove(isbn)
                return True 
        return False
    
    def clear(self)->None:
        self._books.clear()
        if self._indexer is not None:
            self._indexer.clear()

    def __contains__(self,item: Union[Book,str])->bool:
        if isinstance(item,Book):
            return any(b.isbn==item.isbn for b in self._books)
        return any(b.isbn==item for b in self._books)

    def __add__(self,other: "BookCollection") ->"BookCollection":
        merged=BookCollection(indexer=self._indexer)
        seen=set()
        for b in self._books+list(other):
            if b.isbn not in seen:
                merged._books.append(b)
                seen+=(b.isbn)

        if self._indexer is not None:
            self._indexer.rebuild(merged._books)
        return merged 

    def as_list(self)->List[Book]:
        return list(self._books) 