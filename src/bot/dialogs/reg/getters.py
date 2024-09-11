from aiogram_dialog import DialogManager

async def check_window_getter(
        dialog_manager: DialogManager,
        **kwargs,
):
    dialog_manager.dialog_data['input'] = {
        'id': dialog_manager.dialog_data['user_id'],
        'school': dialog_manager.dialog_data['school'],
        'grade': dialog_manager.dialog_data['grade'],
    }

    return dialog_manager.dialog_data['input']