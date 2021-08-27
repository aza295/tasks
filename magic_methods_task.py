
# 1. Создайте класс Account и переопределите в нем методы init, repr, str и del.
# Объекты класса должны содержать атрибуты имени, баланса и города, где открыт счет.
# Метод init должен возвращать сообщение о создании счета, repr только имя держателя счета
# и баланс, а str сообщение с приветствием и также информацией о держателе счета, 
# балансе и филиале банка в котором зарегистрирован клиент, del в свою очередь сообщение об удаление 
# и слово "Пока!"
# class Account:
#       def __init__(self,name,balance,city,department):
#             self.name = name 
#             self.balance = balance 
#             self.city = city
#             self.department = department
#             print ('счет открыт ')
      
#       def __repr__(self):
#             return f'имя держателя счета {self.name}, баланс = {self.balance}'
#       def __str__(self):
#             return f'привет {self.name}, город {self.city},  банк: {self.department}, ваш баланс = {self.balance}'

#       def __del__(self):
#             print('Аккаунт удален')
#             return 'Пока'

# a = Account('Шер',10800,'Шанхай','ICBC')
# print(a)
# del a
 




# '''
# 2. Определите класс MyNumber который наследуется от класса int. 
# У экземпляра класса должен быть обязательный атрибут value. 
# Переопределите методы сложения, вычитания, умножения и деления для класса таким  образом чтобы при при использовании операторов + - * / - результат возвращался с сообщением об использованном методе, 
# например:print(num + 5)  -------> "Это сложение и Ваш результат равен 10"
# '''

# class MyNumber(int):

#   def init(self, value):
#     self.value = value
  
#   def add(self, x):
#     return f'Это сложение и ваш результат равен {self.value + x}'
  
#   def sub(self, x):
#     return f'Это вычитания и ваш результат равен {self.value - x}'

#   def mul(self, x):
#     return f'Это умножения и ваш результат равен {self.value * x}'

#   def truediv(self, x):
#     return f'Это деление и ваш результат равен {self.value / x}'

# num = MyNumber(16)
# print(num + 7)
# print(num - 12)
# print(num * 0)
# print(num / 4)

# '''
# 3. Напишите класс MyList, который наследуется от list. Сделайте так, чтобы индексация
# элементов начиналась с 1. Например:
# x = MyList([1,2,3,4,5])
# x[1] → 1
# '''

# class MyList(list):
#   def getitem(self, index):
#     if index < 0:
#       return super().getitem(index)
#     elif index == 0 or index > len(self):
#       raise IndexError
#     return super().getitem(index - 1)

# x = MyList([1,2,3,4,5])
# print(x[1])

# '''
# # 4. Напишите класс Student, который описывает студента. У студента есть следующие атрибуты: имя, фамилия, класс, и оценки по предметам в следующем виде: {math’: 100, ‘history’: 89, literature’: 88}. 
# # Сделайте так, чтобы сравнение студентов между собой производилось по средней оценке студента по предметам.
# # '''

# class Student:

#   def init(self, name, surname, year, grade):
#     self.name = name
#     self.surname = surname
#     self.year = year 
#     self.grade = grade

#   def average(self):
#     average = 0
#     average = sum(self.grade.values())
#     return average / len(self.grade)

#   def eq(self, other):
#     return self.average() == other.average()

#   def ne(self, other):
#     return self.average() != other.average()

#   def lt(self, other):
#     return self.average() < other.average()

#   def gt(self, other):
#     return self.average() > other.average()

#   def le(self, other):
#     return self.average() <= other.average()

#   def ge(self, other):
#     return self.average() >= other.average()

# student1 = Student(name='Ermek', surname='Tynychbekov', year=4, grade={'math': 100, 'history': 89, 'literature': 88})
# student2 = Student(name='Erlan', surname='Zhumabekov', year=4, grade={'math': 90, 'history': 90, 'literature': 100})

# print(student1 == student2)
# print(student1 != student2)
# print(student1 < student2)
# print(student1 > student2)
# print(student1 <= student2)
# print(student1 >= student2)


# 5. Напишите класс Word и переопределите методы 'больше чем', 'меньше чем', 'больше или равно', 'меньше или равно' для сравнения объектов класса - строк по длине(len). 
# Также в методе new напишите условие для удаления
# пробелов и пустых строк в созданных словах.
# '''

# 1. Создайте класс Account и переопределите в нем методы init, repr, str и del.
# Объекты класса должны содержать атрибуты имени, баланса и города, где открыт счет.
# Метод init должен возвращать сообщение о создании счета, repr только имя держателя счета
# и баланс, а str сообщение с приветствием и также информацией о держателе счета, 
# балансе и филиале банка в котором зарегистрирован клиент, del в свою очередь сообщение об удаление 
# и слово "Пока!"
# class Account:
#       def __init__(self,name,balance,city,department):
#             self.name = name 
#             self.balance = balance 
#             self.city = city
#             self.department = department
#             print ('счет открыт ')
      
