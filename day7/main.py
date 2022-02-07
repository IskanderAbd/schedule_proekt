counter = 0
while counter < 11:
    print(counter)
    counter += 1   
# for i in 'hello world':
    # print(i)

# operator break&continue
# for i in 'hello world':
#     if i == 'o':
#         continue
#     print(i*2)

# for i in 'hello world':
#     if i == 'o':
#         break
#     print(i*2)





# db = []
# while True:
#     data = input('enter some data: ')
#     db.oppend(data)
#     answ = input('Cuntinue? y or n')
#     if answ == 'n':
#         break

# for i in 'hello world':
#     if i == 'w':
#         break
#     print(i)
# else:
#     print('takoi bykvy net')

# lst = ['hello', 1, [True, False], 10]
# counter = 0
# for i in lst:
#     print(f'{counter}, {i}!')
#     counter += 1

# for item_num, word in enumerate(lst):
#     print(f'{item_num}, {word}!')

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