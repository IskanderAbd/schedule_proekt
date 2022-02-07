# def test (*args, **kwargs):
#     print(args)
#     print(kwargs)

# test ('hello', 2,34)

# def hello_func(age, name= 'Guest'):
#     return f'hello, {name},you are'
# print(hello_func(20,'tom'))

# db = {'hello':123}
# print(db['hello2']) - oshibka
# rint(db.get('hello3') ne vydaet oshibku kak discard

# string = input('enter str: ').lower()
# def translate_str(string):
#     intab = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
#     outtab = "йцукенгшщзхъфывапролджэячсмитьбю"
#     trantab = str.maketrans(intab,outtab)
#     return string.translate(trantab)
# result = translate_str(string)
# print(result)

# import datetime
# hour_time = datetime.datetime.now().hour
# db = {'tom': '+999777888', 'helen':'+888777222','bob': ' +777555333'}
# def do_obeda(name, phone):
#     print('skidka na kofe, dlya IMYA, s nomerom NOMER')
# def posle_obeda(name, phone):
#     print(f'skidka na vypechku, dlya {name}, s nomerom{phone}')
# for name,phone in db.items():
#     if hour_time < 13:
#         do_obeda(name, phone)
#     else:
#         posle_obeda(name, phone)

# num = int(input('enter ur summ: '))
# def rub_(rub):
#     rub = 1.24
#     res = rub*num
# def usd_(usd):
#     usd = 1.24
#     res = usd*num
# def eur_(eur):
#     eur = 1.24
#     eur = eur*num
    

# lop = input(
#     operation = input('kakoi kyrs "rub" ili "usd" ili "eur"')
# if operation =='rub':
#             print(summ_(num1, num2))
# elif operation == '-':
#             print(raznost_(num1, num2))
# elif operation == '*':
#             print(umnojenie(num1, num2))
# elif operation == '/':
#             print(delenie(num1, num2))
# else:
#         print("you've entered another word")

# import random
# num = random.randint(1,10)
# def func1(a, b, c):
#     if num1 == num:
#         print('vy ugadali chislo')
#     elif num2 == num:
#         print('vy ugadali chislo')
#     elif num3 == num:
#         print('vy ugadali chislo')
#     elif num1, num2, num3 != num
#     print('vy ne ugadali')

# import random
# random_num = random.randrange(11)
# attemps = 3
# def check_attemps():
#     if attemps == 0:
#         print('u vas zakinchilis popytki')
#         return False
#     return True
# while check_attemps():
#     print('popo')
#     num = int(input('vvedite chislo'))
#     if num == random_num:
#         print('va ugadali chislo')
#         break
# attemps -= 1

# accounts = [[1, 5],[7, 3],[3, 5]]
# def func1(accounts):
#     res = []
#     for i in range(len(accounts)):
#         res.append(sum(accounts[i]))
#     return max(res)
# print(func1(accounts))
# /////
# def func(accounts):
#     return max([sum(i) for i in accounts])
# print(func(accounts))


# word = 'abcdefd'
# ch = 'd'
# def func1(word,ch):
#     try:
#         x = word.index(ch)+1
#     except ValueError:
#         return word
#     else:
#         word_start = word[:x]
#         word_end = word[x:]
#         return word_start [::-1] + word_end
# print(func1(word, ch))
