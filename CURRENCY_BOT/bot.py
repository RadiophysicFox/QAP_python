import telebot
from config import TOKEN, keys
from extensions import APIException, CurrencyConverter


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате:\n<имя валюты> \
 <в какую валюту перевести> \
 <количество переводимой валюты>\nУвидеть список всех доступных валют: /values\n\
 Все валюты вводить в нижнем регистре'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def get_price(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise APIException('Слишком много параметров.')

        base, quote, amount = values
        total_base = CurrencyConverter.get_price(base, quote, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду.\n{e}')
    else:
        result = float(amount) * float(total_base)
        if base == 'рубль':
            numbers = [10, 11, 12, 13, 14]
            remainder = [1, 2, 3, 4]
            if float(amount) == 1 or float(amount) % 10 in remainder and float(amount) not in numbers:
                currency_in = 'рубля'
            else:
                currency_in = 'рублей'
        elif base == 'доллар':
            if float(amount) == 1 or float(amount) % 10 == 1 and float(amount) != 11:
                currency_in = 'доллара'
            else:
                currency_in = 'долларов'
        else:
            currency_in = 'евро'
        if quote == 'рубль':
            currency_out = 'рублях'
        elif quote == 'доллар':
            currency_out = 'долларах'
        else:
            currency_out = 'евро'

        text = f'Цена {amount} {currency_in} в {currency_out} - {result}'
        bot.send_message(message.chat.id, text)


bot.polling()
