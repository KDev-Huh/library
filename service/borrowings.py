import service
from data import borrowings as data
from cache import borrower as cache
from model.borrowings import Borrowing

def borrow_book(borrowing: Borrowing):
    try:
        data.borrow_book(borrowing.title, borrowing.borrower)
        cache.save_borrowed_book(borrowing.borrower, borrowing.title)
        return True
    except Exception as e:
        print(e)
        return False


def get_month_borrow(borrow_month: int):
    records = data.get_borrowed_books_by_month(borrow_month)
    result = [
        {
            "title": title,
            "author": author,
            "borrowed_at": borrowed_at
        }
        for title, author, borrowed_at in records
    ]
    return result


def get_borrow_data_by_borrorwer(borrower):
    records = data.get_borrowings_by_borrower(borrower)
    return [
        {
            "title": title,
            "author": author,
            "borrowed_at": borrowed_at,
            "returned_at": returned_at
        }
        for title, author, borrowed_at, returned_at in records
    ]


def return_book_service(borrower, title):
    result = data.return_book(borrower, title)

    if result:
        cache_result = cache.return_book(borrower, title)
        return cache_result

    return False