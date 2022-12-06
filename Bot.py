import telebot

TOKEN = "5912300558:AAH8A9uZ1KUyEreLgkrWWP3PBgcwIjYMewA"

bot = telebot.TeleBot(TOKEN)

# Чтобы запустить бота, нужно воспользоваться методом polling.
bot.polling(none_stop=True)

# Параметр none_stop=True говорит, что бот должен стараться не прекращать работу при возникновении каких-либо ошибок.

