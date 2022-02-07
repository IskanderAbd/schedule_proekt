# LEGB - local enclosed global built - in

# x = 'eto globalnaya peremena'

# def some_func():
#     x = 'localnaya peremennaya'
#     print(x)
#     def some_func2():
#         x = 'localnaya peremennaya'
#         print(x)
#     return some_func2()
# print(x)

# locals(), globals()
# x = 'hello'
# def some_func():
#     print('hello')
# #print(globals())
# print(x is globals()['x'])

# globals()['new data'] = 'Some data'
# print(globals())

# def func():
#     x = 'hello'
#     locals()['y'] = 525
#     print(locals())
#     def child_func():
#         x = 100
#         print(locals())
#     return child_func()
# func()

# counter = 0
# def counter_():
#     global counter
#     counter += 1
#     print(counter)
# counter_()
# counter_()
# counter_()

# nonlocal
# def f():
#     x = 20
#     def g():
#         nonlocal x
#         x = 40
#     g()
#     print(x)
# f()

# some_func()

# def manager():
#     some_func()

# def some_func():
#     print('hello, world')

# manager()

# CRUD - create read/retrieve update delete

# def create():
#     logic
#     create succsess
# def manager():
#     create? -> y
#     create()

# /////////////////////
# chistaya funkciya 
# def sum(a,b):
#     return a + b
# print(sum(3, 6))

# import random 
# print(random.random())
# print(random.random())

# my_list = [12, 34, 3, 45]
# def sort_by_sort(li):    #sortiruet izmenyaya 
#     li.sort()
#     print(li)
# sort_by_sort(my_list)
# print(my_list) 

# my_list = [12, 34, 3, 45]
# def sort_by_sort(li):
#     print(sorted(li))     #sortiruet ne izmenyaya
#     return sorted(li)
# sort_by_sort(my_list)
# print(my_list) 

# FVP - funkcii vyshego poryadka / mojet prinimat argument i vyvodit funkciu
# def func(num):
#     return num ** 2

# def fvp_func(fun, num):
#     return fun(num)+ fun(num)
# print(func(4))
# print(fvp_func(func, 4))


# def func(num):
#     num ** 2
# def func(fun, num):
#     fun(num) + fun(num)
#     return fun
# print(func)

# (), globals()
# x = 'hello'
# def some_func():
#     print('hello')
# #print(globals())
# print(x is globals()['x'])

x = 'Я глобальная переменная!'
def func():
  global x
  x = 'Я могу изменяться'
  print(x)
print(x is globals(['x']))