from aiogram_dialog import Dialog
from aiogram_dialog import LaunchMode

from .windows import welcome_window
from .windows import help_window


main_menu_dialog = Dialog(
    welcome_window(),
    help_window(),
    launch_mode=LaunchMode.STANDARD,
)


__all__ = ['main_menu_dialog']