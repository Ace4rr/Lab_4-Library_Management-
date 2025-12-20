from dataclasses import dataclass
from typing import Optional

@dataclass
class Book:
    title:str
    author:str
    year:int
    genre:str
    isbn:str

    def __repr__(self)->str:
        return (
            f"Book(title={self.title!r}, author={self.author!r}, "
            f"year={self.year}, genre={self.genre!r}, isbn={self.isbn!r})"
        )
    def __str__(self)->str:
        return f"{self.title} by {self.author} ({self.year}) [{self.isbn}]"
    def __contains__(self, item: str) -> bool:
        return item == self.isbn

@dataclass
class RareBook(Book):
    est_value:float=0.0
    def __repr__(self)->str:
        return(
            f"RareBook(title={self.title!r}, author={self.author!r}, "
            f"year={self.year}, value={self.est_value})"
        )

@dataclass
class TextBook(Book):
    subject: Optional[str]=None
    def __repr__(self) -> str:
        sub=f", subject={self.subject!r}" if self.subject else ""
        return (
            f"TextBook(title={self.title!r}, author={self.author!r}, "
            f"year={self.year}{sub})"
        )
