# 1) Объявите 3 переменных, запишите в них строку, список и словарь. Затем запишите их в список, пройдитесь по нему циклом и распечатайте длину каждого из объектов.
# """
# a = ('1,2,3,4,5,6,7,8')
# b = [19,27,30,17]
# c = {'hour':60,'minutes':60,'day':24}

# list_=[a,b,c]

# for i in list_:
#       print(len(i))
# """
# 2) Создайте классы Dog и Cat с одинаковым методом voice. Для собак он должен печатать "Гав", для кошек "Мяу".
# Объявите для каждого из классов по экземпляру. Затем объявить функцию to_pet(), которая будет принимать животное и вызывать у него метод voice()
# """
# class Dog:
#       def __init__(self,name):
#             self.name = name 
#       def voice(self):
#             print('Гав')

# class Cat:
#       def __init__(self,name):
#             self.name = name 
#       def voice(self):
#             print('Мяу')   

# c = Cat('Qwerty')
# c.voice()
# d = Dog('Nurzhan')
# d.voice()

# def to_pet(animal):
#       animal.voice()

# for animal in (c,d):
#       to_pet(animal)
# """
# 3) Создайте 3 класса: Person, Employee и Student, при этом Employee и Student должны наследоваться от Person. Определите во всех трёх классах метод get_info():
# -для класса Person он должен возвращать следующее: “Привет, меня зовут Иван Петров”.
# -для класса Employee он должен возвращать: “Привет, меня зовут Иван Петров, я работаю в компании “Рога и копыта” на должности “директор”.
# -для класса Student должно возвращаться: “Привет, меня зовут Иван Петров, я учусь в КГТУ на 3 курсе”.
# Определите функцию get_human_info(), которая будет принимать объект одного из трёх классов, вызывать метод get_info и печатать результат.
# """
# ]class Person:
#       def __init__(self,name):
#             self.name = name 
#       def get_info(self):
#             return f'Привет, меня зовут {self.name}.'

# class Employee(Person):
#       def __init__(self,name, company,job):
#             self.name= name 
#             self.company = company 
#             self.job = job
#       def get_info(self):
#             return f'Привет, меня зовут {self.name}, я работаю в компании {self.company},на должности  {self.job}'


# class Student(Employee):
#       def __init__(self,name,edu,level):
#             self.name= name 
#             self.edu = edu 
#             self.level = level
#       def get_info(self):
#             return f'Привет, меня зовут {self.name}, я учусь в  {self.edu}, на  {self.level} курсе'

# p = Person('Иван петров')
# e = Employee('Иван Петров','Рога и копыта','Директор')
# s = Student ('Иван Петров','КГТУ','3')

# def get_human_info(i):
#       print(i.get_info())
# for i in (p,e,s):
#       get_human_info(i)
# """
# 4) Объявите абстрактный класс геометрических фигур Shape и определите в нём абстрактный метод get_area() для расчёта площади фигуры, которые необходимо переопределить в дочерних классах.

# Затем наследуйте от Shape три класса: Triangle, Square и Circle.
# -треугольник создаётся с заданными основанием и высотой
# -квадрат создаётся с заданной длиной стороны
# -круг создаётся с заданным радиусом
# Переопределите в каждом из классов метод get_area() таким образом, чтобы он рассчитывал площадь для конкретной фигуры.

# Затем создайте от каждого из трёх классов по экземпляру, и вызовите у каждого метод get_area()

# Подсказка: для создания абстрактных классов воспользуйтесь модулем abc
# """

# # FIRST METHOD
# from abc import ABC, abstractclassmethod
# from math import pi 

# class Shape(ABC):
#       @abstractclassmethod
#       def get_area(self):
#             pass
# class Triangle:
#       def __init__(self,base,height):
#             self.base = base 
#             self.height = height
#       def get_area(self):
#             return 0,5 * self.base * self.height
      
# class Square:
#       def __init__(self,sides):
#             self.sides = sides
#       def get_area(self):
#             return self.sides **2 
# class Cirlce:
#       def __init__(self,radius):
#             self.radius = radius
#       def get_area(self):
#             return 3.14 * self.radius **2

# t = Triangle(19,27)
# print(t.get_area())
# s = Square(8)
# print(s.get_area())
# c = Cirlce(15)
# print(c.get_area())




# #SECOND METHOD 
# from abc import ABC, abstractclassmethod
# from math import pi 

# class Shape(ABC):
#       @abstractclassmethod
#       def get_area(self):
#             pass
# class Triangle:
#       def __init__(self,base,height):
#             self.base = base 
#             self.height = height
#       def get_area(self):
#             print (0,5 * self.base * self.height)
      
# class Square:
#       def __init__(self,sides):
#             self.sides = sides
#       def get_area(self):
#             print (self.sides **2)
# class Cirlce:
#       def __init__(self,radius):
#             self.radius = radius
#       def get_area(self):
#             print (3.14 * self.radius **2)

# t = Triangle(19,27)
# t.get_area()
# s = Square(8)
# s.get_area()
# c = Cirlce(15)
# c.get_area()




# # THIRD METHOD

# from abc import ABC, abstractclassmethod
# from math import pi 

# class Shape(ABC):
#       @abstractclassmethod
#       def get_area(self):
#             pass
# class Triangle:
#       def __init__(self,base,height):
#             self.base = base 
#             self.height = height
#       def get_area(self):
#             return 0,5 * self.base * self.height
      
# class Square:
#       def __init__(self,sides):
#             self.sides = sides
#       def get_area(self):
#             return self.sides **2
# class Cirlce:
#       def __init__(self,radius):
#             self.radius = radius
#       def get_area(self):
#             return 3.14 * self.radius **2

# t = Triangle(19,27)
# s = Square(8)
# c = Cirlce(15)


# for i in (t,s,c):
#       print(i.get_area())






# from abc import ABC, abstractclassmethod
# from math import pi

# class Shape(ABC):
#       @abstractclassmethod
#       def get_area(self):
#             pass

# class Triangle(Shape):
#       def __init__(self,base,height):
#             self.base = base 
#             self.height = height 
#       def get_area(self):
#             return 0,5 * self.base * self.height 
      
# class Square(Triangle):
#       def __init__(self,sides):
#             self.sides = sides
#       def get_area(self):
#             return self.sides **2

# class Cirlce(Square):
#       def __init__(self,radius):
#             self.radius = radius
#       def get_area(self):
#             return 3.14 * self.radius **2

# a = Triangle(24,19)
# print(a.get_area())
# b = Square (66)
# print(b.get_area())
# c = Cirlce (13)
# print(c.get_area())
      





