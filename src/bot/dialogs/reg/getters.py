from aiogram_dialog import DialogManager

async def check_window_getter(
        dialog_manager: DialogManager,
        **kwargs,
):
    return dialog_manager.dialog_data['input']