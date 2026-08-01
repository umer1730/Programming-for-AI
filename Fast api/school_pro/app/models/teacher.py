from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    subject = Column(String)
    salary = Column(Float)