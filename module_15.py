### Чтение и запись в файлы ###

myfile = open('filename.txt')
myfile = open('filename.txt', 'rt')
myfile = open('filename.txt', 'rt', encoding='utf8')

# Метод read() — сохраняет всё содержимое файла как строку.
myfile = open('filename.txt')
print(myfile.read())

# Если в метод read() передать число, то вернётся указанное число символов.
print(myfile.read(20))

# Метод readline() читает файл построчно.
# В него можно передавать число, и из строки будет прочитано указанное число символов.
# Важно! Как только мы применили этот метод, то повторное его применение выдаст вторую строку, ещё одно —
# третью строку и так далее.
myfile = open('filename.txt')
print(myfile.readline())

# Метод readlines() вернёт список, в котором элементами будут строки из файла.
print(myfile.readlines())

# Самый часто используемый в реальности способ — чтение файла построчно в цикле for.
myfile = open('filename.txt')
for line in myfile:
    print(line)

# Фактически есть только два способа записи информации в файл — это метод write() и функция print().
myfile = open('namefilename.txt', 'w')
myfile.write('tttt')
print('zzzz', file=myfile)

# Метод flush() сразу говорит интерпретатору записать данные в файл.
# Метод close() вызывает внутри себя метод flush() и закрывает файл.

# Оператор with работает так:

# Ключевое слово with.
# Открытие файла с помощью функции open(), так как мы разбирали выше.
# Ключевое слово as.
# Имя, с которым будет ассоциирован открытый файл.
# Двоеточие.
# Блок кода, отделенный четырьмя пробелами, по аналогии с циклами и функциями.
with open('filename.txt') as myfile:
    for line in myfile:
        print(line)


# Задача: пользователь вводит произвольное целое число, а программа читает некий русский текст из файла и
# зашифровывает его в другой файл со сдвигом, соответствующим этому числу.
alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphaUp = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
number = int(input('Введите число, на которое нужно сдвинуть текст: '))

summary = ''


def changeChar(char):
    if char in alpha:
        return alpha[(alpha.index(char) + number) % len(alpha)]
    elif char in alphaUp:
        return alphaUp[(alphaUp.index(char) + number) % len(alphaUp)]
    else:
        return char


with open("filename2.txt", encoding="utf8") as myFile:
    for line in myFile:
        for char in line:
            summary += changeChar(char)

with open("output.txt", 'w', encoding="utf8") as myFile:
    myFile.write(summary)

# Абсолютный путь
myfile = open(r'C:\Users\Vova\QAP\test\filename.txt', 'rt', encoding="utf8")

# Модуль os в Python содержит функции и методы для работы с операционной системой. В этом модуле в данном контексте
# нас интересует вложенный в него модуль os.path, предназначенный для работы с путями.
import os

print(os.path.join('..', 'test', 'filename.txt'))

# Задача звучит следующим образом:
# Есть файл, в котором задан лабиринт.
# В этом лабиринте буквой А отмечен вход. Буквой В отмечен выход, 0 — свободный проход, 1 — непроходимая стена.
# Нужно составить и вывести на экран последовательность шагов (вверх, вниз, вправо, влево), которая приведет
# из точки А в точку В.

# Идея в том, что начальной точке ставится вес — единица, затем от нее проверяется, можно ли пойти налево,
# направо, вверх или вниз и в те места, где можно ставится вес на единицу больше. Затем перемещаем начальную
# точку туда, куда мы смогли походить, и проверяем еще раз.

# В итоге мы получаем лабиринт, в котором -1 — это непроходимая стена, а остальные — это веса, которые символизируют,
# за сколько шагов можно достичь этого места от начала лабиринта. Соответственно, путь строится от обратного:
# точка с выходом принимается за начальную, и путь идет ровно по уменьшению веса — это будет минимально короткий
# выход из лабиринта.

def found(pathArr, finPoint):
    weight = 1
    for i in range(len(pathArr) * len(pathArr[0])):
        for y in range(len(pathArr)):
            for x in range(len(pathArr[y])):
                if pathArr[y][x] == weight:
                    # Вниз
                    if y > 0 and pathArr[y - 1][x] == 0:
                        pathArr[y - 1][x] = weight + 1

                        # Вверх
                    if y < (len(pathArr) - 1) and pathArr[y + 1][x] == 0:
                        pathArr[y + 1][x] = weight + 1

                    # Вправо
                    if x > 0 and pathArr[y][x - 1] == 0:
                        pathArr[y][x - 1] = weight + 1

                    # Влево
                    if x < (len(pathArr[y]) - 1) and pathArr[y][x + 1] == 0:
                        pathArr[y][x + 1] = weight + 1

                    # Конечная точка
                    if (abs(y - finPoint[0]) + abs(x - finPoint[1])) == 1:
                        pathArr[finPoint[0]][finPoint[1]] = weight + 1
                        return True
        weight += 1
    return False


