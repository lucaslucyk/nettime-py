from pydantic import BaseModel


class Delete(BaseModel):
    type: int
    id: str
    rev: int
    message: str