### Логические операторы ###

# Логическое «НЕ»
print(not True)
# False

print(not False)
# True

# Логическое «И»
# можно проверить, находится ли число 1 в промежутке (0,4)
cond1 = 0 < 1
cond2 = 1 < 4

print(cond1 and cond2)
# True

# или, например, содержат ли две строки один и тот же символ
cond3 = 't' in "python"
cond4 = 't' in "django"

print(cond3 and cond4)
# False

# Логическое «ИЛИ»
# к слову, логические выражения можно сразу объединять в одно целое
print(('t' in "python") or ('t' in "django"))
# True

### Проверка вхождения элемента в последовательность ###

# Применим такую хитрость, что сначала мы переведем число в строку, а потом в список, и посмотрим,
# что будет в итоге:

print(list(str(123456789)))
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# Мы с вами получили последовательность цифр числа в виде списка, потому что если строку перевести в список,
# то она разбивается на отдельные символы. Теперь нужно перевести каждый элемент списка обратно в число.
# Для этого есть map:
print(list(map(int, ['1', '2', '3', '4', '5', '6', '7', '8', '9'])))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Теперь, когда мы получили список всех цифр, можно проверить, содержится ли среди них цифра 5:
list_digit = list(map(int, list(str(123456789))))
print(5 in list_digit)
# True

# Но на самом деле эту задачу можно было решить намного проще:
print('5' in str(123456789))
# True

# Дано n-значное целое число N. Определите, входят ли в него цифры 3 и 7.
print(('5' in str(N)) and ('7' in str(N)))

### Простой условный оператор ###
is_rainy = True  # дождь будет

if is_rainy:
    print("Брать зонт")
else:
    print("Не брать зонт")

### Вложенные условные операторы ###
is_rainy = True  # дождь будет
heavy_rain = False  # не сильный дождь

if is_rainy:
    # в данный блок дописали ещё один условный оператор
    if heavy_rain:
        print("Брать зонт")
    else:
        print("Надеть дождевик")
else:
    print("Не брать зонт")

### Неявное приведение к булеву типу ###

# Чтобы проверить, к чему будет приведен тот или иной тип,  можете воспользоваться встроенной функцией bool:

print(bool(0))  # False
print(bool(1))  # True

print(bool(""))  # False
print(bool("1"))  # True

print(bool([]))  # False
print(bool([1]))  # True

# Если ваша задача проверить, можно ли делить, и является ли делитель нулём, то проверку в
# явном виде zero != 0 делать излишне.

# Плохо
if zero != 0:
   print(10 / zero)
else:
   print("Делить на ноль нельзя")

# Хорошо
if zero:
   print(10 / zero)
else:
   print("Делить на ноль нельзя")

# Если вам нужно проверить, пустая строка или нет, то сравнивать её способом password == "", а уж тем
# более способом len(password) == 0 ни к чему.

# Плохо
if password == "":
   print("Вы забыли ввести пароль")
else:
   ...

# Очень плохо
if len(password) == 0:
   print("Вы забыли ввести пароль")
else:
   ...

# Хорошо
if not password:
   print("Вы забыли ввести пароль")
else:
   ...


### Исключения ###

# Как же сделать так, чтобы программа не вылетала при ошибке и продолжала свою работу?
# Для этого и нужна конструкция try-except.
try:  # Добавляем конструкцию try-except для отлова нашей ошибки
    print("Перед исключением")
    # теперь пользователь сам вводит числа для деления
    a = int(input("a: "))
    b = int(input("b: "))
    c = a / b  # здесь может возникнуть исключение деления на ноль
    print(c)  # печатаем c = a / b если всё хорошо
except ZeroDivisionError as e:  # Добавляем тип именно той ошибки которую хотим отловить.
    print(e)  # Выводим информацию об ошибке
    print("После исключения")

print("После После исключения")

# Есть также блоки finally и else:
try:
    print("Перед исключением")
    a = int(input("a: "))
    b = int(input("b: "))
    c = a / b
    print(c)  # печатаем c = a / b, если всё хорошо
except ZeroDivisionError as e:
    print("После исключения")
else:  # код в блоке else выполняется только в том случае, если код в блоке try выполнился успешно (т.е. не вылетело никакого исключения).
    print("Всё ништяк")
finally:  # код в блоке finally выполнится в любом случае при выходе из try-except
    print("Finally на месте")

print("После После исключения")

# Мы можем вызывать ошибки самостоятельно с помощью конструкции raise:
age = int(input("How old are you?"))

if age > 100 or age <= 0:
    raise ValueError("Тебе не может быть столько лет")

print(f"Тебе {age} лет!")  # Возраст выводится только в случае, если пользователь ввёл правильный возраст.

