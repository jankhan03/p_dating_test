from aiogram import executor
from bot_manager import dp
from handlers.start_handler import *
from handlers.video_search_handler import *

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
