# # # # from telebot import types
# # # # import telebot

# # # # bot = telebot.TeleBot(token='7738243272:AAEGWIY4U3uxJGpXDSaDlFm8T_uxPEGfEWI')

# # # @bot.message_handler(content_types=["text"])
# # # def main(message):
# # #     if message.text == "/start":
# # #         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# # #         b1 = types.KeyboardButton("Python tarixi")
# # # #         b2 = types.KeyboardButton("C ++ tarixi")
# # # #         b3 = types.KeyboardButton("Java tarixi")
# # # #         b4 = types.KeyboardButton("Kotlin tarixi")
# # # #         b5 = types.KeyboardButton("video")
# # # #         b6 = types.KeyboardButton("Faylar")
# # # #         markup.add(b1, b2, b3, b4, b5, b6)  
# # # #         bot.send_message(message.chat.id, "Salom!", reply_markup=markup)

# # # #     elif message.text == "Python tarixi":
# # # #         bot.send_message(message.chat.id, "Python ni Guido van Rossum yaratgan!")

# # # #     elif message.text == "C ++ tarixi":
# # # #         bot.send_message(message.chat.id, "C ++ ni Bjarne Stroustrup yaratgan!")

# # # #     elif message.text == "Java tarixi":
# # # #         bot.send_message(message.chat.id, "Java ni James Gosling yaratgan!")

# # #     # elif message.text == "Kotlin tarixi":
# # #     #     bot.send_message(message.chat.id, "Kotlin ni JetBrains kompaniyasi yaratgan!")
# # #     # elif message.text == "video":
# # #     #     with open("video_test.mp4", "rb") as video:
# # #     #         bot.send_video(message.chat.id, video)
# # # #     elif message.text == "Faylar":
# # # #         with open("a.txt", "rb") as fayl:
# # # #             bot.send_document(message.chat.id, fayl)
# # # #     else:
# # # #         bot.send_message(message.chat.id, "Iltimos, to'g'ri variantni tanla!!!")


# # # # if __name__ == "__main__":
# # # #     bot.polling(none_stop=True)


# # # '''
# # # Uyga vazifa
# # # '''


# # # # from telebot import types
# # # # import telebot

# # # # bot = telebot.TeleBot(token='7738243272:AAEGWIY4U3uxJGpXDSaDlFm8T_uxPEGfEWI')

# # # # @bot.message_handler(content_types=["text"])
# # # # def main(message):
# # # #     if message.text == "/start":
# # # #         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# # # #         b1 = types.KeyboardButton("9 - sinf bsb-1,2")
# # # #         b2 = types.KeyboardButton("10 - sinf bsb-1,2")
# # # #         markup.add(b1, b2,)  
# # # #         bot.send_message(message.chat.id, "Salom!", reply_markup=markup)

# # # #     elif message.text == "9 - sinf bsb-1,2":
# # # #         bot.send_message(message.chat.id, "@bsb_va_chsb")

# # # #     elif message.text == "10 - sinf bsb-1,2":
# # # #         bot.send_message(message.chat.id, "@bsb_va_chsb")

# # # #     else:
# # # #         bot.send_message(message.chat.id, "Iltimos, to'g'ri variantni tanlang!!!")

# # # # if __name__ == "__main__":
# # # #     bot.polling(none_stop=True)

# # # '''
# # # 6.11.2024-yil
# # # Mavzu:
# # # '''

# # # # import telebot
# # # # bot = telebot.TeleBot(token="7738243272:AAEGWIY4U3uxJGpXDSaDlFm8T_uxPEGfEWI")

# # # # @bot.message_handler(content_types=['text']) 
# # # # def main(message):
# # # #     if message.text == "/start":
# # # #         lst_number = bot.send_message(message.chat.id, "list kirit: ")
# # # #         bot.register_next_step_handler(lst_number, get_fun)
# # # #     else:
# # # #         bot.send_message(message.chat.id, "/start")
# # # #         main(message)

