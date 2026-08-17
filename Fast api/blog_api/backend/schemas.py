from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    age: int | None = None

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    age: int | None = None

    class Config:
        from_attributes = True

class PostCreate(BaseModel):
    title: str
    content: str
    published: bool = False
    owner_id: int

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    owner_id: int

    class Config:
        from_attributes = True