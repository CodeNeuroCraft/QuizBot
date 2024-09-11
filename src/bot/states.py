from aiogram.filters.state import State
from aiogram.filters.state import StatesGroup

class MainMenu(StatesGroup):
    welcome = State()
    help = State()

class Reg(StatesGroup):
    confirm = State()
    school = State()
    grade = State()
    error_grade = State()
    check = State()
    success = State()