# # # # def get_fun(message):
# # # #     lst_number = message.text
# # # #     if lst_number[0] == "[" and lst_number[-1] == "]":
# # # #         try:
# # # #             lst_number = lst_number[1:-1]  
# # # #             number_list = [int(x.strip()) for x in lst_number.split(',')]

# # #              bot.send_message(message.chat.id, f"Maximum number is: {max(number_list)}")
# # #          except ValueError:
        
# # #              bot.send_message(message.chat.id, "Please enter a valid list of integers.")
# # #      else:
# # #          bot.send_message(message.chat.id, "Please enter the list in the correct format: [1, 2, 3]")
# # #  bot.polling(none_stop=True)




# # #  import telebot

# # #  bot = telebot.TeleBot(token='7738243272:AAEGWIY4U3uxJGpXDSaDlFm8T_uxPEGfEWI')

# # #  @bot.message_handler(commands=["start"])
# # #  def start(message):
# # #      bot.send_message(message.chat.id, "Matn kiriting:")
# # #      bot.register_next_step_handler(message, get_text)

# # #  def get_text(message):
# # #      matn = message.text.lower()
# # #      bot.send_message(message.chat.id, "Iltimos, qidirilayotgan harfni kiriting:")
# # #      bot.register_next_step_handler(message, get_harf, matn)

# # #  def get_harf(message, matn):
# # #      harf = message.text.lower() 
# # #      son = matn.count(harf) 
# # #      if son > 0:
# # #          bot.send_message(message.chat.id, f"'{harf}' harfi matnda {son} marta takrorlangan.")
# # #      else:
# # #         bot.send_message(message.chat.id, f"'{harf}' harfi matnda mavjud emas.")


# # # # bot.polling()



# # # '''

# # # '''

# # # from telebot import types
# # # import telebot

# # # bot = telebot.TeleBot(token='7345837427:AAHYlTuY5_1ozPhHwUKKRvJid7FL5NEeskc')

# # # @bot.message_handler(content_types=["text"])
# # # def main(message):
# # #     if message.text == "/start":
# # #         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# # #         b1 = types.KeyboardButton("🤖pul ishlash")
# # #         b2 = types.KeyboardButton("🤖Dasturlash")  

# # #         markup.add(b1, b2)  
# # #         bot.send_message(message.chat.id, "Salom! Iltimos, biror variantni tanlang:", reply_markup=markup)

# # #     elif message.text == "🤖pul ishlash":
# # #         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# # #         b1 = types.KeyboardButton("💼 Onlayn ish")
# # #         b2 = types.KeyboardButton("📈 Investitsiya")  

# # #         markup.add(b1, b2)  
# # #         bot.send_message(message.chat.id, "Pul ishlash bo'yicha variantlar:", reply_markup=markup)

# # #     elif message.text == "🤖Dasturlash":
# # #         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# # #         b1 = types.KeyboardButton("🖥 Python")
        
# # #         markup.add(b1)  
# # #         bot.send_message(message.chat.id, "Dasturlash bo'yicha variantlar:", reply_markup=markup)

# # #     elif message.text == "💼 Onlayn ish":
# # #         bot.send_message(message.chat.id, "Onlayn ish variantlari haqida ma'lumot...")
       
# # #     elif message.text == "📈 Investitsiya":
# # #         bot.send_message(message.chat.id, "Investitsiyalar haqida ma'lumot...")

# # #     elif message.text == "🖥 Python":
# # #         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# # #         v1 = types.KeyboardButton("📹 Video 1")
# # #         v2 = types.KeyboardButton("📹 Video 2")

# # #         markup.add(v1, v2)  
# # #         bot.send_message(message.chat.id, "Python bo'yicha videolarni tanlang:", reply_markup=markup)

# # #     elif message.text == "📹 Video 1":
# # #         with open("#00 Python Darslari _ Kirish so'z.mp4", "rb") as video:
# # #             bot.send_video(message.chat.id, video)

# #     # elif message.text == "📹 Video 2":
# #     #     with open("#00 Python Darslari _ mohirdev.uz bilan tanishuv.mp4", "rb") as video:
# #     #         bot.send_video(message.chat.id, video)

# # #     else:
# # #         bot.send_message(message.chat.id, "Iltimos, to'g'ri variantni tanla!!!")

# # # if __name__ == "__main__":
# # #     bot.polling(none_stop=True)


# # '''
# # 15.11.2024-yil.
# # Mavzu: Tg bot yozish. 
# # '''

# # """
# # from telebot import types
# # import telebot

# # bot = telebot.TeleBot(token='7738243272:AAEGWIY4U3uxJGpXDSaDlFm8T_uxPEGfEWI')

# # @bot.message_handler(content_types=["text"])
# # def main(message):
# #     markup = types.InlineKeyboardMarkup()
# #     b1 = types.InlineKeyboardButton("Manzil.", callback_data="Manzil.")
# #     b2 = types.InlineKeyboardButton("Gruppa.", callback_data="Gruppa.")
# #     b3 = types.InlineKeyboardButton("Admin", callback_data="Admin")
# #     b4 = types.InlineKeyboardButton("Kurslar", callback_data="Kurslar")
# #     b5 = types.InlineKeyboardButton("Yozilish", callback_data="Yozilish")
# #     markup.add(b1, b2, b3, b4, b5)

# #     if message.text == "/start":
# #         bot.send_message(message.chat.id, "Xush kelibsiz!", reply_markup=markup)

# # @bot.callback_query_handler(func=lambda call: True)
# # def h(call):
# #     if call.data == "Manzil.":
# #         bot.send_message(call.message.chat.id, "Andijon viloyati, Asaka tumani, Huzur kafesi ro'parasida")

# #     elif call.data == "Gruppa.":
# #         bot.send_message(call.message.chat.id, "salom.uz")

# #     elif call.data == "Admin":
# #         bot.send_message(call.message.chat.id, "name: Ibrohimjonn@User_i01")

# #     elif call.data == "Kurslar":
# #         kurs_markup = types.InlineKeyboardMarkup()
# #         front_end_button = types.InlineKeyboardButton("Front-end", callback_data="front_end")
# #         backend_button = types.InlineKeyboardButton("Backend", callback_data="backend")
# #         rus_tili_button = types.InlineKeyboardButton("Rus tili", callback_data="rus_tili")
# #         ingliz_tili_button = types.InlineKeyboardButton("Ingliz tili", callback_data="ingliz_tili")
        
# #         kurs_markup.add(front_end_button, backend_button, rus_tili_button, ingliz_tili_button)
# #         bot.send_message(call.message.chat.id, "Tanlang:", reply_markup=kurs_markup)

# #     elif call.data == "front_end":
# #         bot.send_message(call.message.chat.id, "Siz Front-end ni tanladingiz!!!")
    
# #     elif call.data == "backend":
# #         bot.send_message(call.message.chat.id, "Siz Back-end ni tanladingiz!!!")
    
# #     elif call.data == "rus_tili":
# #         bot.send_message(call.message.chat.id, "Rus tilini tanladingiz!!!")

# #     elif call.data == "ingliz_tili":
# #         bot.send_message(call.message.chat.id, "Ingliz tilini tanladingiz!!!")

# #     elif call.data == "Yozilish":
# #         msg = bot.send_message(call.message.chat.id, "Ismingizni kiriting:")
# #         bot.register_next_step_handler(msg, get_surname)

# # def get_surname(message):
# #     surname = message.text
# #     msg = bot.send_message(message.chat.id, "Familyangizni kiriting:")
# #     bot.register_next_step_handler(msg, get_age, surname)

# # def get_age(message, surname):
# #     age = message.text
# #     msg = bot.send_message(message.chat.id, "Yoshingizni kiriting:")
# #     bot.register_next_step_handler(msg, get_phone_number, surname, age)

# # def get_phone_number(message, surname, age):
# #     phone_number = message.text
# #     if len(phone_number) != 9 or not phone_number.isdigit():
# #         msg = bot.send_message(message.chat.id, "Telefon raqamingiz:\n979717707")
# #         bot.register_next_step_handler(msg, get_phone_number, surname, age)
# #     else:
 
# #         bot.send_message(message.chat.id, f"Ism: {message.text}\nFamiliya: {surname}\nYosh: {age}nTelefon raqami: {phone_number}")

# # if __name__ == "__main__":
# #     bot.polling(none_stop=True)
# # """

# # # uyga vazifa 
# # # N2


# # # from telebot import types
# # # import telebot

# # # bot = telebot.TeleBot(token='8107222562:AAGGWWUbqDzo8zBugoqkJ75rSbAarBlDf2Y')

# # # @bot.message_handler(content_types=["text"])
# # # def main(message):
# # #     markup = types.InlineKeyboardMarkup()
# # #     b1 = types.InlineKeyboardButton("Manzil.", callback_data="Manzil.")
# # #     b2 = types.InlineKeyboardButton("Gruppa.", callback_data="Gruppa.")
# # #     b3 = types.InlineKeyboardButton("Admin", callback_data="Admin")
# # #     b4 = types.InlineKeyboardButton("Kurslar", callback_data="Kurslar")
# # #     b5 = types.InlineKeyboardButton("Yozilish", callback_data="Yozilish")
# # #     markup.add(b1, b2, b3, b4, b5)

# # #     if message.text == "/start":
# # #         bot.send_message(message.chat.id, "Xush kelibsiz!", reply_markup=markup)

# # # @bot.callback_query_handler(func=lambda call: True)
# # # def h(call):
# # #     if call.data == "Manzil.":
# # #         bot.send_message(call.message.chat.id, "🏘 Manzil: Asaka shahar,Umid ko'chasi 45-uy.\nMo'ljal: Huzur kafesi ro'parasida.")

# # #     elif call.data == "Gruppa.":
# # #         bot.send_message(call.message.chat.id, "Group: https://t.me/LITECH_IT_Academy\nChannel: https://t.me/litech_itacademy")

# # #     elif call.data == "Admin":
# # #         bot.send_message(call.message.chat.id, "Admin:@User_i01")

# # #     elif call.data == "Kurslar":
# # #         kurs_markup = types.InlineKeyboardMarkup()
# # #         front_end_button = types.InlineKeyboardButton("Front-end", callback_data="front_end")
# # #         backend_button = types.InlineKeyboardButton("Backend", callback_data="backend")
# # #         rus_tili_button = types.InlineKeyboardButton("Rus tili", callback_data="rus_tili")
# # #         ingliz_tili_button = types.InlineKeyboardButton("Ingliz tili", callback_data="ingliz_tili")
        
# # #         kurs_markup.add(front_end_button, backend_button, rus_tili_button, ingliz_tili_button)
# # #         bot.send_message(call.message.chat.id, "Tanlang:", reply_markup=kurs_markup)

# # #     elif call.data == "front_end":
# # #         bot.send_message(call.message.chat.id, "Siz Front-end ni tanladingiz!!!")
    
# # #     elif call.data == "backend":
# # #         bot.send_message(call.message.chat.id, "Siz Back-end ni tanladingiz!!!")
    
# # #     elif call.data == "rus_tili":
# # #         bot.send_message(call.message.chat.id, "Rus tilini tanladingiz!!!")

# # #     elif call.data == "ingliz_tili":
# # #         bot.send_message(call.message.chat.id, "Ingliz tilini tanladingiz!!!")

# # #     elif call.data == "Yozilish":
# # #         msg = bot.send_message(call.message.chat.id, "Ismingizni kiriting:")
# # #         bot.register_next_step_handler(msg, get_surname)

# # # def get_surname(message):
# # #     surname = message.text
# # #     msg = bot.send_message(message.chat.id, "Familyangizni kiriting:")
# # #     bot.register_next_step_handler(msg, get_age, surname)

# # # def get_age(message, surname):
# # #     age = message.text
# # #     msg = bot.send_message(message.chat.id, "Yoshingizni kiriting:")
# # #     bot.register_next_step_handler(msg, get_phone_number, surname, age)

# # # def get_phone_number(message, surname, age):
# # #     phone_number = message.text
# # #     if len(phone_number) != 9 or not phone_number.isdigit():
# # #         msg = bot.send_message(message.chat.id, "Telefon raqamingiz: 977967607")
# # #         bot.register_next_step_handler(msg, get_phone_number, surname, age)
# # #     else:
# # #         admin_chat_id = '6495169271' 
# # #         bot.send_message(admin_chat_id, f"Ism: {message.text}\nFamiliya: {surname}\nYosh: {age}\nTelefon raqami: {phone_number}\nYozilish yakunlandi!")

# # # if __name__ == "__main__":
# # #     bot.polling(none_stop=True)

# # '''
# # 18.11.2024-yil.
# # Mavzu: Telegram bot yaratish

# # '''


# # import telebot

# # bot = telebot.TeleBot(token='7738243272:AAEGWIY4U3uxJGpXDSaDlFm8T_uxPEGfEWI')

# # @bot.message_handler(commands=["start"])
# # def start(message):
# #     msg = bot.send_message(message.chat.id, "Ismingizni kiriting:")
# #     bot.register_next_step_handler(msg, get_surname)

# # def get_surname(message):
# #     name = message.text
# #     if not name.isalpha():
# #         msg = bot.send_message(message.chat.id, "faqat harflardan iborat ism kiriting:")
# #         bot.register_next_step_handler(msg, get_surname)
# #     else:
# #         msg = bot.send_message(message.chat.id, "Familyangizni kiriting:")
# #         bot.register_next_step_handler(msg, lambda m: p(m, name))

# # def p(message, name):
# #     surname = message.text
# #     if not surname.isalpha():
# #         msg = bot.send_message(message.chat.id, "faqat harflardan iborat familiya kiriting:")
# #         bot.register_next_step_handler(msg, lambda m: p(m, name))
# #     else:
# #         msg = bot.send_message(message.chat.id, "Telefon raqamingizni kiriting(970707707):")
# #         bot.register_next_step_handler(msg, lambda m: f(m, name, surname))

# # def f(message, name, surname):
# #     phone_number = message.text
# #     if len(phone_number) != 9 or not phone_number.isdigit():
# #         msg = bot.send_message(message.chat.id, "Iltimos, to'g'ri telefon raqamini kiriting (9 ta raqam):")
# #         bot.register_next_step_handler(msg, lambda m: f(m, name, surname))
# #     else:
# #         bot.send_message(message.chat.id, f"Yozilish yakunlandi!\nIsm: {name}\nFamiliya: {surname}\nTelefon raqami: {phone_number}")

# # bot.polling(none_stop=True)

# '''

# 21.11.2024-yil.
# Mavzu: kirituvchiga user name ni qaytarish.

# '''

# import telebot

# bot = telebot.TeleBot(token='7738243272:AAEGWIY4U3uxJGpXDSaDlFm8T_uxPEGfEWI')
# ibrohim_id = 6495169271

# @bot.message_handler(commands=['start'])
# def main(message):
#     name_msg = bot.send_message(message.chat.id, "Ismingizni kiriting:")
#     bot.register_next_step_handler(name_msg, get_name)

