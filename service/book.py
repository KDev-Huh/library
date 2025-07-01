from model.book import Book
from data import book as data


def create_book(book: Book) -> bool:
    result = data.create_book(book.title, book.author)
    return result


def get_books():
    result = data.get_books_can_borrow()
    return result


def delete_book(book_id: int):
    return data.delete_book_by_id(book_id)