# 1 """Создайте класс Auto в нем реализуйте метод ride который выводит сообщение Riding on a ground, создайте класс Boat реализуйте метод swim, который выводит floating on water.
# Создайте класс Amphibian который наследуется от класса Auto и Boat. Создайте от него объект и вызовите все методы.



# class Auto:
#       def ride(self):
#             print('Riding on a ground')
# class Boat:
#       def swim(self):
#             # super().ride()
#             print('Floating on a water')

# class Amphibian(Auto,Boat):
#       pass
       

# a = Amphibian()
# a.swim()
# a.ride()

#2  #"""Создайте класс RadioMixin в нем реализуйте метод для 
# проигрывания музыки play_music который принимает в себя название песни. 
# Создайте класс Auto, Boat, Amphibian и расширьте функционал этих классов при помощи миксина"""


# class RadioMixin:
#       def play_music(self,song):
#             print(f'Right now is playing {song}')
      

# class Auto(RadioMixin):
#       pass

# class Boat(RadioMixin):
#       pass
 
# class Amphibian(RadioMixin):
#       pass

# a = Auto()
# b = Boat()
# aa = Amphibian()
# a.play_music('creeping death')
# b.play_music('head crusher')
# aa.play_music('unforgiven')       




# # """Будильник
# Создайте класс Clock, у которого будет метод показывающий текущее время и класс Alarm, 
# с методами для включения и выключения будильника.
# Далее создайте класс AlarmClock, который наследуется от двух предыдущих классов. Добавьте к
# нему метод для установки будильника, при вызове которого должен включатся будильник."""


# import datetime

# class Clock:
#       def show_time(self):
#             print(datetime.datetime.now())

# class Alarm: 
#       def turn_on(self):
#             print('turn on')

#       def turn_off(self):
#             print('turn off')

# class AlarmClock(Clock,Alarm):
#       def set_alarm(self):
#             self.turn_on()

# a = AlarmClock()
# a.show_time()
# a.set_alarm()
# a.turn_off()



# from abc import   ABC, abstractclassmethod 

# class Coder(ABC):
#       experience = 0
#       count_code_time = 0

#       @abstractclassmethod
#       def get_info(self):
#             pass 

#       @abstractclassmethod
#       def coding(self):
#             pass


# Создайте классы Backend и Frontend, которые наследуют все атрибуты и методы 
# от класса Coder.
# class Backend(Coder):
#       pass


# class Frontend(Coder):

#  Класс Backend должен принимать дополнительно 
# параметр languages_backend, а Frontend — languages_frontend соответственно.
# Переопределите в обоих классах методы get_info и coding 
# (так, чтобы он принимал количество часов кодинга и при каждом 
# вызове этого метода добавлял это значение к count_code_time). 
# Так же бывают FullStack разработчики и
# поэтому создайте данный класс и чтобы у него были 
# атрибуты и методы предыдущих классов. Создайте несколько экземпляров от классов
#  Backend, Frontend, FullStack и вызовите их методы."""









