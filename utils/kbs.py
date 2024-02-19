from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from utils import texts


main_menue = [
    [KeyboardButton(text=texts.go_to_video_search_text)],
    [KeyboardButton(text=texts.go_to_ads_text)]
]

main_menue = ReplyKeyboardMarkup(keyboard=main_menue, resize_keyboard=True)

get_more_videos_menue = [
    [KeyboardButton(text=texts.get_more_videos_text)],
    [KeyboardButton(text=texts.go_to_menue_text)]
]

get_more_videos_menue = ReplyKeyboardMarkup(keyboard=get_more_videos_menue, resize_keyboard=True)


back_to_main_menue = [
    [KeyboardButton(text=texts.go_to_menue_text)]
]

back_to_main_menue = ReplyKeyboardMarkup(keyboard=back_to_main_menue, resize_keyboard=True)