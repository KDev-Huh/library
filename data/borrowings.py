from typing import List, Tuple

from . import con, cur
from data import book as book_data

def test():
    return "sqlite connect ok"


def borrow_book(title: str, borrower: str):
    try:
        book_id = book_data.find_book_id_by_title(title)
        sql = "INSERT INTO borrowings (book_id, borrower) VALUES (?, ?)"
        cur.execute(sql, (book_id, borrower))
        con.commit()
        return True
    except Exception as e:
        print(e)
        return False

# def get_borrow_data() -> list[tuple[str, str]]:
#     sql = """
#     SELECT borrower, title
#     FROM borrowings
#     JOIN books ON borrowings.book_id = books.book_id
#     WHERE returned_at IS NULL
#     """
#     cur.execute(sql)
#     rows = cur.fetchall()
#     return [(row["borrower"], row["title"]) for row in rows]

def get_borrowed_books_by_month(borrow_month: int) -> List[Tuple[str, str, str]]:
    sql = """
    SELECT b.title, b.author, br.borrowed_at
    FROM borrowings br
    JOIN books b ON br.book_id = b.book_id
    WHERE strftime('%m', br.borrowed_at) = ?
    """
    month_str = f"{borrow_month:02d}"  # 7 → "07"
    cur.execute(sql, (month_str,))
    rows = cur.fetchall()
    return [(row["title"], row["author"], row["borrowed_at"]) for row in rows]


def get_borrowings_by_borrower(borrower):
    sql = """
        SELECT b.title, b.author, br.borrowed_at, br.returned_at
        FROM borrowings br
        JOIN books b ON br.book_id = b.book_id
        WHERE br.borrower = ?
        ORDER BY br.borrowed_at DESC
        """
    cur.execute(sql, (borrower,))
    rows = cur.fetchall()
    return [(row["title"], row["author"], row["borrowed_at"], row["returned_at"]) for row in rows]


def return_book(borrower, title):
    book_id = book_data.find_book_id_by_title(title)

    cur.execute("""
            UPDATE borrowings
            SET returned_at = datetime('now')
            WHERE borrower = ? AND book_id = ? AND returned_at IS NULL
        """, (borrower, book_id))

    if cur.rowcount == 0:
        return False

    cur.execute("UPDATE books SET available = 1 WHERE book_id = ?", (book_id,))
    con.commit()
    return True