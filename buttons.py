from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove,InlineKeyboardButton, InlineKeyboardMarkup



#buttonlar        
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Yordam â¡', callback_data='help'),
        InlineKeyboardButton('Bot haqidaâ', callback_data='about')
        ]]
    )

ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Bosh menu ð ', callback_data='home'),
        ],[
        InlineKeyboardButton('â', callback_data='close')
        ]]
    )
ERROR_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Yordam â¡', callback_data='help'),
        ],[
        InlineKeyboardButton('â', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Bosh menu ð ', callback_data='home'),
        ],[
        InlineKeyboardButton('â', callback_data='close')
        ]]
    )
DEV_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="Murojaat qilish", url='https://telegram.me/LiderBoy'),
        ],[
        InlineKeyboardButton('â', callback_data='close')
        ]]
    )
CLOSE_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('â', callback_data='close')
        ]]
    )