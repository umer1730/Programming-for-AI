from pydantic import BaseModel

class AuthorCreate(BaseModel):
    name: str

class BookCreate(BaseModel):
    title: str
    price: float
    author_id: int

class AuthorResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class BookResponse(BaseModel):
    id: int
    title: str
    price: float
    author_id: int

#Jab tum SQLAlchemy object return karoge, Pydantic us object ko read nahi kar payega aur error aa sakta hai so we use this 
    class Config:
        from_attributes = True