from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class QRData(Base):
    __tablename__ = "qrdata"

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer)
    data = Column(String)