# def get_name(message):
#     name = message.text
#     age_msg = bot.send_message(message.chat.id, "Yoshingizni kiriting:")
#     bot.register_next_step_handler(age_msg, get_age, name)

# def get_age(message, name):
#     age = message.text
#     choice_msg = bot.send_message(message.chat.id, "Ish yoki o'qish tanlang:\n1. Ish\n2. O'qish")
#     bot.register_next_step_handler(choice_msg, choose_option, name, age)

# def choose_option(message, name, age):
#     option = message.text
#     if option == "1" or option.lower() == "ish":
#         work_msg = bot.send_message(message.chat.id, "Qayerda ishlaysiz?")
#         bot.register_next_step_handler(work_msg, get_work_place, name, age)
#     elif option == "2" or option.lower() == "o'qish":
#         study_msg = bot.send_message(message.chat.id, "Qayerda o'qiysiz?")
#         bot.register_next_step_handler(study_msg, get_study_place, name, age)
#     else:
#         bot.send_message(message.chat.id, " 'Ish' yoki 'O'qish' deb yozing.")
#         choose_option(message, name, age)

# def get_work_place(message, name, age):
#     work_place = message.text
#     bot.send_message(ibrohim_id, f"Yangi foydalanuvchi: {name}, Yosh: {age}, Ish joyi: {work_place}")
#     bot.send_message(message.chat.id, f"Salom, {name}! Sizning ismingiz va ish joyingizni qabul qildik.")

# def get_study_place(message, name, age):
#     study_place = message.text
#     bot.send_message(ibrohim_id, f"Yangi foydalanuvchi: {name}, Yosh: {age}, O'qish joyi: {study_place}")
#     bot.send_message(message.chat.id, f"Salom, {name}! Sizning ismingiz va o'qish joyingizni qabul qildik.")

# bot.polling(non_stop=True)

"""import telebot
from telebot import types

bot = telebot.TeleBot(token="7738243272:AAEGWIY4U3uxJGpXDSaDlFm8T_uxPEGfEWI")
print("run")
@bot.message_handler(commands=['start'])
def main(message):
    name = bot.send_message(message.chat.id, "ism :")
    bot.register_next_step_handler(name, get_name)

def get_name(message):
    global name
    name = message.text
    if name.isalpha():
        lname = bot.send_message(message.chat.id, "lname: ")
        bot.register_next_step_handler(lname, get_lname)

    else:
        again_name = bot.send_message(message.chat.id, "ism :")
        bot.register_next_step_handler(again_name, main)
        
def get_lname(message):
    global lname
    lname = message.text
    if lname.isalpha():
    
        m = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton("xa", callback_data="xa")
        b2 = types.InlineKeyboardButton("yo'q", callback_data="yoq")
        m.add(b1,b2)
        bot.send_message(message.chat.id, f"malumotlar togrimi\n{name} - {lname}", reply_markup=m)

    else:
        again_lname = bot.send_message(message.chat.id, "lname :")
        bot.register_next_step_handler(again_lname, get_name)

@bot.callback_query_handler(func=lambda call:True)
def check_data(call):
    if call.data == "xa":
        send_message_fun(call.message)
    else:
        bot.send_message(call.message.chat.id, "xayer")

    
def send_message_fun(message):
    global name, lname
    bot.send_message(6495169271, 
                     f"ism {name} familiya {lname}")

bot.polling(non_stop=True)
"""


'''
27.11.2024-yil.
Mavzu: youtobe dan video yuklovchi bot yasash.
'''
'''
import yt_dlp

url = 'https://youtube.com/shorts/XsG5Mz-iR3c?si=-UprVT9jMaSsdYRc'

options = {
    'format': 'best',  
    'outtmpl': 'video.%(ext)s',
    }

with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([url])

print("Видео успешно скачано!")
'''

