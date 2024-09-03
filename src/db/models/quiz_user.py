from sqlalchemy import BigInteger
from sqlalchemy import VARCHAR
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class QuizUser(Base):
    """QuizUser model."""

    __tablename__ = 'accounts'


    user_id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, unique=True, nullable=False
    )
    school: Mapped[str] = mapped_column(
        VARCHAR(255), unique=False, nullable=True
    )
    grade: Mapped[str] = mapped_column(
        VARCHAR(255), unique=False, nullable=True
    )
