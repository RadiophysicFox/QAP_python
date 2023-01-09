### Простые декораторы ###

def my_decorator(func):
    def wrapper():
        print("Начало выполнения функции.")
        func()
        print("Конец выполнения функции.")

    return wrapper


# Эту функцию мы будем декорировать
@my_decorator
def my_first_decorator():
    print("Это мой первый декоратор!")


my_first_decorator()

# Переиспользование декораторов
from decorators import do_twice

@do_twice
def test_twice():
    print("Это вызов функции test_twice!")


test_twice()


# Декорирование функций с аргументами
@do_twice
def test_twice_without_params():
    print("Этот вызов без параметров")


@do_twice
def test_twice_2_params(str1, str2):
    print("В этой функции 2 параметра - {0} и {1}".format(str1, str2))


@do_twice
def test_twice(str):
    print("Этот вызов возвращает строку {0}".format(str))


test_twice_without_params()
test_twice_2_params("1", "2")
test_twice("single")


# Декорирование функций с аргументами
import functools

def debug(func):
    """Выводит сигнатуру функции и возвращаемое значение"""
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Вызываем {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} вернула значение - {value!r}")
        return value
    return wrapper_debug

# И код, чтобы проверить нашу функцию-дебаггер:

@debug
def age_passed(name, age=None):
    if age is None:
        return "Необходимо передать значение age"
    else:
        return "Аргументы по умолчанию заданы!"


age_passed("Роман")
age_passed("Роман", age=21)


### Понятие фикстуры ###

# Фикстуры — это функции, выполняемые pytest до или после тестовых функций. Код в фикстуре может делать все, что вам
# необходимо: подготавливать данные для теста, настраивать логирование приложения и т.д. Иными словами, фикстуры
# обеспечивают механизм отделения непосредственно кода тестов от «подготовки к» и «очистке после» исполнения тестов.

import pytest
import requests
from datetime import datetime


@pytest.fixture()
def some_data():
    return 42


def test_some_data(some_data):
    assert some_data == 42


# Организация setup и teardown в фикстурах

def get_key():
    # переменные email и password нужно заменить своими учетными данными
    response = requests.post(url='https://petfriends.skillfactory.ru/login',
                             data={"email": email, "pass": password})
    assert response.status_code == 200, 'Запрос выполнен неуспешно'
    assert 'Cookie' in response.request.headers, 'В запросе не передан ключ авторизации'
    return response.request.headers.get('Cookie')


def test_getAllPets(get_key):
    response = requests.get(url='https://petfriends.skillfactory.ru/api/pets',
                            headers={"Cookie": get_key})
    assert response.status_code == 200, 'Запрос выполнен неуспешно'
    assert len(response.json().get('pets')) > 0, 'Количество питомцев не соответствует ожиданиям'

# C setup разобрались. Теперь давайте разберёмся с teardown. Для этого напишем фикстуру, которая будет считать,
# сколько времени длился тест.


@pytest.fixture(autouse=True)
def time_delta():
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    print (f"\nТест шел: {end_time - start_time}")

# Фикстура request
@pytest.fixture()
def request_fixture(request):
    print(request.fixturename)
    print(request.scope)
    print(request.function.__name__)
    print(request.cls)
    print(request.module.__name__)
    print(request.fspath)
    if request.cls:
        return f"\n У теста {request.function.__name__} класс есть\n"
    else:
        return f"\n У теста {request.function.__name__} класса нет\n"


def test_request_1(request_fixture):
    print(request_fixture)


class TestClassRequest:

    def test_request_2(self, request_fixture):
        print(request_fixture)


# Разберём на практике
@pytest.fixture(scope="class")
def get_key(request):
    # переменные email и password нужно заменить своими учетными данными
    response = requests.post(url='https://petfriends.skillfactory.ru/login',
                             data={"email": email, "pass": password})
    assert response.status_code == 200, 'Запрос выполнен неуспешно'
    assert 'Cookie' in response.request.headers, 'В запросе не передан ключ авторизации'
    print("\nreturn auth_key")
    return response.request.headers.get('Cookie')


@pytest.fixture(autouse=True)
def request_fixture(request):
    if 'Pets' in request.function.__name__:
        print(f"\nЗапущен тест из сьюта Дом Питомца: {request.function.__name__}")


class TestClassPets:

    def test_getAllPets2(self, get_key):
        response = requests.get(url='https://petfriends.skillfactory.ru/api/pets',
                                headers={"Cookie": get_key})
        assert response.status_code == 200, 'Запрос выполнен неуспешно'
        assert len(response.json().get('pets')) > 0, 'Количество питомцев не соответствует ожиданиям'

    def test_getMyPets2(self, get_key):
        response = requests.get(url='https://petfriends.skillfactory.ru/my_pets',
                                headers={"Cookie": get_key})
        assert response.status_code == 200, 'Запрос выполнен неуспешно'
        assert response.headers.get('Content-Type') == 'text/html; charset=utf-8'

    def test_anotherTest(self):
        pass

# Встроенные фикстуры pytest
# pytest.mark.skip
@pytest.mark.skip(reason="Баг в продукте - <ссылка>")
def test_one(): … # Это наш тест, который находит тот самый баг

# pytest.mark.skipif
@pytest.mark.skipif(sys.version_info < (3, 6), reason="Тест требует python версии 3.6 или выше")
def test_python36_and_greater():

# pytest.mark.xfail
@pytest.mark.xfail(sys.platform == "win32",
                   reason="Ошибка в системной библиотеке")  # На платформе Windows ожидаем, что тест будет падать
def test_not_for_windows():

# Пользовательские группы
@pytest.mark.api
@pytest.mark.auth
def test_auth_api():
    pass


@pytest.mark.ui
@pytest.mark.auth
def test_auth_ui():
    pass


@pytest.mark.api
@pytest.mark.event
def test_event_api():
    pass


@pytest.mark.ui
@pytest.mark.event
def test_event_ui():
    pass

# Cоздать pytest.ini
[pytest]
markers =
   api: тесты API
   ui: тесты UI
   event: тесты мероприятий
   auth: тесты авторизации


pytest test.py -v -m "api" # test.py замените на имя своего файла в проекте
pytest test.py -v -m "ui and auth"
pytest test.py -v -m "auth or event"