from aiogram import types
from bot_manager import dp, bot
from parsers.pornhub_parser import generate_content_from_random_page
import asyncio
from utils import texts
from utils import kbs
from models.state_models import VideoSearch


@dp.message_handler(commands=['start'])
async def start(message: types.Message) -> None:
    await message.answer(text=texts.start_message, reply_markup=kbs.main_menue)


@dp.message_handler(commands=["get_id"])
async def get_id(message: types.Message) -> None:
    await message.answer(text=message.chat.id)


@dp.message_handler()
async def general_message_handler(message: types.Message, state=None) -> None:
    if message.text == texts.go_to_video_search_text:
        await message.answer(text=texts.type_video_desctiption_to_search, reply_markup=kbs.back_to_main_menue)
        await VideoSearch.text_description.set()
    elif message.text == texts.go_to_ads_text:
        await message.answer(text=texts.smartlink_adult_dating_description, reply_markup=kbs.main_menue)
    else:
        await message.answer(text=texts.wrong_request_text, reply_markup=kbs.main_menue)
