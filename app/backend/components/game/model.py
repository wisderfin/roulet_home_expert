from sqlalchemy import Column, Integer, String, Numeric
from components.model import Base


class PresentModel(Base):
    __tablename__ = 'present'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
