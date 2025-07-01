from fastapi import APIRouter

from model.borrowings import ReturnRequest, Borrowing
from service import borrowings as service

router = APIRouter(prefix="/borrows")

@router.post("")
def borrow(borrowing: Borrowing):
    result = service.borrow_book(borrowing)
    return result

@router.get("/month/{borrow_month}")
def month_borrow(borrow_month: int):
    result = service.get_month_borrow(borrow_month)
    return result

@router.get("/{borrower}/books")
def get_borrow_data_by_borrower(borrower: str):
    return service.get_borrow_data_by_borrorwer(borrower)