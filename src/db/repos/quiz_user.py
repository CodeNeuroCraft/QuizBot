from sqlalchemy.ext.asyncio import AsyncSession

from ..models import QuizUser
from .abstract import Repository


class QuizUserRepo(Repository[QuizUser]):
    '''quiz_user repository for CRUD and other SQL queries.'''

    def __init__(self, session: AsyncSession):
        '''Initialize user repository as for all users or only for one user.'''

        super().__init__(type_model=QuizUser, session=session)

    async def new(
        self,
        user_id: int,
        school: str,
        grade: str,
    ):
        '''Insert a new quiz_user into the database.'''

        await self.session.merge(
            QuizUser(
                user_id=user_id,
                school=school,
                grade=grade,
            )
        )

        await self.session.commit()

    async def from_dict(self, data: dict):
        '''Wrapper for 'new' method.'''

        await self.new(
            data['user_id'],
            data['school'],
            data['grade'],
        )