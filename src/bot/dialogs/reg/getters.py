from aiogram_dialog import DialogManager

async def check_window_get_data(dialog_manager: DialogManager, **kwargs):
    return dialog_manager.dialog_data['user_input']