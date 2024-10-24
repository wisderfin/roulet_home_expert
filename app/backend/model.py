from sqlalchemy.orm import declarative_base


Base = declarative_base()


from sqlalchemy import Column, BigInteger, Integer, String, Boolean, Numeric

class UserModel(Base):
    __tablename__ = 'user'
    id = Column(BigInteger, primary_key=True)
    username = Column(String, nullable=False)
    time = Column(BigInteger, nullable=False)
