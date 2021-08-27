# """ 
# 1. Откройте файл task1.txt. В нём записаны числа от 1 до 10 в столбец. Выведите первые 5 элементов в вашем файле в терминал(Подсказка: используйте метод для построчного считывания).
# """
# # №1
# with open('/home/aziz/Desktop/makers/week4/task1.txt','r') as o: # мы указываем путь до директории где находится наш файл task1.txt
#       print(o.readline())
#       print(o.readline())
#       print(o.readline())
#       print(o.readline())
#       print(o.readline())


# # №2
# with open('/home/aziz/Desktop/makers/week4/task1.txt','rt') as o:
#       print(o.read(9))
# """
# 2. Откройте файл task2.txt. В нём записаны числа от 1 до 10 в столбец. Распечатайте все числа, не используя методы.
# """


# m = open('/home/aziz/Desktop/makers/week4/task2.txt','r')
# for numbers in m:
#   print(numbers)
# m.close()





# """
# 3. Откройте файл task3.txt в режиме записи. Запишите в него 10 любых чисел. Затем вернитесь в начало файла и распечатайте записанные числа.
# """

# Мы открываем наш файл по текущей директории '/home/aziz/Desktop/makers/week4/task3.txt','w') as r:
# используем метод (r.write('19,24,14,3,43,17,27,9,55')) прописываем любые числа.



# with open ('/home/aziz/Desktop/makers/week4/task3.txt','w') as r: 
#       print(r.write('19,24,14,3,43,17,27,9,55'))



# Мы открываем наш файл по текущей директории '/home/aziz/Desktop/makers/week4/task3.txt','r')
# используем метод 'w'(read) и просматриваем(читаем) содержимое.


# with open('/home/aziz/Desktop/makers/week4/task3.txt','r') as v:
#       print(v.read())


# """
# 4. Откройте файл task4.txt. В нём в нескольких строках записан текст. Прочтите содержимое и распечатайте количество строк.
# """



# q = open('/home/aziz/Desktop/makers/week4/task4.txt','r')
# w = q.readlines()
# print(len(w))
# q.close()












# """
# 5. Откройте файл task5.txt. В нём записаны целые числа. 
# Прочтите эти числа, затем найдите максимальное и минимальное числа. Затем запишите эти числа в новый файл task6.txt
# """
# # открываем файл task5.txt в режиме чтения r
# with open('task5.txt','r') as f: 
#       brt = [] # создаем пустой список 
#       brt2 = f.read() # указываем режим в котором будем работать 
#       for i in brt2.split(): #
#             brt.append(int(i)) # 
# # открываем файл task6.txt в режиме чтения записи w
# with open('task6.txt','w') as v:
#     print(max(brt), file=v) #
#     print(min(brt), file=v) #








