### Стек (stack) ###

# Функция par_checker(string), которая проверяет строку string на корректность расстановки скобок
def par_checker(string):
    stack = []  # инициализируем стек

    for s in string:  # читаем строку посимвольно
        if s == "(":  # если открывающая скобка,
            stack.append(s)  # добавляем её в стек
        elif s == ")":
            # если встретилась закрывающая скобка, то проверяем
            # пуст ли стек и является ли верхний элемент — открывающей скобкой
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()  # удаляем из стека
            else:  # иначе завершаем функцию с False
                return False
    # если стек пустой, то незакрытых скобок не осталось
    # значит, возвращаем True, иначе — False
    return len(stack) == 0

# Функция par_checker(string), которая проверяет строку string на корректность расстановки круглых и квадратных скобок
pars = {")": "(", "]": "["}


def par_checker_mod(string):
    stack = []

    for s in string:
        if s in "([":
            stack.append(s)
        elif s in ")]":
            if len(stack) > 0 and stack[-1] == pars[s]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


### Очередь ###

# Попробуем создать обработчик задач на бесконечном цикле с использованием очереди:
N_max = int(input("Определите размер очереди:"))

queue = [0 for _ in range(N_max)]  # инициализируем список с нулевыми элементами
order = 0  # будем хранить сквозной номер задачи
head = 0  # указатель на начало очереди
tail = 0  # указатель на элемент следующий за концом очереди

while True:
    cmd = input("Введите команду:")
    if cmd == "empty":
        if is_empty():
            print("Очередь пустая")
        else:
            print("В очереди есть задачи")
    elif cmd == "size":
        print("Количество задач в очереди:", size())
    elif cmd == "add":
        if size() != N_max:
            add()
        else:
            print("Очередь переполнена")
    elif cmd == "show":
        if is_empty():
            print("Очередь пустая")
        else:
            show()
    elif cmd == "do":
        if is_empty():
            print("Очередь пустая")
        else:
            do()
    elif cmd == "exit":
        for _ in range(size()):
            do()
        print("Очередь пустая. Завершение работы")
        break
    else:
        print("Введена неверная команда")

# Функция is_empty, которая проверяет наличие элементов в очереди, используя указатели head и tail
def is_empty(): # очередь пуста?
    # да, если указатели совпадают и в них содержится ноль
    return head == tail and queue[head] == 0

# Функция size, которая возвращает текущий размер очереди
def size(): # получаем размер очереди
    if is_empty(): # если она пуста
        return 0 # возвращаем ноль
    elif head == tail: # иначе, если очередь не пуста, но указатели совпадают
        return N_max # значит очередь заполнена
    elif head > tail: # если хвост очереди сместился в начало списка
        return N_max - head + tail
    else: # или если хвост стоит правее начала
        return tail - head

# Функция add, которая добавляет задачу в конец очереди
def add():  # добавляем задачу в очередь
    global tail, order
    order += 1  # увеличиваем порядковый номер задачи
    queue[tail] = order  # добавляем его в очередь
    print("Задача №%d добавлена" % (queue[tail]))

    # увеличиваем указатель на 1 по модулю максимального числа элементов
    # для зацикливания очереди в списке
    tail = (tail + 1) % N_max

# Функция печатающая информацию о приоритетной задаче в формате:
def show(): # выводим приоритетную задачу
    print("Задача №%d в приоритете" % (queue[head]))

# Функция  которая печатает в консоль задачу (=выполняет её) и, соответственно, удаляет её из очереди, присваивая ей
# значение 0
def do(): # выполняем приоритетную задачу
    global head
    print("Задача №%d выполнена" % (queue[head]))
    queue[head] = 0 # после выполнения зануляем элемент по указателю
    head = (head + 1) % N_max # и циклично перемещаем указатель

# Весь код по очереди:

class Queue:
    # Конструктор нашего класса, в нём происходит нужная инициализация объекта
    def __init__(self, max_size):
        self.max_size = max_size  # размер очереди
        self.task_num = 0  # будем хранить сквозной номер задачи

        self.tasks = [0 for _ in range(self.max_size)]  # инициализируем список с нулевыми элементами
        self.head = 0  # указатель на начало очереди
        self.tail = 0  # указатель на элемент следующий за концом очереди

    def is_empty(self):  # очередь пуста?
        # да, если указатели совпадают и в них содержится ноль
        return self.head == self.tail and self.tasks[self.head] == 0

    def size(self):  # получаем размер очереди
        if self.is_empty():  # если она пуста
            return 0  # возвращаем ноль
        elif self.head == self.tail:  # иначе, если очередь не пуста, но указатели совпадают
            return self.max_size  # значит, очередь заполнена
        elif self.head > self.tail:  # если хвост очереди сместился в начало списка
            return self.max_size - self.head + self.tail
        else:  # или если хвост стоит правее начала
            return self.tail - self.head

    def add(self):
        self.task_num += 1  # увеличиваем порядковый номер задачи
        self.tasks[self.tail] = self.task_num  # добавляем его в очередь
        print(f"Задача №{self.tasks[self.tail]} добавлена")

        # увеличиваем указатель на 1 по модулю максимального числа элементов
        # для зацикливания очереди в списке
        self.tail = (self.tail + 1) % self.max_size

    def show(self):  # выводим приоритетную задачу
        print(f"Задача №{self.tasks[self.head]} в приоритете")

    def do(self):  # выполняем приоритетную задачу
        print(f"Задача №{self.tasks[self.head]} выполнена")
        # после выполнения зануляем элемент по указателю
        self.tasks[self.head] = 0
        # и циклично перемещаем указатель
        self.head = (self.head + 1) % self.max_size


