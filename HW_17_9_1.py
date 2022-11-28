import sys

# Проверка, что вводятся только цифры с помощью конструкции try/except
try:
    sequence = input("Введите последовательность чисел через пробел:")
    # Проверка на отсутствие пробелов:
    if " " not in sequence:
        print("Пробел отсутствует. Перезапустите программу")
        sys.exit()
    # Преобразование введённой последовательности в список:
    list_sequence = list(map(int, sequence.split()))
    number = int(input("Введите число:"))
except ValueError:
    print('Недопустимый ввод. Перезапустите программу и используйте целые числовые значения')
    sys.exit()


# Функция двоичного поиска:
def binary_search(array, element, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        print('Число выходит за диапазон списка, введите меньшее число.')
        sys.exit()


# Функция сортировки пузырьком:
def sort_array(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


# Сортируем и печатаем список:
sorted_list_sequence = sort_array(list_sequence)
print("Отсортированный список:", sorted_list_sequence)

# Ищем индекс элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу:
if not binary_search(sorted_list_sequence, number, 0, len(sorted_list_sequence)):
    index_list = []
    for index, value in enumerate(sorted_list_sequence):
        if value > number:
            if index != 0:
                index_list.append(index)
    for index in index_list:
        if sorted_list_sequence[index-1] < number:
            print("Номер позиции искомого элемента:", index-1)
            sys.exit()
else:
    if sorted_list_sequence.count(number) > 1:
        index_list = []
        for index, value in enumerate(sorted_list_sequence):
            if value == number:
                if index != 0:
                    index_list.append(index)
        for index in index_list:
            if sorted_list_sequence[index-1] < number:
                print("Номер позиции искомого элемента:", index-1)
                sys.exit()
    else:
        index = binary_search(sorted_list_sequence, number, 0, len(sorted_list_sequence))
        if sorted_list_sequence[index-1] < number:
            print("Номер позиции искомого элемента:", index-1)
            sys.exit()

print("В последовательности нет числа, удовлетворяющего всем условиям")



