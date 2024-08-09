from aiogram_dialog import Dialog
from aiogram_dialog import LaunchMode

from .windows import confirm_window
from .windows import school_window
from .windows import parallel_window
from .windows import check_window
from .windows import success_window


reg_dialog = Dialog(
    confirm_window(),
    school_window(),
    parallel_window(),
    check_window(),
    success_window(),
    launch_mode=LaunchMode.STANDARD,
)


__all__ = ['reg_dialog']