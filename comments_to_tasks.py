# 1) Дан список list_ = [1, 2, 3, 4]. Выведите сумму всех этих чисел.
# """
# list_ = [1, 2, 3, 4,]
# sum(list_)

# def sum(x,y):
#       return x+y

# res = reduce(sum,list_)
# print(res)

# from functools import reduce 
# list_ = [1, 2, 3, 4,]
# list2 = reduce(lambda x,y:x+y,list_)
# print(list2)











# for line in task:
      # print(line)



# 4)from functools import reduce

# a= [1,2,3,4,]
# b = reduce(lambda x,y:x+y,a,)
# print(b)
5
# a= [1,2,3,4,5,6,7,8]
# filtered_numbers= list(filter(lambda x:x%2==0,a))
# print(filtered_numbers)

6 


# def lcd(s):
#       return(len(s))
# a = "fffdssdaf"
# print(lcd(a))





# a= [1,2,3,4,6,8]
# b = (lambda x: if x % 2==0,a)
# print(b)


# a= [1,2,3,4,6,8]
# def sum (a):
#       return a%2==0
# sum(a)




# 1) list comprehension 
# a = [i+100 if i %2!=0 else i for i in range(1,51)]
# print(a)
# 2 dict comprehension 
# a = {i:i**2 for i in range(1,11)}
# print(a)

# 3) try - except
# def divide ():

#       try:  
#             x = int(input('enter any number:'))
#             y = int(input('enter any number:'))
#             print (x/y) 
#       except ZeroDivisionError:
#             print('you can not divide for zero')
#       except ValueError:
#             print('this operation do not support')
# divide()