# Используем класс
size = int(input("Определите размер очереди: "))
q = Queue(size)

while True:
    cmd = input("Введите команду:")
    if cmd == "empty":
        if q.is_empty():
            print("Очередь пустая")
        else:
            print("В очереди есть задачи")
    elif cmd == "size":
        print("Количество задач в очереди:", q.size())
    elif cmd == "add":
        if q.size() != q.max_size:
            q.add()
        else:
            print("Очередь переполнена")
    elif cmd == "show":
        if q.is_empty():
            print("Очередь пустая")
        else:
            q.show()
    elif cmd == "do":
        if q.is_empty():
            print("Очередь пустая")
        else:
            q.do()
    elif cmd == "exit":
        for _ in range(q.size()):
            q.do()
        print("Очередь пустая. Завершение работы")
        break
    else:
        print("Введена неверная команда")

### Графы ###

# Граф — это структура, имеющая узлы (вершины графа) и связи между ними (ребра).

G = {"Адмиралтейская" :
         ["Садовая"],
     "Садовая" :
         ["Сенная площадь",
          "Спасская",
          "Адмиралтейская",
          "Звенигородская"],
     "Сенная площадь" :
         ["Садовая",
          "Спасская"],
     "Спасская" :
         ["Садовая",
          "Сенная площадь",
          "Достоевская"],
     "Звенигородская" :
         ["Пушкинская",
          "Садовая"],
     "Пушкинская" :
         ["Звенигородская",
          "Владимирская"],
     "Владимирская" :
         ["Достоевская",
          "Пушкинская"],
     "Достоевская" :
         ["Владимирская",
          "Спасская"]}

# Возьмите граф из предыдущего задания (с картой метро) и постройте из него взвешенный граф. В качестве весов
# используйте время, необходимое для того, чтобы доехать (или перейти) с одной станции на другую.
G = {"Адмиралтейская" :
         {"Садовая" : 4},
     "Садовая" :
         {"Сенная площадь" : 3,
          "Спасская" : 3,
          "Адмиралтейская" : 4,
          "Звенигородская" : 5},
     "Сенная площадь" :
         {"Садовая" : 3,
          "Спасская" : 3},
     "Спасская" :
         {"Садовая" : 3,
          "Сенная площадь" : 3,
          "Достоевская" : 4},
     "Звенигородская" :
         {"Пушкинская" : 3,
          "Садовая" : 5},
     "Пушкинская" :
         {"Звенигородская" : 3,
          "Владимирская" : 4},
     "Владимирская" :
         {"Достоевская" : 3,
          "Пушкинская" : 4},
     "Достоевская" :
         {"Владимирская" : 3,
          "Спасская" : 4}}

# «алгоритм Дейкстры».
# Его суть заключается в том, чтобы последовательно перебирать вершины одну за другой в поисках кратчайшего пути
# до этой вершины. Вершину будем называть предком для другой, если она идет раньше по пути перемещения по ребрам
# в графе.
D = {k : 100 for k in G.keys()} # расстояния
start_k = 'Адмиралтейская' # стартовая вершина
D[start_k] = 0 # расстояние от неё до самой себя равно нулю
U = {k : False for k in G.keys()} # флаги просмотра вершин

for _ in range(len(D)):
    # выбираем среди непросмотренных наименьшее по расстоянию
    min_k = min([k for k in U.keys() if not U[k]], key = lambda x: D[x])

    for v in G[min_k].keys(): # проходимся по всем смежным вершинам
        D[v] = min(D[v], D[min_k] + G[min_k][v]) # минимум
    U[min_k] = True # просмотренную вершину помечаем


# Модифицируйте алгоритм Дейкстры таким образом, что в массив P по соответствующему ключу будет записываться
# предок с минимальным расстоянием, если это необходимо.
D = {k : 100 for k in G.keys()} # расстояния
start_k = 'Адмиралтейская' # стартовая вершина
D[start_k] = 0 # расстояние от нее до самой себя равно нулю
U = {k : False for k in G.keys()} # флаги просмотра вершин
P = {k : None for k in G.keys()} # предки

for _ in range(len(D)):
    # выбираем среди непросмотренных наименьшее по расстоянию
    min_k = min([k for k in U.keys() if not U[k]], key = lambda x: D[x])

    for v in G[min_k].keys(): # проходимся по всем смежным вершинам
         if D[v] > D[min_k] + G[min_k][v]: # если расстояние от текущей вершины меньше
            D[v] = D[min_k] + G[min_k][v] # то фиксируем его
            P[v] = min_k # и записываем как предок
    U[min_k] = True # просмотренную вершину помечаем

pointer = some_station # куда должны прийти
while pointer is not None: # перемещаемся, пока не придём в стартовую точку
    print(pointer)
    pointer = P[pointer]


### Деревья ###
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

def insert_left(self, next_value):
    if self.left_child is None:
        self.left_child = BinaryTree(next_value)
    else:
        new_child = BinaryTree(next_value)
        new_child.left_child = self.left_child
        self.left_child = new_child
    return self

def insert_right(self, next_value):
    if self.right_child is None:
        self.right_child = BinaryTree(next_value)
    else:
        new_child = BinaryTree(next_value)
        new_child.right_child = self.right_child
        self.right_child = new_child
    return self

# создаём корень и его потомков /7|2|5\
node_root = BinaryTree(2).insert_left(7).insert_right(5)
# левое поддерево корня /2|7|6\
node_7 = node_root.left_child.insert_left(2).insert_right(6)
# правое поддерево предыдущего узла /5|6|11\
node_6 = node_7.right_child.insert_left(5).insert_right(11)
# правое поддерево корня /|5|9\
node_5 = node_root.right_child.insert_right(9)
# левое поддерево предыдущего узла корня /4|9|\
node_9 = node_5.right_child.insert_left(4)

# Обход дерева
# Поиск в глубину (depth-first search, DFS). Его основная суть заключается в том, что, проходя по каждому узлу,
# мы сначала идём в его потомка, а потом возвращаемся обратно — это обход с возвратом. Такой поиск бывает трёх видов:
# - префиксный (pre-order);
# - постфиксный (post-order);
# - инфиксный (in-order).
# Поиск в ширину (breadth-first search, BFS). Такой обход осуществляется в обходе уровня за уровнем.

# Рассмотрим префиксный подход. Сначала мы должны обработать значение самого узла (поэтому он и префиксный),
# а затем рекурсивно проделать то же самое с левым потомком, и затем — с правым. В качестве процедуры обработки
# узла возьмём самое простое — печать его значения.
def pre_order(self):
    print(self.value) # процедура обработки

    if self.left_child is not None: # если левый потомок существует
        self.left_child.pre_order() # рекурсивно вызываем функцию

    if self.right_child is not None: # если правый потомок существует
        self.right_child.pre_order() # рекурсивно вызываем функцию

node_root.pre_order()
# 2
# 7
# 2
# 6
# 5
# 11
# 5
# 9
# 4

# Метод постфиксного обхода в глубину.
def post_order(self):
    if self.left_child is not None: # если левый потомок существует
        self.left_child.post_order() # рекурсивно вызываем функцию

    if self.right_child is not None: # если правый потомок существует
        self.right_child.post_order() # рекурсивно вызываем функцию

    print(self.value) # процедура обработки

node_root.post_order()
# 2
# 5
# 11
# 6
# 7
# 4
# 9
# 5
# 2

# Инфиксный подход заключается в том, что порядок обработки узла и его потомков смешивается: сначала шагаем в левое
# поддерево, потом обрабатываем сам узел, затем — правое поддерево.
def in_order(self):
    if self.left_child is not None: # если левый потомок существует
        self.left_child.in_order() # рекурсивно вызываем функцию

    print(self.value) # процедура обработки

    if self.right_child is not None: # если правый потомок существует
        self.right_child.in_order() # рекурсивно вызываем функцию

node_root.in_order()
# 2
# 7
# 5
# 6
# 11
# 2
# 5
# 4
# 9


### Связанный список ###

# Сейчас мы попробуем создать класс LinkedList, реализующий список. Элементы списка будут представлять собой
# экземпляры класса Node.
class Node:  # класс элемента
    def __init__(self, value=None, next_=None):  # инициализируем
        self.value = value  # значением
        self.next = next_  # и ссылкой на следующий элемент

    def __str__(self):
        return "Node value = " + str(self.value)