# Отлавливать вызываемые с помощью raise ошибки тоже можно.
try:
    age = int(input("How old are you?"))
    if age > 100 or age <= 0:
        raise ValueError("Тебе не может быть столько лет")
except ValueError as error:
    print(error)
    print("Неправильный возраст")
else:
    print(f"You are {age} years old!") # Возраст выводится только в случае, если пользователь ввёл правильный возраст.

# Программа:
try:
    a = int(input("Введите значение:"))
except ValueError as error:
    print(error)
    print("Вы ввели неправильное число")
else:
    print("Вы ввели правильное число", a)
finally:
    print("Выход из программы")

# Пример 1. Использование логических операторов с условным оператором.
# Условие задачи. Запишите условие проверки целого числа А, является ли оно кратным двум или трем.
if A % 2 == 0 or A % 3 == 0:
    print('Число А кратно 2 или 3')

# Для последовательностей (строк, списков, кортежей) используйте тот факт, что пустая последовательность
# есть False:
# Хорошо
if not seq:
if seq:

# Плохо
if len(seq)
if not len(seq)

# Примеры
if pozitive_num:  # нет смысла проверять len(pozitive_num)
   # если список не пустой, то печатаем его
   print("Список положительных чисел равен: ", pozitive_num)
else:
   # печатаем, если список оказался пустым
   print("Список положительных чисел пустой")


if not password:  # password строка содержащая пароль, введенный пользователем
   print("Вы забыли ввести пароль! Повторите попытку ещё раз")


# Пример 2. Использование операторов сравнения с условным оператором.
# Условие задачи. Напишите программу для определения того, является ли данное время суток утром. Выведите
# соответствующее сообщение. Утром считается временной промежуток с 6 часов включительно и до 12 часов не
# включительно.
if 6 <= hour < 12:
    print("Утро!!!")

# Пример 3. Использование оператора if-elif-else.
# Условие задачи. Введите с клавиатуры номер месяца. Определите сезон в зависимости от номера месяца и
# выведите сообщение:
# «Весна» для 3, 4, 5 месяца;
# «Лето» для 6, 7, 8 месяца;
# «Осень» для 9, 10, 11 месяца;
# «Зима» для 12, 1, 2 месяца.
month = int(input())

if month in [3, 4, 5]:
    print("Весна")
elif month in [6, 7, 8]:
    print("Лето")
elif month in [9, 10, 11]:
    print("Осень")
elif month in [12, 1, 2]:
    print("Зима")

# Тернарный условный оператор
result = a if a > b else b

# Запишите условие, которое является истинным, когда только одно из чисел А, В и С меньше 45
A = int(input('Введите первое число\n'))
B = int(input('Введите второе число\n'))
C = int(input('Введите третье число\n'))

if ((A < 45) and (B >= 45) and (C >=45)) or \
    ((A >= 45) and (B < 45) and (C >=45)) or \
    ((A >= 45) and (B >= 45) and (C < 45)):
    print('Есть число меньше 45 и только одно')
else:
    print('Числа меньше 45 нет или их несколько')

# Запишите логическое выражение, которое определяет, что число А не принадлежит интервалу от -10 до -1
# или интервалу от 2 до 15.
A = int(input('Введите число\n'))

if not (-10 <= A <= -1 or 2 <= A <= 15):
    print("Число не принадлежит интервалу")
else:
    print("Число принадлежит интервалу")

# Дано двузначное число. Определите, входит ли в него цифра 5. Попробуйте решить задачу с использованием
# целочисленного деления и деления с остатком.
n = 15
first_digit = n // 10
second_digit = n % 10

print((first_digit == 5) or (second_digit == 5))

# Проверьте, все ли элементы в списке являются уникальными.
list_ = [-5, 2, 4, 8, 12, -7, 5]

print(len(list_) == len(set(list_)))

# Дано натуральное восьмизначное число. Выясните, является ли оно палиндромом (читается одинаково слева
# направо и справа налево).
num = 12345678

print(str(num) == str(num)[::-1])

### Цикл For ###

# Пример 1. Найдите сумму всех натуральных чисел от 1 до N включительно.
S = 0  # заводим переменную-счетчик, в которой мы будем считать сумму
N = 5

# заводим цикл for, в котором мы будем проходить по всем числам от одного до N
for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
    print("Значение суммы на предыдущем шаге: ", S)
    print("Текущее число: ", i)
    S = S + i  # cуммируем текущее число i и перезаписываем значение суммы
    print("Значение суммы после сложения: ", S)
    print("---")
print("Конец цикла")
print()
print("Ответ: сумма равна = ", S)

