# def __init__():
#     pass

# class A:

#     def __init__(self, num):
#         self.num = num
    
#     def __add__(self, other):
#         print('ADD METHOD IS WORK')
#         return self.num + other.num

#     def __sub__(self, other):
#         print('SUB METHOD IS WORK')
#         return self.num - other.num

#     def __gt__(self, other):
#         print('GREAT THEN METHOD IS WORKED')
#         return self.num > other.num

#     def __lt__(self, other):
#         print('LESS THEN METHOD IS WORKED')
#         return self.num < other.num

#     def __eq__(self, other):
#         print('EQUAL METHOD IS WORKED')
#         return self.num == other.num

# obj1 = A(5)
# obj2 = A(15)
# # print(obj2 + obj1)
# # print(obj2 - obj1)
# # print(obj2 > obj1)
# print(obj2 == obj1)

# class C:
#     def __new__(cls, *args):
#         new_obj = object.__new__(cls)
#         print('C class __new__ gets called')
#         return new_obj
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         print('C class __init__ gets called')
# obj = C('Gas', 51)

# class B:

#     def __init__(self, data):
#         self.data = data
    
    # def __str__(self):
    #     return f'vyzvan metod str kotoryi pomogaet otbrajat object dlya polzovatelya bolee ponyatno'

    # def __repr__(self):
    #     return f'B({self.data!r})'

# obj = B('hello')
# print(obj)
# new_obj = eval(repr(obj))
# print(new_obj.data)

# class Person:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = name

#     def __getattr__(self, name):
#         print(name)
#         print('!!!srabotalo GETTATTR')
    
#     def __getattribute__(self, name):
#         print('!!!srabotalo GETTATTRRIBUTE')
#         return super().__getattribute__(name)        

# obj = Person('tom', 30)
# print(obj.surname)


# class Som:

#     currencies = {
#         'USD': 84.5,
#         'EUR': 96,
#         'RUB': 1.1,
#         'KZT': 0.2,
#         'SOM': 1
#     }
#     def __init__(self, value, curr):
#         self.value = value
#         self.curr = curr

#     def __add__(self, other):
#         curr1 = Som.currencies.get(self.curr)
#         curr2 = Som.currencies.get(other.curr)
        
#         print(f'{self.value * curr1} som i {other.value * curr2} som')
#         return self.value * curr1 + other.value * curr2 

#     def __add__(self, other):
#         curr1 = Som.currencies.get(self.curr)
#         curr2 = Som.currencies.get(other.curr)
        
#         print(f'{self.value * curr1} som i {other.value * curr2} som')
#         return self.value * curr1 - other.value * curr2 

# a = Som(100, 'USD')
# b = Som(50, 'EUR')
# # print(a + b)
# print(a + b)






# class Distance:

#     units_M = {
#         'SM': 0.01,
#         'DM': 0.1,
#         'M': 1,
#         'KM': 1000,
#         'Miles': 1600

#     }

#     def __init__(self, value, unit):
#         self.value = value
#         self.unit = unit

#     def __gt__(self, other):
#         dist1 = Distance.units_M.get(self.unit)
#         dist2 = Distance.units_M.get(other.unit)
#         print(f'{self.value * dist1} M and {other.value * dist2}')
#         return self.value *dist1 > other.value * dist2

# a = Distance(1000000000000000000000000000000, 'KM')
# b = Distance(5000000000000000000000000000, 'Miles')
# print(a>b)

# """Создайте два класса A и B. В обоих классах есть метод count. 
# В классе A он подсчитывает, сколько гласных букв в слове, которое передается в качестве аргумента в методе count, 
# а в классе B он подсчитывает количество согласных. Создайте объекты от этих классов и вызовите этот метод у каждого объекта"""

# class A:
#     def __init__(self, num):
#         self.num = num
#     def __add__(self, other, other_2, other_3):
#         return self,num +other.num +other_2.num + other_3.num

# obj = A(10)
# obj2 = A(15)
# obj3 = A(25)
# obj4 = A(50)
# #     def count(self,word):
#         self.word = word
#         for gs in word:
#             if gs 

# class B:
#     def count(self):

# + -> __add__
# - -> __sub__
# / -> __div__
# * -> __mul__
# % -> __mod__

# == -> ___eq_
# != -> __ne__


# class MyClass:
#     def __init__(self, name, age):

#         self.name = name
#         self.age = age

#     def __setattr__(self, name, value):
#         print(f'i want to set attribute {name} with value {value}')
#         self.__dict__[name] = value

#     def __delattr__(self, name):
#         print(f'i want to del attr name is: {name}')
#         return super().__delattr__(name)

#     def __getattr__(self, name):
#         pass
#     def __getattribute__(self, name):
#         return super().__getattribute__(name)


# obj = MyClass('john', 30)
# obj.surname = 'snow'
# obj.__delattr__('age')
# print(obj.__dict__)

# class Account:
#   def __init__(self, name, balance, towns):
#     self.name = name
#     self.balance = balance
#     self.towns = towns
#     print('sozdau schet...')
#   def __repr__(self):
#     return f'{self.name} {self.balance}'
#   def __str__(self):
#     return f'privet {self.name}, {self.balance} '
#   def __del__(self):
#     return f'udalenie...Poka!'

# obj = Account('iska',100, 'bishkek')
# print(obj.__init__())
# print(obj.__repr__())
# print(obj.__str__())
#     del obj