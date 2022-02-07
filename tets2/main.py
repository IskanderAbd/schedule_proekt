# b = {'world', 5, 'tom', True}
# c = {5, 7, 'hello'}


# set.issuperset() ---> proverka na nadmnojestvo
# a = {'hello', 1, 2, 'world'}
# b = {'hello', 1, 2}
# print(a.issuperset(b))
# print(b <= a)

# r =  {5, 7, 11, 10, 28}
# k = {29, 2, 6, 12, 3}
# m =  {1, 5, 14, 8, 22}
# if r.isdisjoint(k) == True:
#     print(k)
# elif r.isdisjoint(k) == False:
#     print('kale ne ugadal')
# elif r.isdisjoint(m) == True:
#     print(m)
# elif r.isdisjoint(m) == False:
#     print('m ne ugadal')

# lst = [1, 2, 3, 4, 5]
# a = ('')
# for el in lst:
#     lst.append(a)
#     print(a)

# lst = [1, 2, 3, 4, 5]
# lst_ = [str(i) for i in lst]
# print(lst_)

# print("Ноль в качестве знака операции"
#       "\nзавершит работу программы")
# while True:
#     s = input("Знак (+,-,*,/): ")
#     if s == '0':
#         break
#     if s in ('+', '-', '*', '/'):
#         x = float(input("x="))
#         y = float(input("y="))
#         if s == '+':
#             print("%.2f" % (x+y))
#         elif s == '-':
#             print("%.2f" % (x-y))
#         elif s == '*':
#             print("%.2f" % (x*y))
#         elif s == '/':
#             if y != 0:
#                 print("%.2f" % (x/y))
#             else:
#                 print("Деление на ноль!")
#     else:
#         print("Неверный знак операции!")

# dct = {'name': 24, 'age': 15}
# for key, value in dct.items():
#   if value %2 == 0:
#     dct[key] = 2
# print(dct)

# dct = {'pen':15,'pencil':10,'book':100}
# for key, value in dct.items():
#     print(key,value//5)

# dct = {'banana':55,'apple':13,'pineapple':77}
# dct2 = dct.copy()
# for key,value in dct.items():
#     if value & 2 !=0:
#         dct2.pop(key)
# print(dct2)

# dct = {'banana':55,'apple':13,'pineapple':77}
# for key in dct:
#     text = text.replace(key, dct[key])
# print(dct)

# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# lst2 = [int(i) for i in str_list]
# print(lst2)

# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dct = {i: list(range(1,b + 1)) for i , b in a.items()}
# print(dct)

# a = {'a'::;}
# print(a)
# if a !=0:
#     print(a)
#     if b != 0:b

# print('a')
# try:
#     num1/num2
# except ValueError: