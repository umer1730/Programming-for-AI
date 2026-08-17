from sqlalchemy import Column,Integer,String,Boolean,Text,ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__  = "users"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False) # nullable mean no null value allowed
    email = Column(String,nullable=False)
    age = Column(Integer,nullable=False)
    posts = relationship("Post",back_populates="owner")

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,nullable=False)
    content = Column(Text,nullable=False)
    published = Column(Boolean,default=False)

    owner_id = Column(Integer,ForeignKey("users.id"),nullable=False)
    owner = relationship("User",back_populates="posts")