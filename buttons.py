from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove,InlineKeyboardButton, InlineKeyboardMarkup



#buttonlar        
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Yordam ⚡', callback_data='help'),
        InlineKeyboardButton('Bot haqida❕', callback_data='about')
        ]]
    )

ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Bosh menu 🏠', callback_data='home'),
        ],[
        InlineKeyboardButton('❌', callback_data='close')
        ]]
    )
ERROR_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Yordam ⚡', callback_data='help'),
        ],[
        InlineKeyboardButton('❌', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Bosh menu 🏠', callback_data='home'),
        ],[
        InlineKeyboardButton('❌', callback_data='close')
        ]]
    )
DEV_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="Murojaat qilish", url='https://telegram.me/LiderBoy'),
        ],[
        InlineKeyboardButton('❌', callback_data='close')
        ]]
    )
CLOSE_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('❌', callback_data='close')
        ]]
    )