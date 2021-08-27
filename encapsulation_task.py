# # Задания на тему "Инкапсуляция"

# """
# 1. Создайте класс и объявите в нём 3 метода: 
# публичный, защищённый и приватный. 
# Затем создайте экземпляр данного класса и в
# ызовите по очереди каждый из методов.
# """
# class A:
      
#       def __say_hello(self):
#           print('walk')
#       def _say_hello(self):
#           print('fighters')
#       def say_hello(self):
#           print('foo')
# a = A()
# a.say_hello()
# a = A()
# a._say_hello()
# a = A()
# a._A__say_hello()


# 2. Определите класс A, в нём объявите метод method1, 
# который печатает строку "Hello World". 
# Затем создайте класс B, который будет наследоваться от класса A. 
# Создайте экземпляр от класса B, и через него вызовите метод method1.

# class A:
#       def method1(self):
#             print('Hello wolrd')
# class B(A):
#       def method1(self):
#             super().method1()
#             pass
      
# b = B()
# b.method1()




# 3. Объявите класс Car, 
# в котором будет приватный атрибут экземпляра speed. 
# Затем определите метод set_speed, 
# который будет устанавливать значение скорости и метод show_speed, 
# с помощью которого Вы будете получать значение скорости.

# class Car:
#       __speed = 15 

#       def set_speed(self,new_speed):
#             self.__speed = new_speed
      
#       def show_speed (self):
#             print(self.__speed)
# a = Car()
# a.set_speed(20)
# a.show_speed()



# который будет устанавливать значение скорости и метод show_speed, 
# с помощью которого Вы будете получать значение скорости.

# 4. Перепишите класс Car из предыдущего задания.
# Перепишите метод set_speed() с использование декоратора @speed.setter, 
# а метод show_speed() с использованием декоратора @property, 
# для того чтобы можно было работать с данным классом следующим образом:
# car = Car()
# car.speed = 120
# print(car.speed)

class Car:
      __speed = 15 


      @property
      def speed (self):
            return self.__speed

      @speed.setter
      def speed(self,new_speed):
            self.__speed = new_speed
     
a = Car()
a.speed = 120
print(a.speed)

   
            