# Пример 2. Найдите произведение всех натуральных чисел от 1 до N включительно.
P = 0  # заводим переменную-счетчик, в которой мы будем считать произведение
N = 5

# заводим цикл for, в котором мы будем проходить по всем числам от одного до N
for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
    print("Значение произведения на предыдущем шаге: ", P)
    print("Текущее число: ", i)
    P *= i  # умножаем текущее число i и перезаписываем значение произведения
    print("Значение произведения после умножения: ", P)
    print("---")
print("Конец цикла")
print()
print("Ответ: произведение равно = ", P)

# Напишите программу, которая будет печатать лесенку
n = int(input("Введите целое число:"))
for i in range(1, n+1):
    print("*" * i)

### Цикл While ###

# Напишите цикл, который будет складывать натуральные числа, пока их сумма не превысит 500.
S = 0  # заводим переменную-счетчик, в которой мы будем считать сумму
n = 1  # текущее натуральное число

# заводим цикл while, который будет работать, пока сумма не превысит 500
while S < 500:  # делай пока ...
    S += n  # увеличиваем сумму, равносильно S = S + n
    n += 1  # так как сумма ещё не достигла нужного значения, то увеличиваем переменную-счетчик
    print("Ещё считаю ...")

print("Сумма равна: ", S)
print("Количество чисел: ", n)

# Напишите цикл с использованием whilе, который возводит числа в квадрат, пока результат меньше 1000.
n = 1
while n ** 2 < 1000:
    n += 1

# Напишите цикл с использованием бесконечного цикла whilе с постусловием, который возводит натуральные
# числа в квадрат, пока результат меньше 1000.
n = 1
while True:
    print(n**2)
    n +=1
    if n**2 > 1000:
        break

### Работа с вложенными циклами ###
N = 2
M = 3
# заполнили матрицу последовательными числами
matrix = [
    [0, 1, 2],
    [3, 4, 5],
]
for i in range(N):
    for j in range(M):
        print(matrix[i][j], end=" ")
    print()  # перенос на новую строку

# 0 1 2
# 3 4 5

# Дана двумерная матрица 3x3. Определите максимум и минимум каждой строки, а также их индексы.
random_matrix = [
    [9, 2, 1],
    [2, 5, 3],
    [4, 8, 5]
]

mean_value_rows = []  # здесь будут храниться средние значения для каждой строки
min_value_rows = []  # здесь будут храниться минимальные значения для каждой строки
min_index_rows = []  # здесь будут храниться индексы минимальных значений для каждой строки
max_value_rows = []  # здесь будут храниться максимальные значения для каждой строки
max_index_rows = []  # здесь будут храниться индексы максимальных значений для каждой строки

for row in random_matrix:  # здесь мы целиком берем каждую сроку
    min_index = 0  # в качестве минимального значения возьмем первый элемент строки
    max_index = 0
    min_value = row[min_index]  # начальное минимальное значение для каждой строки будет новое
    max_value = row[max_index]  # для максимального значения тоже самое
    for index_col in range(len(row)):
        if row[index_col] < min_value:
            min_value = row[index_col]
            min_index = index_col
        if row[index_col] > max_value:
            max_value = row[index_col]
            max_index = index_col
    min_value_rows.append(min_value)
    min_index_rows.append(min_index)
    max_value_rows.append(max_value)
    max_index_rows.append(max_index)

print(min_value_rows)
print(min_index_rows)
print(max_value_rows)
print(max_index_rows)

### Функция enumerate ###
list_ = [-5, 2, 4, 8, 12, -7, 5]
# Функция enumerate возвращает данные в виде кортежей,
# где на первом месте стоит индекс, а затем значение
# [(0, -5), (1, 2), (2, 4), ...]
for i, value in enumerate(list_):
    print("Индекс элемента: ", i)
    print("Значение элемента: ", value)  # с помощью индекса получаем значение элемента
    print("---")
print("Конец цикла")

# Программа, которая находит индекс последнего отрицательного элемента в списке
list_ = [-5, 2, 4, 8, 12, -7, 5]
# Объявим переменную, в которой будем хранить индекс отрицательного элемента
index_negative = None

for i, value in enumerate(list_):
   if value < 0:
       print("Отрицательное число: ", value)
       index_negative = i  # перезаписываем значение индекса
       print("Новый индекс отрицательного числа: ", index_negative)
   else:
       print("Положительное число: ", value)
   print("---")
print("Конец цикла")
print()
print("Ответ: индекс последнего отрицательного элемента = ", index_negative)

### Цикл for со строками и словарями ###
# Условие задачи: С помощью словаря в заданном тексте посчитать количество вхождения каждого символа.
text = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо -- песнь заводит,
Налево -- сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух... там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

