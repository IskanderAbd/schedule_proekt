# open(path, method)
# f = open('test.txt', 'r')
# print(f'1. {f.read()}')
# f.seek(0)
# print(f'2. {f.read()}')
# print(f.read(10))
# print(f.read(10))

# f = open('test.txt', 'rt')
# print(f)
# for line in f:
#     print(line)

# s|t read text - chtenie teksta
# r(read) chtenie dannyh
# w(write) otkryvaetfile dlya zapisi(sozdaet novyi file ili ochishyaet soderjimoe fila. esli file sushestvuet)
# x(exclusive) otkryvaet dlya zapisi tolko esli ego ne sushestvyet to est' sozdaet novyi 
# a(append) otkruvaet file dlya zapisi, dobavlyaet poslednii 


# f = open('test.txt', 'wt')
# f.write('hello world525!')
# f.close()

# try:
#     f = open()
#     f.write()

# finally:
#     f.close()

# f = open('test.txt', 'r')
# file_content = f.read()
# print(file_content)
# print('---------')
# print(f.tell())
# f.seek(50)
# print(f.read())
# f.close

# f = open('test.txt', 'r')
# # print(f.read())
# print(f.readline()) ----------- #chitaet po strochno
# print(f.readline())

# content = f.readlines() ------ delaet spisok iz strok
# print(content)

# f = open('test.txt', 'w+')
# # f.write('string1\n')
# # f.write('string1\n')
# f.writelines(['string1\n', 'string50\n'])
# f.seek(0)
# print(f.read())
# f.close

# f = open('test.txt', 'a+')
# f.writelines(['hello world\n', 'wprld hello\n'])
# f.close

# JSON(javascript object notation)

# frontend(form)-> JSON -> backend -> parse JSON -> PYTHONDATA
# file.json

# [{'name': 'tom', 'age':30},]

# data = {'name': 'tom', 'age':30}
# import json
# # print(type(data))
# json_obj = json.dumps(data)   ---- iz pythona perevoditsya v json
# # print(type(json_obj))
# python_obj = json.loads(json_obj)  ---- iz json v python
# print(type(python_obj))







# Python -> JSON
# dict -> object
# list - array
# tuple - string
# int - number
# True - true
# False - false
# None - null


# import json
# data = {'name': 'tom', 'age':30}
# with open('data.json', 'a+') as f:
#     json.dump(data, f)

# import json
# with open('data.json', 'r+')as f:
#     # python_obj = json.loads(f.read())
#     python_obj = json.load(f)
#     print(python_obj)

# def write_to_txt():
#     data = input('enter: ') + '\n'
#     with open('users_data.txt', 'a+') as file_:
#         file_.writelines(data)

# def manager():
#     while True:
#         write_to_txt()
#         answ = input('write more? y or n: ')
#         if answ == 'n':
#             break
# manager()