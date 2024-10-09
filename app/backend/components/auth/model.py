from sqlalchemy import Column, BigInteger, Integer, String, Boolean, Numeric
from components.model import Base

class UserModel(Base):
    __tablename__ = 'user'
    id = Column(BigInteger, primary_key=True)
    username = Column(String, nullable=False)
    balance = Column(Numeric, nullable=False, default=0.0)
    blocked = Column(Boolean, nullable=False, default=False)
    chance = Column(Integer, nullable=False, default=50)
    