class LinkedList:  # класс списка
    def __init__(self):  # инициализируем пустым
        self.first = None
        self.last = None

    def clear(self):  # очищаем список
        self.__init__()

    def __str__(self):  # функция печати
        R = ''

        pointer = self.first  # берем первый указатель
        while pointer is not None:  # пока указатель не станет None
            R += str(pointer.value)  # добавляем значение в строку
            pointer = pointer.next  # идем дальше по указателю
            if pointer is not None:  # если он существует добавляем пробел
                R += ' '
        return R

    def pushleft(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value, self.first)
            self.first = new_node

    def pushright(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value)
            self.last.next = new_node
            self.last = new_node

    def popleft(self):
        if self.first is None:  # если список пустой, возвращаем None
            return None
        elif self.first == self.last:  # если список содержит только один элемент
            node = self.first  # сохраняем его
            self.__init__()  # очищаем
            return node  # и возвращаем сохраненный элемент
        else:
            node = self.first  # сохраняем первый элемент
            self.first = self.first.next  # меняем указатель на первый элемент
            return node  # возвращаем сохраненный

    def popright(self):
        if self.first is None:  # если список пустой, возвращаем None
            return None
        elif self.first == self.last:  # если список содержит только один элемент
            node = self.first  # сохраняем его
            self.__init__()  # очищаем
            return node  # и возвращаем сохраненный элемент
        else:
            node = self.last  # сохраняем последний
            pointer = self.first  # создаем указатель
            while pointer.next is not node:  # пока не найдем предпоследний
                pointer = pointer.next
            pointer.next = None  # обнуляем указатели, чтобы
            self.last = pointer  # предпоследний стал последним
            return node  # возвращаем сохраненный


# Теперь напишем функционал этого класса, чтобы он стал полноценным итератором.
def __iter__(self): # объявляем класс как итератор
    self.current = self.first # в текущий элемент помещаем первый
    return self # возвращаем итератор

def __next__(self): # метод перехода
    if self.current is None: # если текущий стал последним
        raise StopIteration # вызываем исключение
    else:
        node = self.current # сохраняем текущий элемент
        self.current = self.current.next # совершаем переход
        return node # и возвращаем сохраненный

# И в заключение напишем «магический» метод, возвращающий размер структуры данных.

def __len__(self):
    count = 0
    pointer = self.first
    while pointer is not None:
        count += 1
        pointer = pointer.next
    return count


### Алгоритмы поиска ###

# Линейный поиск
def find(array, element):
    for i, a in enumerate(array):
        if a == element:
            return i
    return False

array = list(map(int, input().split()))
element = int(input())

print(find(array, element))

# Функция count, которая возвращает количество вхождений элемента в массив
def count(array, element):
    count = 0
    for i, a in enumerate(array):
        if a == element:
            count += 1
    return count

# Двоичный поиск
def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


element = int(input())
array = [i for i in range(1, 100)]  # 1,2,3,4,...

# запускаем алгоритм на левой и правой границе
print(binary_search(array, element, 0, 99))

### Алгоритмы сортировки ###

# Наивная сортировка
import random  # модуль, с помощью которого перемешиваем массив

# пусть имеем массив всего лишь из 9 элементов
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

is_sort = False  # станет True, если отсортирован
count = 0  # счетчик количества перестановок

while not is_sort:  # пока не отсортирован
    count += 1  # прибавляем 1 к счётчику

    random.shuffle(array)  # перемешиваем массив

    # проверяем, отсортирован ли
    is_sort = True
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            is_sort = False
            break

print(array)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(count)
# 290698

# Сортировка выбором
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

for i in range(len(array)):  # проходим по всему массиву
    idx_min = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i, len(array)):
        if array[j] < array[idx_min]:
            idx_min = j
    if i != idx_min:  # если индекс не совпадает с минимальным, меняем
        array[i], array[idx_min] = array[idx_min], array[i]

print(array)

# Сортировка пузырьком
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

for i in range(len(array)):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print(array)

# Сортировка вставками
for i in range(1, len(array)):
    x = array[i]
    idx = i
    while idx > 0 and array[idx-1] > x:
        array[idx] = array[idx-1]
        idx -= 1
    array[idx] = x

# Сортировка слиянием
def merge_sort(L):  # "разделяй"
    if len(L) < 2:  # если кусок массива равен 2,
        return L[:]  # выходим из рекурсии
    else:
        middle = len(L) // 2  # ищем середину
        left = merge_sort(L[:middle])  # рекурсивно делим левую часть
        right = merge_sort(L[middle:])  # и правую
        return merge(left, right)  # выполняем слияние


def merge(left, right):  # "властвуй"
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы

    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

# Быстрая сортировка
def qsort(array, left, right):
    middle = (left + right) // 2

    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)

# Модифицируйте алгоритм быстрой сортировки таким образом, чтобы ведущий элемент выбирался как случайный среди
# подмассива, который сортируется на данном этапе.
def qsort_random(array, left, right):
    p = random.choice(array[left:right + 1])
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            count += 1
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort_random(array, left, j)
    if right > i:
        qsort_random(array, i, right)