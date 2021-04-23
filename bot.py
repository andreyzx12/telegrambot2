import telebot
bot = telebot.TeleBot('1780171105:AAFYBSbsBC2t9kr4qSZX4m8_M9JBq1CeQH8')

@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()