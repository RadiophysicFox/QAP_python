### Магический метод __init__ ###

# Конструктор класса — «магический» метод __init__, который заранее определяет атрибуты новых экземпляров.
# Первым аргументом он обязательно принимает на вход self, а дальше — произвольный набор аргументов, как обычная
# функция:
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    peter = User(name="Peter Robertson", email="peterrobertson@mail.com")
    julia = User(name="Julia Donaldson", email="juliadonaldson@mail.com")

    print(peter.name)
    print(julia.email)

    Peter
    Robertson
    juliadonaldson @ mail.com


### Методы и функции ###
# Метод — это всего лишь функция, реализованная внутри класса, и первым аргументом принимающая self.
class Product:
    def __init__(self, name, category, quantity_in_stock):
        self.name = name
        self.category = category
        self.quantity_in_stock = quantity_in_stock

    def is_available(self):
        return True if self.quantity_in_stock > 0 else False

eggs = Product("eggs", "food", 5)
print(eggs.is_available())
# True

# Создадим класс с конструктором:
class Event:
    def __init__(self, timestamp=0, event_type="", session_id=""):
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id

    def init_from_dict(self, event_dict):
        self.timestamp = event_dict.get("timestamp")
        self.type = event_dict.get("type")
        self.session_id = event_dict.get("session_id")

events = [
    {
     "timestamp": 1554583508000,
     "type": "itemViewEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1555296337000,
     "type": "itemViewEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1549461608000,
     "type": "itemBuyEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
]

for event in events:
    event_obj = Event()
    event_obj.init_from_dict(event)
    print(event_obj.timestamp)

### Наследование ###
# Чтобы задать родительский класс, надо указать его в скобках при объявлении класса, как будто это аргумент функции:
import datetime


class Product:
    max_quantity = 100000

    def __init__(self, name, category, quantity_in_stock):
        self.name = name
        self.category = category
        self.quantity_in_stock = quantity_in_stock

    def is_available(self):
        return True if self.quantity_in_stock > 0 else False


class Food(Product):
    is_critical = True
    needs_to_be_refreshed = True
    refresh_frequency = datetime.timedelta(days=1)


eggs = Food(name="eggs", category="food", quantity_in_stock=5)
print(eggs.max_quantity)

