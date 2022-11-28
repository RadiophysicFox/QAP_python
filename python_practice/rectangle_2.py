from rectangle import Rectangle, Square, Circle

# далее создаём два прямоугольника

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

# вывод площади двух прямоугольников

print(rect_1.get_area())
print(rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_area_square(), square_2.get_area_square())

circle_1 = Circle(2)
circle_2 = Circle(4)

print(circle_1.get_area_circle(), circle_2.get_area_circle())

figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]
for figure in figures:
    if isinstance(figure,Square):
        print(figure.get_area_square())
    elif isinstance(figure, Circle):
        print(figure.get_area_circle())
    else:
        print(figure.get_area())

# В условии есть функция isinstance, поддерживающая наследование. Она проверяет, является ли аргумент объекта
# экземпляром класса или экземпляром класса из кортежа. В случае если является, функция возвращает True, если не
# является — False.