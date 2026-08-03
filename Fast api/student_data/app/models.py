from sqlalchemy import Column, Integer, String
from app.database import Base

class Student(Base):
    __tablename__ = "Students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    department = Column(String)