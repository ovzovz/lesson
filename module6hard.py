from math import pi as PI
class Figure():
    sides_count = 0
    __color=[]
    __sides = []
    def __init__(self,__color, *__sides, filled = True):
        self.__color = __color
        self.__sides = [*__sides]
        if len(self.__sides) != self.sides_count:
             self.__sides = [1] * self.sides_count
        self.filled = filled

    def get_color(self):
        return self.__color
    def __is_valid_color (self,*color):
        if len(color) != 3:
            return False
        for col in color:
            if  col not in range(0,256,1):
                return False
        return True

    def set_color (self,*color):
        if self.__is_valid_color (*color):
            self.__color = color

    def __is_valid_sides(self, *sides):
        if len(sides) != self.sides_count:
            return False
        for side in sides:
            if  not (isinstance(side,int) and side > 0):
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__ (self):
        return sum(self.__sides)

    def set_sides(self,*new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1
    __radius = 0

    def get_radius(self):
        self.__radius = int(*super().get_sides())/(2*PI)  #super().get_sides()[0]/(2*PI)
        return self.__radius

    def get_square(self):
        return PI*self.get_radius()**2

class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        p = super().__len__()/2
        square = p
        for side in super().get_sides():
            square = square*(p-side)
        square = square**0.5
        return square

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().set_color(*color)
        super().set_sides(*[*sides] * self.sides_count)
        super().__init__(super().get_color(),*super().get_sides())

    def get_volume(self):
        return super().get_sides()[0]**3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

#ВАЖНО!
c1=Circle((200, 200, 100), 10, 15, 6)
print(c1.get_sides())
t1=Triangle((200, 200, 100), 10, 6)
print(t1.get_sides())
c1=Cube((200, 200, 100), 9)
print(c1.get_sides())
c1=Cube((200, 200, 100), 9, 12)
print(c1.get_sides())


print(circle1.get_radius())
print (t1.get_square())