from aiogram import types
from bot_manager import dp, bot
from aiogram.dispatcher import FSMContext
from parsers.pornhub_parser import generate_content_from_random_page
from parsers.bs4parser import get_pornhub_results
from models.state_models import VideoSearch
from utils import texts, kbs


@dp.message_handler(state=VideoSearch.text_description)
async def text_description_handle(message: types.Message, state: FSMContext):
    if message.text == texts.go_to_menue_text:
        await state.finish()
        await message.answer(text=texts.going_to_main_menue_text, reply_markup=kbs.main_menue)
        return

    async with state.proxy() as data:
        data["video_description"] = message.text

    await message.answer(text=texts.waiting_videos_to_load_text, reply_markup=kbs.main_menue)
    # messages = generate_content_from_random_page(message.chat.id, message.text)

    messages = get_pornhub_results(message.text)

    await handle_messages_from_parser(messages, message, state)


@dp.message_handler(state=VideoSearch.decision_stage)
async def decision_stage_handle(message: types.Message, state: FSMContext):
    if message.text == texts.get_more_videos_text:
        await message.answer(text=texts.waiting_videos_to_load_text, reply_markup=kbs.main_menue)
        async with state.proxy() as data:
            # asyncio.create_task(start_parsing(message.chat.id, data["video_description"], message.chat.id, state))
            # messages = generate_content_from_random_page(message.chat.id, data["video_description"])
            messages = get_pornhub_results(data["video_description"])
            await handle_messages_from_parser(messages, message, state)

    elif message.text == texts.go_to_menue_text:
        await state.finish()
        await message.answer(text=texts.going_to_main_menue_text, reply_markup=kbs.main_menue)
        return


async def handle_messages_from_parser(messages: list, message, state):
    if not messages:
        await bot.send_message(message.chat.id, text=texts.not_enough_results_error_text)  # сделать в
        # будущем подборку из запросов пользователей, сделать рандомно. Для этого сделать таблицу с текстовыми
        # запросами
        await bot.send_message(message.chat.id, text=texts.going_to_main_menue_text, reply_markup=kbs.main_menue)
        await state.finish()
    elif messages:
        for vieo_description in messages:
            await bot.send_message(message.chat.id, vieo_description)
        await bot.send_message(message.chat.id, text=texts.want_more_videos_message, reply_markup=kbs.get_more_videos_menue)
        await VideoSearch.decision_stage.set()

    else:
        await bot.send_message(message.chat.id, text=texts.general_error_text)
        await bot.send_message(message.chat.id, text=texts.going_to_main_menue_text, reply_markup=kbs.main_menue)
        await state.finish()