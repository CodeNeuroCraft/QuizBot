from sqlalchemy import String
from sqlalchemy import BigInteger
from sqlalchemy import Column
from sqlalchemy.orm import DeclarativeBase


class QuizUserORM(DeclarativeBase):
    __tablename__ = 'quiz_users'

    id = Column(BigInteger, primary_key=True)
    school = Column(String)
    parallel = Column(String)