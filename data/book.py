from data import cur, con
from model.book import Book

def find_book_id_by_title(title: str):
    try:
        sql = "select book_id from books where title = ?"
        cur.execute(sql, (title,))
        book_id = cur.fetchone()[0]
        return book_id
    except Exception as e:
        print(e)
        return None

def create_book(title: str, author: str):
    try:
        sql = "insert into books (title, author) values (?, ?)"
        cur.execute(sql, (title, author))
        con.commit()
        return True
    except Exception as e:
        print(e)
        return False


def get_books_can_borrow():
    try:
        sql = "select title, author from books where available = 1"
        cur.execute(sql)
        rows = cur.fetchall()
        books = [Book(**dict(row)) for row in rows]
        return books
    except Exception as e:
        print(e)
        return []


def delete_book_by_id(book_id : int):
    try:
        sql = "delete from books where book_id = ? and available = 1"
        cur.execute(sql, (book_id,))
        con.commit()
        return True
    except Exception as e:
        print(e)
        return False