from telebot import types
import telebot

bot = telebot.TeleBot(token='8107222562:AAGGWWUbqDzo8zBugoqkJ75rSbAarBlDf2Y')

@bot.message_handler(content_types=["text"])
def main(message):
    markup = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton("Manzil.", callback_data="Manzil.")
    b2 = types.InlineKeyboardButton("Gruppa.", callback_data="Gruppa.")
    b3 = types.InlineKeyboardButton("Admin", callback_data="Admin")
    b4 = types.InlineKeyboardButton("Kurslar", callback_data="Kurslar")
    b5 = types.InlineKeyboardButton("Yozilish", callback_data="Yozilish")
    markup.add(b1, b2, b3, b4, b5)

    if message.text == "/start":
        bot.send_message(message.chat.id, "Xush kelibsiz!", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def h(call):
    if call.data == "Manzil.":
        bot.send_message(call.message.chat.id, "🏘 Manzil: Asaka shahar,Umid ko'chasi 45-uy.\nMo'ljal: Huzur kafesi ro'parasida.")

    elif call.data == "Gruppa.":
        bot.send_message(call.message.chat.id, "Group: https://t.me/LITECH_IT_Academy\nChannel: https://t.me/litech_itacademy")

    elif call.data == "Admin":
        bot.send_message(call.message.chat.id, "Admin:@User_i01")

    elif call.data == "Kurslar":
        kurs_markup = types.InlineKeyboardMarkup()
        front_end_button = types.InlineKeyboardButton("Front-end", callback_data="front_end")
        backend_button = types.InlineKeyboardButton("Backend", callback_data="backend")
        rus_tili_button = types.InlineKeyboardButton("Rus tili", callback_data="rus_tili")
        ingliz_tili_button = types.InlineKeyboardButton("Ingliz tili", callback_data="ingliz_tili")
        
        kurs_markup.add(front_end_button, backend_button, rus_tili_button, ingliz_tili_button)
        bot.send_message(call.message.chat.id, "Tanlang:", reply_markup=kurs_markup)

    elif call.data == "front_end":
        bot.send_message(call.message.chat.id, "Siz Front-end ni tanladingiz!!!")
    
    elif call.data == "backend":
        bot.send_message(call.message.chat.id, "Siz Back-end ni tanladingiz!!!")
    
    elif call.data == "rus_tili":
        bot.send_message(call.message.chat.id, "Rus tilini tanladingiz!!!")

    elif call.data == "ingliz_tili":
        bot.send_message(call.message.chat.id, "Ingliz tilini tanladingiz!!!")

    elif call.data == "Yozilish":
        msg = bot.send_message(call.message.chat.id, "Ismingizni kiriting:")
        bot.register_next_step_handler(msg, get_surname)

def get_surname(message):
    surname = message.text
    msg = bot.send_message(message.chat.id, "Familyangizni kiriting:")
    bot.register_next_step_handler(msg, get_age, surname)

def get_age(message, surname):
    age = message.text
    msg = bot.send_message(message.chat.id, "Yoshingizni kiriting:")
    bot.register_next_step_handler(msg, get_phone_number, surname, age)

def get_phone_number(message, surname, age):
    phone_number = message.text
    if len(phone_number) != 9 or not phone_number.isdigit():
        msg = bot.send_message(message.chat.id, "Telefon raqamingiz: 977967607")
        bot.register_next_step_handler(msg, get_phone_number, surname, age)
    else:
        admin_chat_id = '6495169271' 
        bot.send_message(admin_chat_id, f"Ism: {message.text}\nFamiliya: {surname}\nYosh: {age}\nTelefon raqami: {phone_number}\nYozilish yakunlandi!")

if __name__ == "__main__":
    bot.polling(none_stop=True)