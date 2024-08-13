from sqlalchemy import String
from sqlalchemy import BigInteger
from sqlalchemy import Column

from .base import Base


class QuizUser(Base):
    __tablename__ = 'quiz_users'

    id = Column(BigInteger, primary_key=True)
    school = Column(String)
    parallel = Column(String)