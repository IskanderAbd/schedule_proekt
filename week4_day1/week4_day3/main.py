# lambda
# def add_nums(a,b):
#     return a+b
# result = add_nums(5, 10)
# print(result)

# result = lambda a, b:a + b
# print(result(10, 20))

# map()
# lst = [1, 2, 3, 4, 5]
# # result  = list(map(lambda x: str(x), lst))
# def do_str(x):
#     return str(x)
# result = list(map(do_str, lst))
# print(result)

# filter

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # result = list(filter(lambda x: x >5, lst))
# def filter_this(x):
#     return x > 5
# result = list(filter(filter_this, lst))
# print(result)

# reduce()
# from functools import reduce
# lst = [1, 2, 3, 4, 5]
# result = reduce(lambda x, y: x + y, lst)
# print(result)

# def summ_this(x, y):
#     return x+y
# result = reduce(summ_this, lst)

# zip()
# employee_numbers = [2, 9, 18, 28]
# employee_names = ['helen', 'sam', 'jessika', 'james']
# employee_spheare = ['it', 'broker', 'cook', 'banker']
# zipped_values = zip(employee_numbers, employee_names, employee_spheare)
# zipped_list = list(zipped_values)
# print(zipped_list)

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # result = list(map(lambda x: 'chetnoe' if x % 2 == 0 else 'nechetnoe', lst))

# # print(result)

# def func(a):
#     return 'chetnoe' if a % 2 == 0 else 'nechetnoe'
# result = list (map(func, lst))
# print(result)
# db = {}
# def create():
#     global db 
#     name = input('enter name: ')
#     password = input('enter password: ')
#     db[name] = password
#     print(f'successfully created!{db}')
#     manager()

# def read():
#     print(f'users list: {db.keys()}')
#     manager()

def update():
    global db
    name = input('enter ur name: ')
    if name in db.keys():
        new_pass = input('enter new password: ')
        db[name] = new_pass
        print(f'successfully change {db}[name]') 
#     else:
#         print('users not found')

# def delete():
#     global db 
#     name = input('enter name: ')
#     current_pass = db[name]
#     password = input('enter password: ')
#     if current_pass == password:
#         db.pop(name)
#         print('successfully deleted')
#     else:
#         print('password do not match')
#     manager()
# def manager():
#     answ = input('choose operation(create(c), read(r), update(u), delete(d): ')
#     if answ == 'c':
#         create()
#     elif answ == 'r':
#         read()
#     elif answ == 'u':
#         update()
#     elif answ == 'd':
#         delete()

# manager()
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = list(map(lambda x:'bolshe' if x > 3 else 'menshe', lst))
# print(result)

# lst = ['iskander', 'aleksandr', 'anelya', 'sagynai', 'bob']
# from functools import reduce
# result = reduce(lambda x, y:y if len(x)<len(y) else x, lst)
# print(result)    