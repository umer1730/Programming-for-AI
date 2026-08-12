from sqlalchemy import Column,Integer,Float,DateTime
from datetime import datetime

from database import Base

class Prediction(Base):
    __tablename__ = "prediction"

    id = Column(Integer,primary_key=True,index=True)
    input_value = Column(Float,nullable=False)
    prediction = Column(Float, nullable=False)

    created_at = Column(DateTime,default=datetime.utcnow)