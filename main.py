import telebot
from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove,InlineKeyboardButton, InlineKeyboardMarkup
from countryinfo import CountryInfo
import sqlite3 as sql
from config import *
from buttons import *
from strings import *


bot=telebot.TeleBot(token)



with sql.connect(dbfile) as con:
    cur=con.cursor()
    
    cur.execute("""CREATE TABLE IF NOT EXISTS user(
        id INTEGER,
        name TEXT
    )""")
    
    con.commit()

def insert(userid, name):
    con= sql.connect(dbfile)
    cur = con.cursor()
    cur.execute("SELECT * FROM user WHERE id = ?",(userid,))
    
    if cur.fetchone() is None:
        
        cur.execute("INSERT INTO user(id,name)VALUES(?,?)",(userid,name))
        con.commit()

#buyruqlar
@bot.message_handler(commands=['start'])
def start_msg(msg):
    	u_name=msg.from_user.first_name
    	insert(msg.chat.id, u_name)
    	
    	chat_id=msg.chat.id
    	
    	bot.send_message(chat_id,START_TEXT .format(msg.from_user.first_name), reply_markup=START_BUTTONS, parse_mode="markdown")
    

@bot.message_handler(commands=['help'])
def help_msg(msg):
    
    chat_id=msg.chat.id
    
    bot.send_message(chat_id,HELP_TEXT, reply_markup=HELP_BUTTONS)

@bot.message_handler(commands=['about'])
def about_msg(msg):
    
    chat_id=msg.chat.id
    
    bot.send_message(chat_id,ABOUT_TEXT, reply_markup=ABOUT_BUTTONS)

@bot.message_handler(commands=['developer'])
def dev_msg(msg):
    
    chat_id=msg.chat.id
    
    bot.send_message(chat_id,DEV_TEXT, reply_markup=DEV_BUTTONS, parse_mode="html")

#admin_panel
@bot.message_handler(commands=['users'])
def users(msg):
    stat(msg)

@bot.message_handler(commands=['liderboy'])
def admin_panel(msg):
        if msg.chat.id==admin:
        	bot.send_message(msg.chat.id,"Assalomu alaykum Arslonbek admin panelga xush kelibsiz!!!\nIshlatishingiz mumkin boʻlgan buyruqlar:\n/copysend - Oddiy xabar yuborish.\n/forsend - Forward xabar yuborish.\n/users - Foydalanuvchilar soni.", reply_markup=CLOSE_BUTTONS)
        else:
        	bot.send_message(msg.chat.id,"Notoʻgʻri buyruq!", reply_markup=CLOSE_BUTTONS)


@bot.message_handler(commands=['copysend'])
def copymsg(msg):
        if msg.chat.id==admin:
        	xabar = bot.send_message (admin,'Yaxshi, endi menga xabar yuboring!', reply_markup=CLOSE_BUTTONS)
        	bot.register_next_step_handler(xabar,copysend)
        else:
        	bot.send_message(msg.chat.id,"Notoʻgʻri buyruq!",reply_markup=CLOSE_BUTTONS)
@bot.message_handler(commands=['forsend'])
def formsg(msg):
    if msg.chat.id==admin:
        xabar = bot.send_message (admin,'Yaxshi, endi menga forward qilib xabar yuboring!', reply_markup=CLOSE_BUTTONS)
        bot.register_next_step_handler(xabar,forsend)
    else:
        bot.send_message(msg.chat.id,"Notoʻgʻri buyruq!", reply_markup=CLOSE_BUTTONS)

def copysend(msg):
    
    msgid = msg.message_id
    con = sql.connect(dbfile)
    cur = con.cursor()
    cur.execute("SELECT id FROM user")
    usersid = cur.fetchall()
    count=0
    for user_id in usersid:
       try:
           
           bot.copy_message(user_id,msg.chat.id,msgid)
           count+=1
       except:
           continue 
    bot.send_message(admin,f'Xabar <b>{count}</b> foydalanuvchiga yetkazildi.', parse_mode="html", reply_markup=CLOSE_BUTTONS)
        #print(user_id)
    con.commit()

def forsend(msg):
    
    msgid = msg.message_id
    con = sql.connect(dbfile)
    cur = con.cursor()
    cur.execute("SELECT id FROM user")
    usersid = cur.fetchall()
    count = 0
    for user_id in usersid:
       try:
           bot.forward_message(user_id,msg.chat.id,msgid)
           count+=1
       except:
           continue 
    bot.send_message (admin,f' Forward Xabar <b>{count}</b> foydalanuvchiga yetkazildi!',parse_mode="html", reply_markup=CLOSE_BUTTONS)
       
           
    con.commit()
    
def stat(msg):
    con = sql.connect(dbfile)
    cur = con.cursor()
    cur.execute("SELECT count(*) FROM user")
    users = cur.fetchone()
    con.commit()
    bot.send_message(msg.chat.id, f'Bot azolari: <b>{(str(users[0]))}</b>\nDeveloper: @LiderBoy ', parse_mode="html", reply_markup=CLOSE_BUTTONS)

#asos
@bot.message_handler(content_types=['text'])
def asos(msg):
    try:
        country = CountryInfo(msg.text)
        info = f"""
Nomi : `{country.name()}`
Asl nomi : `{country.native_name()}`
Poytaxt : `{country.capital()}`
Aholisi : `{country.population()}`
Mintaqa : `{country.region()}`
Sub Mintaqa : `{country.subregion()}`
Viloyatlar: `{country.provinces}`
Asosiy domen nomi : `{country.tld()}`
Qoʻngʻiroq kodi: `{country.calling_codes()}`
Valyutasi : `{country.currencies()}`
Vaqt mintaqasi : `{country.timezones()}`
    
**Maʼlumotlar wikipedia.org saytidan olindi...**
"""
        country_name=country.name()
        country_name = country_name.replace(" ", "+")
        info_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton('Wikipedia', url=f'{country.wiki()}'),
            ],[
            InlineKeyboardButton('❌', callback_data='close')
            ]]
        )
        
        bot.send_message(msg.chat.id, info, reply_markup=info_markup, parse_mode="MARKDOWN")
    except Exception as ex:
        bot.send_message(msg.chat.id, "Kechirasiz, topilmadi 😔 davlat nomi toʻgʻri yozilganligini tekshiring!", reply_markup=ERROR_BUTTON)

#callbacks
@bot.callback_query_handler(func = lambda call: True)
def delete(call):
    if call.data == 'home':
    	bot.edit_message_text("Bosh menuga qaytdingiz.",  call.message.chat.id, call.message.message_id, reply_markup=START_BUTTONS)
  
    if call.data == 'help':
        bot.edit_message_text(HELP_TEXT, call.message.chat.id, call.message.message_id,reply_markup=HELP_BUTTONS)
  
    if call.data == 'about':
        bot.edit_message_text(ABOUT_TEXT, call.message.chat.id, call.message.message_id, reply_markup=ABOUT_BUTTONS)
  
    if call.data == 'close':
        try:
        	for i in range(2):
        		bot.delete_message(call.message.chat.id, call.message.message_id-i )
        except Exception as ex:
        	bot.answer_callback_query(callback_query_id=call.id, show_alert=False,text="❌ Xatolik: Iltimos tugmani bir marta bosing!")
        	#bot.send_message(call.message.chat.id, f"{ex}")
#tugadi
bot.polling()