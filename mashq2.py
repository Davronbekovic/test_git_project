
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