def printPath(pathArr, finPoint):
    y = finPoint[0]
    x = finPoint[1]
    weight = pathArr[y][x]
    result = list(range(weight))
    while (weight):
        weight -= 1
        if y > 0 and pathArr[y - 1][x] == weight:
            result[weight] = 'Вниз'
            y -= 1
        elif y < (len(pathArr) - 1) and pathArr[y + 1][x] == weight:
            result[weight] = 'Вверх'
            y += 1
        elif x > 0 and pathArr[y][x - 1] == weight:
            result[weight] = 'Вправо'
            x -= 1
        elif x < (len(pathArr[y]) - 1) and pathArr[y][x + 1] == weight:
            result[weight] = 'Влево'
            x += 1

    return result[1:]


labirint = []
with open("labirint.txt") as myFile:
    for line in myFile:
        labirint.append(line.replace('\n', '').split(' '))

ii = 0
for i in labirint:
    jj = 0
    for j in i:
        if j == 'A':
            labirint[ii][jj] = 1
            pozIn = (ii, jj)
        elif j == 'B':
            labirint[ii][jj] = 0
            pozOut = (ii, jj)
        elif j == '1':
            labirint[ii][jj] = -1
        else:
            labirint[ii][jj] = 0
        jj += 1
    ii += 1

if not found(labirint, pozOut):
    print("Путь не найден!")
else:
    result = printPath(labirint, pozOut)

    for i in labirint:
        for line in i:
            print("{:^3}".format(line), end=" ")
        print()
    print(result)


### Работа с JSON файлами ###

# Шаги простые:

# Импортируем модуль JSON.
# Открываем файл на чтение (не забываем прописать encoding, так как в файле имеются русские буквы).
# Присваиваем переменной результат работы метода load() из модуля JSON.
# Результат — это словарь
import json

with open('json_example.json', encoding='utf8') as f:
    templates = json.load(f)

print(templates)
print(type(templates))
# {'firstname': 'Иван', 'lastname': 'Иванов', 'isAlive': True, 'age': 32, 'address': {'streetAddress': 'Нейбута 32',
# 'city': 'Владивосток', 'state': '', 'postalcode': ''}, 'phoneNumbers': [{'type': 'mob', 'number': '123-333-4455'},
# {'type': 'office', 'number': '123 111-4567'}], 'children': [], 'spouse': None}

# Существует метод loads(), который считывает не файл, а строку.
import json

with open('json_example.json', encoding='utf8') as f:
    strfile = f.read()
    templates = json.loads(strfile)

print(templates)
print(type(templates))
# {'firstname': 'Иван', 'lastname': 'Иванов', 'isAlive': True, 'age': 32, 'address': {'streetAddress': 'Нейбута 32',
# 'city': 'Владивосток', 'state': '', 'postalcode': ''}, 'phoneNumbers': [{'type': 'mob', 'number': '123-333-4455'},
# {'type': 'office', 'number': '123 111-4567'}], 'children': [], 'spouse': None}

# Аналогично существуют два варианта преобразования словаря в Python в JSON — метод dump() и dumps().
# Первый записывает файл, а второй — строку.

# ensure_ascii указываем для того, чтобы русские буквы оставались русскими при передаче.
# indent — для того, чтобы запись была красивая и человекочитаемая с отступами и переводами строк.
import json

template = {
    'firstname': 'Иван',
    'lastname': 'Иванов',
    'isAlive': True,
    'age': 32,
    'address': {
        'streetAddress': 'Нейбута 32',
        'city': 'Владивосток',
        'state': '',
        'postalcode': ''
    },
    'phoneNumbers': [
        {
            'type': 'mob',
            'number': '123-333-4455'
        },
        {
            'type': 'office',
            'number': '123 111-4567'
        }
    ],
    'children': [],
    'spouse': None
}

with open('to_json_example.json', 'w', encoding='utf8') as f:
    json.dump(template, f, ensure_ascii=False, indent=4)

with open('to_json_example.json', encoding='utf8') as f:
    print(f.read())
# {
#     "firstname": "Иван",
#     "lastname": "Иванов",
#     "isAlive": true,
#     "age": 32,
#     "address": {
#         "streetAddress": "Нейбута 32",
#         "city": "Владивосток",
#         "state": "",
#         "postalcode": ""
#     },
#     "phoneNumbers": [
#         {
#             "type": "mob",
#             "number": "123-333-4455"
#         },
#         {
#             "type": "office",
#             "number": "123 111-4567"
#         }
#     ],
#     "children": [],
#     "spouse": null
# }
