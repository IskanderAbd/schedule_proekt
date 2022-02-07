# Обработка исключений. Оператор try- except

# Ошибки

# 1) SyntaxError - забыли двоеточие забыли скобку
# неправильно назвали переменную
# age = 2
# print(
# 2age = 2

# 2) IdentetionError - непарвильный отступ
    # 2

# 3) TabError - неправильная табуляция (смешивание пробелов и табов)
# if True:
#     print('f1')
#     print('f2')

#  Исключения

# ZeroDivisionError - ошибка деления на ноль
# 2/0

# NameError - когда имя не обнаружено
# name

# TypeError - когда тип объекта не подходит для операции 
# res = 2 + '2'

# ValueError - когда тип объекта подходит для операции, 
# но его значение нет
# a = '2'
# b = 'abc'
# c = '1.5'
# g = 1.5

# print(int(c))


# IndexError - obrashenie k nesushestvueshyemu indexy
# a =[1, 2, 3]
# print(print(a[3]))

# kyeerror - obrashenie k nesushestvuyshemu klychu
# dct_ = {'a: 2'}
# print(dct_['b'])

# importError - nepravilnyi import
# from math import pi2

# modulenotFoundError - ne mojet naiti modul dlya importa 
# import math2

# AttributeError - pytaemsya vyzvat nesishestvueshii atribut ili metod u obekta
# a = 'Hello'
# a.append

# KeybordInterrupt - cntr + c
# while True:
    # print(;hello)

# obrabotka iskluchenii - operator try - expect

# try:
#     pass #popytaisya chto nibud sdelat
# expect:
#     pass #esli vozniklo iskluchenie obrabotai ego

# try:
#     print(name)
# except: #goloe iskluchenie
#     print('takoi peremennoi net')

# from typing import NamedTuple


# try:
#     print(name)
#     2 / 0
# # except ZeroDivisionError:
# #     print('net takoi peremennoi')
# # except NamedError:
# #     print('net takoi peremennoi')
# except(ZeroDivisionError, NamedError):
#     print('hffj')

# try:
#     age = int(input('age:'))

# except ValueError:
#     print('vvedite chislo!')
#     age = 0

# num1 = 10
# num2 = 0
# try:
#     res = num1/ num2 
# except ZeroDivisionError:
#     res = 0
# print(f'delenie ravno = {res}')
# print(res)

# from typing_extensions import ParamSpecArgs


# try:
#     while True:
#         print('hello')
# except KeyboardInterrupt:
#     pass

# print('1')
# print('2')


# try:
#     num1 = int(input('vvedite pervoe chislo:'))
#     num2 = int(input('vvedite vtoroe chislo:'))
# except (ValueError, ZeroDivisionError):
#     print('oshibka v programme!')



# try:
#     num1 = int(input('vvedite pervoe chislo:'))
#     2/0
# except Exception as e:
#     print(type(e))


# from os import name


# try:
#     print(name)
# except NameError:
#     print('NameError')
# else:
#     print('esli except ne srabotalo')
# finally:
#     print('zavershilsya blok koda')

# ////////////////// raise
# age = int(input('enter age:'))
# if age <18:
#     raise Exception('vy sloshkom maly')


# try:
#     age = int(input('enter ur age:'))
#     if age < 18:
#         raise Exception
# except:
#     print('vy slishkom maly')

def foo():
    var = 'переменная foo'

    def bar():
        var = 'переменная bar'

    bar()
    print("переменная в foo: ", var)

foo()
print("переменная в foo: ", var)
