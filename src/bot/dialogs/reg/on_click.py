from aiogram.types import Message, User
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog import ShowMode
from surrealdb import Surreal

from src.bot.states import Reg


class userDB:
    db = Surreal('ws://localhost:8000/rpc')

    def __init__(self):
        self.db.connect()
        self.db.signin({
            'user': 'root',
            'pass': 'root',
        })
    
    async def open_session(self, user: User):
        self.user_id = user.id
        await self.db.create(self.user_id, {
            'school': None,
            'parallel': None,
        })

    async def set_school(self, school: str):
        self.school = school

    async def set_parallel(self, parallel: str):
        self.parallel = parallel

    async def commit_session(self):
        await self.db.update(f'account:{self.user_id}', {
            'school': self.school,
            'parallel': self.parallel
        })

    async def abort_session(self):
        await self.db.delete(self.user_id)
        self.school = ''
        self.parallel = ''

    async def get_session_data(self, ):
        return {
            'school': self.school,
            'parallel': self.parallel,
        }
        
    
async def close(
        callback: CallbackQuery,
        button: Button,
        manager: DialogManager
):
    await manager.done()

# База данных
registrations = userDB()

async def start(
        callback: CallbackQuery,
        button: Button,
        manager: DialogManager,
):
    await registrations.open_session(callback.from_user)

async def abort(
        callback: CallbackQuery,
        button: Button,
        manager: DialogManager,
):
    await registrations.abort_session()

async def commit_data(
        callback: CallbackQuery,
        button: Button,
        manager: DialogManager,
):
    await registrations.commit_session()

async def process_school(
        message: Message,
        message_input: MessageInput,
        manager: DialogManager,
):
    manager.show_mode=ShowMode.EDIT
    await registrations.set_school(message.text)
    await message.delete()
    await manager.switch_to(Reg.parallel)

async def process_parallel(
        message: Message,
        message_input: MessageInput,
        manager: DialogManager,
):
    manager.show_mode=ShowMode.EDIT
    await registrations.set_parallel(message.text)
    await message.delete()
    await manager.switch_to(Reg.check)