#       def __repr__(self):
#             return f'имя держателя счета {self.name}, баланс = {self.balance}'
#       def __str__(self):
#             return f'привет {self.name}, город {self.city},  банк: {self.department}, ваш баланс = {self.balance}'

#       def __del__(self):
#             print('Аккаунт удален')
#             return 'Пока'

# a = Account('Шер',10800,'Шанхай','ICBC')
# print(a)
# del a
 




# '''
# 2. Определите класс MyNumber который наследуется от класса int. 
# У экземпляра класса должен быть обязательный атрибут value. 
# Переопределите методы сложения, вычитания, умножения и деления 
# для класса таким  образом чтобы при при использовании операторов + - * / - 
# результат возвращался с сообщением об использованном методе, 
# например:print(num + 5)  -------> "Это сложение и Ваш результат равен 10"
# '''

# class MyNumber(int):

#   def __init__(self, value):
#     self.value = value
  
#   def __add__(self, x):
#     return f'Это сложение и ваш результат равен {self.value + x}'
  
#   def __sub__(self, x):
#     return f'Это вычитания и ваш результат равен {self.value - x}'

#   def __mul__(self, x):
#     return f'Это умножения и ваш результат равен {self.value * x}'

#   def __truediv__(self, x):
#     return f'Это деление и ваш результат равен {self.value / x}'

# num = MyNumber(27)
# print(num + 19)
# print(num - 17)
# print(num * 666)
# print(num / 3)
# '''
# 3. Напишите класс MyList, который наследуется от list. Сделайте так, чтобы индексация
# элементов начиналась с 1. Например:
# x = MyList([1,2,3,4,5])
# x[1] → 1
# '''

class MyList(list):
  def getitem(self, index):
    if index < 0:
      return super().getitem(index)
    elif index == 0 or index > len(self):
      raise IndexError
    return super().getitem(index - 1)

x = MyList([1,2,3,4,5])
print(x[1])

# '''
# # 4. Напишите класс Student, который описывает студента. 
# У студента есть следующие атрибуты: 
# имя, фамилия, класс, 
# и оценки по предметам в следующем виде: 
# {math’: 100, ‘history’: 89, literature’: 88}. 
# # Сделайте так, чтобы сравнение студентов между 
# собой производилось по средней оценке студента по предметам.
# # '''

# class Student:

#   def init(self, name, surname, year, grade):
#     self.name = name
#     self.surname = surname
#     self.year = year 
#     self.grade = grade

#   def average(self):
#     average = 0
#     average = sum(self.grade.values())
#     return average / len(self.grade)

#   def eq(self, other):
#     return self.average() == other.average()

#   def ne(self, other):
#     return self.average() != other.average()

#   def lt(self, other):
#     return self.average() < other.average()

#   def gt(self, other):
#     return self.average() > other.average()

#   def le(self, other):
#     return self.average() <= other.average()

#   def ge(self, other):
#     return self.average() >= other.average()

# student1 = Student(name='Ermek', surname='Tynychbekov', year=4, grade={'math': 100, 'history': 89, 'literature': 88})
# student2 = Student(name='Erlan', surname='Zhumabekov', year=4, grade={'math': 90, 'history': 90, 'literature': 100})

# print(student1 == student2)
# print(student1 != student2)
# print(student1 < student2)
# print(student1 > student2)
# print(student1 <= student2)
# print(student1 >= student2)


# 5. Напишите класс Word и переопределите методы 'больше чем', 'меньше чем', 'больше или равно', 'меньше или равно' для сравнения объектов класса - строк по длине(len). 
# Также в методе new напишите условие для удаления
# пробелов и пустых строк в созданных словах.
# '''

# class Word:

#   def __new__(cls, word):
#     word = word.replace(' ', '')
#     if word == '':
#       raise Exception('Слово не может быть пустым')
#     return object.__new__(cls)

#   def __init__(self, word):
#     self.word = word.replace(' ', '')

#   def __gt__(self, other):
#     return len(self.word) > len(other.word)

#   def __lt__(self, other):
#     return len(self.word) < len(other.word)

#   def __ge__(self, other):
#     return len(self.word) >= len(other.word)

#   def __le__(self, other):
#     return len(self.word) <= len(other.word)

# word1 = Word('Hello world')
# word2 = Word('HD    HDH     HD DH   JF' )
# word3 = Word('          HTE      ')

# print(word1 > word2)
# print(word2 > word1)
# print(word1 == word2)
# print(word3 > word2)
# print(word1 > word3)