"""import telebot
import yt_dlp

bot = telebot.TeleBot(token="7934592958:AAEMJ1qmkI2ZzNgCJLWIxwrRYtXdKWsThn8")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "YouTube dagi videoning linkini yuboring!")

@bot.message_handler(func=lambda message: True)
def download_video(message):
    url = message.text.strip()  
    if "youtube.com" not in url and "youtu.be" not in url:
        bot.reply_to(message, "Faqat YouTube havolasini yuboring.")
        return

    bot.reply_to(message, "Videoni yuklab olishni boshladim...")
    options = {
        'format': 'best',  
        'outtmpl': '%(title)s.%(ext)s'
    }

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            info = ydl.extract_info(url, download=True)
            video_file = ydl.prepare_filename(info)  

        with open(video_file, 'rb') as video:
            bot.send_video(message.chat.id, video)

    except Exception as e:
        bot.reply_to(message, f"Xato yuz berdi: {e}")

bot.polling()

"""



# N2=> 7211537013:AAG_keMmKErz0Ax-f3D0BVeL0ZvLYVPUT3o
"""
# import telebot

# bot = telebot.TeleBot(token='7211537013:AAG_keMmKErz0Ax-f3D0BVeL0ZvLYVPUT3o')

# @bot.message_handler(content_types=["text"])
# def main(message):
#     if message.text == "/start":
#         markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
#         b1 = telebot.types.KeyboardButton("Car game")
#         b2 = telebot.types.KeyboardButton("Boxing")
#         b3 = telebot.types.KeyboardButton("Karate")


#         markup.add(b1, b2, b3)

#         bot.send_message(message.chat.id, "Tanlang:", reply_markup=markup)
    
#     elif message.text == "Car game":
#         bot.send_message(message.chat.id, "https://poki.com/ru/g/blaze-drifter")
    
#     elif message.text == "Boxing":
#         bot.send_message(message.chat.id, "https://poki.com/ru/g/punch-legend-simulator")
    
#     elif message.text == "Karate":
#         bot.send_message(message.chat.id, "https://poki.com/ru/g/irrational-karate")
    
# bot.polling()
# """


import telebot

bot = telebot.TeleBot(token='7211537013:AAG_keMmKErz0Ax-f3D0BVeL0ZvLYVPUT3o')

@bot.message_handler(commands=["start"])
def main(message):
    markup = telebot.types.InlineKeyboardMarkup()
    b1 = telebot.types.InlineKeyboardButton("Car game", url='https://poki.com/ru/g/blaze-drifter')
    b2 = telebot.types.InlineKeyboardButton("Boxing", url='https://poki.com/ru/g/punch-legend-simulator')
    b3 = telebot.types.InlineKeyboardButton("Karate", url='https://poki.com/ru/g/irrational-karate')
    markup.add(b1, b2, b3)

    bot.send_message(message.chat.id, "Tanlang:", reply_markup=markup)

bot.polling()




# import telebot
# import yt_dlp

# bot = telebot.TeleBot(token="7934592958:AAEMJ1qmkI2ZzNgCJLWIxwrRYtXdKWsThn8")

# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.reply_to(message, "YouTube dagi videoning linkini yuboring!")

# @bot.message_handler(func=lambda message: True)
# def download_video(message):
#     url = message.text.strip()  
#     if "youtube.com" not in url and "youtu.be" not in url:
#         bot.reply_to(message, "Faqat YouTube havolasini yuboring.")
#         return

#     bot.reply_to(message, "Videoni yuklab olishni boshladim...")
#     options = {
#         'format': 'best',  
#         'outtmpl': '%(title)s.%(ext)s'
#     }

#     try:
#         with yt_dlp.YoutubeDL(options) as ydl:
#             info = ydl.extract_info(url, download=True)
#             video_file = ydl.prepare_filename(info)  

#         with open(video_file, 'rb') as video:
#             bot.send_video(message.chat.id, video)

#     except Exception as e:
#         bot.reply_to(message, f"Xato yuz berdi: {e}")

# bot.polling()