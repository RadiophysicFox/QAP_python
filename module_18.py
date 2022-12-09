### Библиотека Requests и её лучший друг JSON ###

import requests

r = requests.get(
    'https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')  # делаем запрос на сервер по переданному адресу
print(r.content)
print(r.status_code)  # узнаем статус полученного ответа

# Попробуем с помощью той же библиотеки Requests обращаться по адресу.
import requests

r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')  # попробуем поймать json ответ
print(r.content)

# Поменяем наш код и превратим данный текст в список, на который он так сильно похож.
import requests
import json  # импортируем необходимую библиотеку

r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
texts = json.loads(r.content)  # делаем из полученных байтов python объект для удобной работы
print(type(texts))  # проверяем тип сконвертированных данных

for text in texts:  # выводим полученный текст. Но для того чтобы он влез в консоль оставим только первые 50 символов.
    print(text[:50], '\n')

# Это тоже будет JSON, но в данном случае он, скорее, будет похож на словарь.
import requests
import json

r = requests.get('https://api.github.com')

print(r.content)

# Давайте всё же теперь сделаем его настоящим словарём.
import requests
import json

r = requests.get('https://api.github.com')

d = json.loads(r.content)  # делаем из полученных байтов python объект для удобной работы

print(type(d))
print(d['following_url'])  # обращаемся к полученному объекту как к словарю и попробуем напечатать одно из его значений

# Давайте попробуем отправить post-запрос:
import requests

r = requests.post('https://httpbin.org/post', data={'key': 'value'})  # отправляем пост запрос
print(r.content)  # содержимое ответа и его обработка происходит так же, как и с гет-запросами, разницы никакой нет

# Давайте посмотрим, как с помощью уже знакомой нам библиотеки отправить данные в нужном нам формате:
import requests
import json

data = {'key': 'value'}

r = requests.post('https://httpbin.org/post', json=json.dumps(
    data))  # отправляем пост запрос, но только в этот раз тип передаваемых данных будет JSON
print(r.content)

# Команды для бота
@bot.message_handler(filters)
def function_name(message):
    bot.reply_to(message, "This is a message handler")


import telebot

bot = telebot.TeleBot("TOKEN")


# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    pass


# Обрабатываются все документы и аудиозаписи
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    pass


# Допишите обработчик так, чтобы он из сообщения брал username и выдавал приветственное сообщение с привязкой к
# пользователю.
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Welcome, \ c{message.chat.username}")


# Напишите обработчик, который на сообщения с фотографией будет отвечать сообщением «Nice meme XDD». Бот должен
# отвечать не отдельным сообщением, а с привязкой к картинке.
import telebot

bot = telebot.TeleBot('TOKEN')


@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')


bot.polling(none_stop=True)


### Парсинг данных с сайтов с помощью lxml ###
import requests  # импортируем наш знакомый модуль
import lxml.html
from lxml import etree

html = requests.get('https://www.python.org/').content  # получим html главной странички официального сайта Python

tree = lxml.html.document_fromstring(html)
title = tree.xpath(
    '/html/head/title/text()')  # забираем текст тега <title> из тега <head> который лежит в свою очередь внутри тега <html> (в этом невидимом теге <head> у нас хранится основная информация о страничке. Её название и инструкции по отображению в браузере.

print(title)  # выводим полученный заголовок страницы


import requests  # импортируем наш знакомый модуль
import lxml.html
from lxml import etree

# создадим объект ElementTree. Он возвращается функцией parse()
tree = etree.parse('Welcome to Python.org.html',
                   lxml.html.HTMLParser())  # попытаемся спарсить наш файл с помощью HTML-парсера. Сам HTML — это то, что мы скачали и поместили в папку из браузера.

ul = tree.findall(
    'body/div/div[3]/div/section/div[3]/div[1]/div/ul/li')  # помещаем в аргумент методу findall скопированный xpath. Здесь мы получим все элементы списка новостей. (Все заголовки и их даты)

# создаём цикл? в котором будем выводить название каждого элемента из списка
for li in ul:
    a = li.find(
        'a')  # в каждом элементе находим, где хранится заголовок новости. У нас это тег <a>. Т.е. гиперссылка, на которую нужно нажать, чтобы перейти на страницу с новостью. Гиперссылки в HTML — это всегда тэг <a>.
    print(a.text)  # из этого тега забираем текст — это и будет нашим названием


# Напишите программу, которая будет с помощью парсера lxml доставать текст из тега tag2 следующего HTML:
import lxml.html

html = ''' <html>
 <head> <title> Some title </title> </head>
 <body>
  <tag1> some text
     <tag2> MY TEXT </tag2>
   </tag1>
 </body>
</html>
'''

tree = lxml.html.document_fromstring(html)

text = tree.xpath('/html/body/tag1/tag2/text()')

print(text)


# Используя полученные знания, допишите сделанный в начале юнита скрипт (где мы доставали заголовки новостей о
# Python с Python.org) так, чтобы он показывал ещё и дату добавления новости.
import requests  # импортируем наш знакомый модуль
import lxml.html
from lxml import etree

html = requests.get('https://www.python.org/').content  # получим html главной странички официального сайта python

# создадим объект ElementTree. Он возвращается функцией parse()
tree = etree.parse('Welcome to Python.org.html',
                   lxml.html.HTMLParser())  # попытаемся спарсить наш файл с помощью html парсера

ul = tree.findall(
    'body/div/div[3]/div/section/div[3]/div[1]/div/ul/li')  # помещаем в аргумент методу findall скопированный xpath

# создаём цикл в котором мы будем выводить название каждого элемента из списка
for li in ul:
    a = li.find('a')  # в каждом элементе находим где хранится название. У нас это тег <a>
    time = li.find('time')
    print(time.get('datetime'), a.text)  # из этого тега забираем текст - это и будет нашим названием


### Кэширование с помощью Redis ###
# Кэширование — это временное сохранение данных для дальнейшего доступа к ним.

# Запишем в кэш словарь:
import redis
import json

red = redis.Redis(
    host='хост',
    port=порт,
    password='пароль'
)

dict1 = {'key1': 'value1', 'key2': 'value2'}  # создаём словарь для записи
red.set('dict1', json.dumps(dict1))  # с помощью функции dumps() из модуля json превратим наш словарь в строчку
converted_dict = json.loads(
    red.get('dict1'))  # с помощью знакомой нам функции превращаем данные полученные из кэша обратно в словарь
print(type(converted_dict))  # убеждаемся, что получили действительно словарь
print(converted_dict)  # ну и выводим его содержание

# Научимся удалять данные из кэша по ключу
import redis
import json

red = redis.Redis(
    host='хост',
    port=порт,
    password='пароль'
)

red.delete('dict1')  # удаляются ключи с помощью метода .delete()
print(red.get('dict1'))

