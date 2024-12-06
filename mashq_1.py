
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






import telebot
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
