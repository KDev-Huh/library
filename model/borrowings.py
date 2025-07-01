from pydantic import BaseModel


class Borrowing(BaseModel):
    title: str
    borrower: str

class ReturnRequest(BaseModel):
    borrower: str
    title: str