text = text.lower()
text = text.replace(" ", "")
text = text.replace("\n", "")
print(text)

count = {}  # для подсчета символов и их количества
for char in text:
   if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
       count[char] += 1
   else:
       count[char] = 1
for char, cnt in count.items():
   print(f"Символ {char} встречается {cnt} раз")

### Break ###
# Проверьте, является ли заданное число степенью тройки
while True:
    if n % 3 == 0:
         n = n // 3
         if n == 1:
              break
    else:
         break

### Continue ###
# В клетке находятся фазаны и кролики. Известно, что у них 35 голов и 94 ноги. Узнайте число фазанов и
# число кроликов.
heads = 35  # количество голов
legs = 94  # количество ног

for r in range(heads + 1):  # количество кроликов
    for ph in range(heads + 1):  # количество фазанов
        #  если суммарное количество голов превышено или ног превышено, то переходим на следующий шаг цикла
        if (r + ph) > heads or \
            (r * 4 + ph * 2) > legs:
            continue
        if (r + ph) == heads and (r * 4 + ph * 2) == legs:
            print("Количество кроликов", r)
            print("Количество фазанов", ph)
            print("---")

### Функции all/any ###
# All возвращает True, если все условия, переданные в аргумент функции в виде списка, являются истинными.
# Any - чтобы был хотя бы один истинный элемент
if all([type(a) == int,
        100 <= a <= 999,
        a % 2 == 0,
        a % 3 == 0]):
    print("Число удовлетворяет условиям")

# Программа, которая на вход принимает последовательность целых чисел, и возвращает True, если все числа
# ненулевые, и False, если хотя бы одно число равно 0.
L = list(map(int, input().split()))

print(all(L))

# Программа, которая на вход принимает последовательность целых чисел и возвращает True, если все числа
# равны нулю, и False, если найдется хотя бы одно ненулевое число.
L = list(map(int, input().split()))
print(not any(L))

### List comprehension ###
# L = [ a for a in some_iter_obj if cond ]

# В список будут включаться квадраты только от нечетных чисел:
squares = [i**2 for i in range(1,11) if i % 2 == 1]
# [1, 9, 25, 49, 81]

# Список из кортежей:
list_tuples = [(i, i**2) for i in range(1,11)]
#[(1, 1),
# (2, 4),
# (3, 9),
# (4, 16),
# (5, 25),
# (6, 36),
# (7, 49),
# (8, 64),
# (9, 81),
# (10, 100)]

# Матрица:
M = [[i+j for j in range(5)] for i in range(5)]
#[[0, 1, 2, 3, 4],
# [1, 2, 3, 4, 5],
# [2, 3, 4, 5, 6],
# [3, 4, 5, 6, 7],
# [4, 5, 6, 7, 8]]

# Пример пять раз запросит у пользователя данные для входа и запишет их в список:
L = [input() for i in range(5)]

# В список сохранялось True, если элемент четный, и False, если элемент нечетный.
L = [int(input()) % 2 == 0 for i in range(5)]

### Функция zip() ###
# Позволяет объединить два списка в новый список кортежей, каждый из которых будет содержать по одному
# элементу из каждого списка.
L = [i for i in range(10)]
# 0 1 2 3 4 5 6 7 8 9
M = [i for i in range(10,0,-1)]
# 10 9 8 7 6 5 4 3 2 1
for a in zip(L,M):
    print(a)
#(0, 10)
#(1, 9)
#(2, 8)
#(3, 7)
#(4, 6)
#(5, 5)
#(6, 4)
#(7, 3)
#(8, 2)
#(9, 1)

# Код можно сделать еще более приятным:
for a, b in zip(L,M):
    print('a =', a, 'b =', b)
#a = 0 b = 10
#a = 1 b = 9
#a = 2 b = 8
#a = 3 b = 7
#a = 4 b = 6
#a = 5 b = 5
#a = 6 b = 4
#a = 7 b = 3
#a = 8 b = 2
#a = 9 b = 1

# Используя функцию zip() внутри генераторов списков, вычислите поэлементные произведения списков L и M.
N = [a*b for a,b in zip(L,M)]

# Программа, которая сжимает последовательность символов
text = input()  # получаем строку

first = text[0]  # сохраняем первый символ
count = 0  # заводим счетчик
result = ''  # и результирующую строку

for c in text:
    if c == first:  # если символ совпадает с сохраненным,
        count += 1  # то увеличиваем счетчик
    else:
        result += first + str(count)  # иначе - записываем в результат
        first = c  # и обновляем сохраненный символ с его счетчиком
        count = 1

result += first + str(count)  # и добавляем в результат последний символ
print(result)