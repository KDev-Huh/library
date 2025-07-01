from typing import List

from fastapi import APIRouter, Body
from starlette.responses import JSONResponse

from service import book as service

from model.book import Book

router = APIRouter(prefix="/books")

@router.post("")
def create_book(book: Book):
    result = service.create_book(book)
    return result

@router.get("")
def get_books():
    result = service.get_books()
    return result

@router.delete("/{book_id}")
def delete_book(book_id: int):
    result = service.delete_book(book_id)
    return result