lst = list(input('enter nums'))
list_ = {i**2 for i in lst}
dct = {i: i**2 for i in lst}
while True:
    # lst = list(input('enter nums'))
    print(lst)
    vopr = input('what you want? "lst","dct"')
    if vopr == 'lst':
        print(list_)
    elif vopr == 'dct':
        print(dct)

# def func():
#     print('res')

    
# def lop(summ):
#     while True:
#         pol = input('continue? y or n: ')
#         if pol == 'y':
#             func()
#         else:

#             break
# lop(func)

# import random
# def get_info():
#     name = (input('enter ur name: '))
#     surname = input('enter surname: ')
# def gen_pass(a):
#     passw = random.choice(0,9)
#     print(f'{name}{passw}')
# get_info(gen_pass)





# books = {'Financial': 'Theodor Draiser', 'Rich dad, poor dad': 'Robert Kiyosaki', 'Think and get rich': 'Napoleon Hill'}
# readers= {}   
# def return_():
#     global books
#     global readers
#     name = input('enter name: ')
#     confirmation = input(f'do you want to return {readers[name]}')
#     if confirmation == 'yes':
#         readers.pop()
# def get_info():
#     print(readers)
#     print(books)
# def take():
#     global books
#     global readers
#     print(f'choose book {books}')
#     name = input('....')
#     taken = books.pop(book)



    



