# class A:  #---obyavili class

#     string = '' #peremenaya classa

#     def first_method(self): #method
#         pass

# first_obj = A() #sozdali ekzemplyar ot klassa
# second_obj = A()


# class Animal:
#     def __init__(self, name, animal_type):
#         self.name = name
#         self.animal_type = animal_type
#     def get_info(self):
#         print(f'Name is {self.name}, type is {self.animal_type}')

# dog = Animal('baks', 'dog')
# cat = Animal('barsik', 'cat')
# dog.get_info()
# cat.get_info()
# # print(dog.name)
# # print()
# class People:
#     def __init__(self,name,country):
#         self.name= name
#         self.country = country

#     def get_info(self):
#         print(f'hello, i\'m {self.name}')

#     def translate_hello(self, hello):
#         print(f'country is {self.country}, in our country hello is {hello}')

# american = People('tom', 'usa')
# kyrgyz = People('aibek', 'kg')
# russian = People('ivan', 'rus')

# # american.get_info()
# # kyrgyz.get_info()
# # russian.get_info()

# american.translate_hello('hello')
# kyrgyz.translate_hello('hello')

# class SelfBank:
#     total = 0

#     def add_summ(self, sum_):
#         self.total += sum_
#         return self.total
#     def get_total_summ(self):
#         return self.total
    
#     def min_summ(self, sum_):
#         if self.total - sum_ <0:
#             print('nedostatochno sredtv')
#             return self.total
#         self.total -= sum_
#         return self.total

# john = SelfBank()
# print(john.get_total_summ())
# john.add_summ(1000)
# john.min_summ(250)
# # john.min_summ(1000)
# # print(john.get_total_summ())

# jessika = SelfBank()
# print(jessika.get_total_summ())

# class Car:
#     car_count = 0

#     def __init__(self):
#         Car.car_count +=1

# car1 = Car()
# print(car1.car_count)
# car2 = Car()
# print(car2.car_count)


# class A:
#     def method1(self):
#         print('hello')

#     def method2(self):
#         pass

# obj_a = A()
# print(obj_a.__dir__())



    # number = input('enter num1: ')
    # number2 = input('enter num1: ')
        



# class Calculator:
#         def __init__(self, num1, num2):
#             self.num1 = 

#         def min_nums(self):
#             return self.num1 - self.num2
        
#         def plus_nums(self):
#             return self.num1 + self.num2

#         def umnoj_nums(self):
#             return self.num1 * self.num2

#         def del_nums(self):
#             return self.num1 // self.num2

# obj1 = Calculator(150, 50)
# obj2 = Calculator(15, 90)
# obj3 = Calculator(30, 30)
                       
# for i in [obj1, obj2, obj3]:
#     print(i.add_nums)
#     print(i,min_nums)

def factorial_recursive(n):
    if n ==1:
        return n
    else:
        return n * factorial_recursive(n-1)

print(factorial_recursive(5))