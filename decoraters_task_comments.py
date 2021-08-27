# """
# Таски по декораторам
# """
# """
# 1) Напишите декоратор, который печатает перед вызовом полученной функции строку: 
# "Вызываю функцию <имя_функции>". Затем следует вызов функции.
#  После вызова функции должна печататься строка:
#  "Вызов функции <имя_функции> прошёл успешно"
# """

# def lxgivil(func): Создаем  функцию 
#   def wrapper(*args,**kwargs): Создаем вложенность wrapper
#     print(f'calling func {func.__name__}') вызываем f функцию 
#     func(*args,**kwargs)
#     print(f'func calling {func.__name__} succesed')
#   return wrapper


# @lxgivil
# def main():
#   print(f'Функция main')

# main()
# #писать код здесь
# """
# 2) Создайте декоратор, который будет распечатывать дату и время вызова принимаемой функции, а затем вызывает саму функцию, например:
# # @decorator
# # def func():
# #     print('Hello world')

# # func() -> 
# # Функция запущена 26.02.2021 21:51
# # Hello World
# Для этого воспользуйтесь модулем datetime.
# """
# def decorator(func):
#       import datetime
#       def wrapper(*args,**kwargs):
#             current_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
#             func(*args,**kwargs)
#             with open('log.txt', 'a') as file:
#                   file.write(f'{func.__name__}\n')
#                   file.write(f'Функция запущена {current_time}\n')

#                   # моежете раскоментировать в случае чего
#                   # file.write(f'Args:{args}\n')
#                   # file.write(f'Kwargs:{kwargs}')
#                   # file.write('-----------------------\n')


#       return wrapper

# @decorator              
# def func1():
#       print('hello world')


# func1()

# """
# 3) Создайте 3 декоратора, каждый из которых применяет к тексту определённый стиль:
# выделение жирным <b>...</b>\
# курсив <i>...</i>
# подчеркивание <u>...</u>.
# Далее создайте функцию которая будет возвращать текст “Hello world”, примените к этой функции цепочку декораторов
# """
# def wwe(func):
#     def wrapper(*args,**kwargs):
#         text = func(*args,**kwargs)
#         return (f'<b>{text}</b>')
#     return wrapper

# def strv(func):
#     def wrapper(*args,**kwargs):
#         text = func(*args,**kwargs)
#         return (f'<i>{text}</i>')
#     return wrapper

# def vr(func):
#     def wrapper(*args,**kwargs):
#         text = func(*args,**kwargs)
#         return (f'<u>{text}</u>')
#     return wrapper

# @vr
# @strv
# @wwe
# def func():
#     return 'Hello World'

# print (func())

# """
# 4) Создайте декоратор, замеряющий время выполнения функции в секундах. Затем объявите функцию, которая выполняет GET-запрос на главную страницу Google, оберните в декоратор и вызовите её
# """
# from tqdm import tqdm

# def timer(func):
#       import time
#       def wrapper(*args,**kwargs):
#             start = time.time()
#             func(*args,**kwargs)
#             end = time.time()
#             working_time = end - start
#             print(f'время выполнения функции{func.__name__}:{working_time} секунд')
#       return wrapper

# def timer(count=1):
#       import time
#       def decorater(func):
#             def wrapper(*args,**kwargs):
#                   total_time = 0
#                   for i in tqdm (range(count)):
#                         start = time.time()
#                         func(*args,**kwargs)
#                         end = time.time()
#                         working_time = end - start 
#                         total_time += working_time
#                   avg_time = total_time/count 
#                   print(f'время выполнения функции{func.__name__}:{avg_time} секунд')

#             return wrapper
#       return decorater

# @timer(count=20)       
# def func1():
#       print('hello')

# @timer
# def func2(x,y):
#       return x+y

# @timer(count=20) 
# def func3(url):
#       import urllib.request
#       urllib.request.urlopen(url)

# func3('https://google.com/')


# func1()
# func2(20,19)
# func3()

# """
# 5) Создайте словарь users и сохраните в нем несколько пользователей (ключом будет имя пользователя, а значением пароль пользователя).
# Напишите следующую функцию:
# # def login(username, password):
# #     print(f'Welcome, {username}')
# Допишите к этой функции декоратор, который будет проверять есть ли в словаре пользователь с таким username и совпадает ли пароль.
# Если нет, то функция вызывает определенный тип исключения:
# """
# users = {'eric': 123456, 'kyle': "qwerty", 'stan': "qwerty123"}


# def check(func):
#     def wrapper(username, password):
#             if not username in users.keys() and password in users.values():
#                 raise Exception ('Вы ввели неверный логин или пароль')
#             else:              
#                 func(username, password)
#     return wrapper

# @check
# def login(username, password):
#     print(f'Welcome, {username}!')

# login('eric', "123456")






class Car:
      
      def __init__(self):
            self.__speed = 24

      def set_speed(self,new_speed):
            self.__speed = new_speed
      
      def show_speed (self):
            print(self.__speed)
a = Car()
a.set_speed(20)
a.show_speed()