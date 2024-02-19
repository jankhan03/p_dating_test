from aiogram.dispatcher.filters.state import StatesGroup, State


class VideoSearch(StatesGroup):
    text_description = State()
    decision_stage = State()