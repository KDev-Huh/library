from fastapi import APIRouter

from service import borrowings as service
from model.borrowings import ReturnRequest

router = APIRouter(prefix="/return")

@router.post("")
def return_book_api(req: ReturnRequest):
    result = service.return_book_service(req.borrower, req.title)
    return result