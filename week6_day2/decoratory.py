# def func1():
#     return 'smth'

# def func2(func):
#     print('before func calling')
#     print(func())

# func2(func1)

# def func_dec(function_to_decorate):
#     def wrapper():
#         print('Kod, kotoryi otrabatyvaet do vyzova funkcii')
#         function_to_decorate()
#         print('Kod, kotoryi otrabatyvaet posle vyzova funkcii')
#     return wrapper

# @func_dec
# def func1():
#     print('Prosto funkciya')

# func1()

# def bread(func):
#     def wrapper():
#         print('--/ bread \--')
#         func()
#         print('--/ bread \--')
#     return wrapper

# def ingridients(func):
#     def wrapper():
#         print('--| tomato |--')
#         func()
#         print('--\ salad\--')
#     return wrapper

# @ingridients
# @bread
# def get_sandwich(meat='__ham__'):
#     print(meat)

# get_sandwich()

# def benchmark(func):
#     import time

#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print(f'func execution is {end - start}')
#     return wrapper

# @benchmark
# def call_webpage():
#     import requests
#     webpage = requests.get('https://google.com')
    
# call_webpage()
# @benchmark
# def iterate_list():
#     for i in range(1, 50000):
#         print(i ** 89 -20)
# iterate_list()

# def risuem(func):
#     def wrapper():
#         hat = '-_o_-'
#         body = '-/[]\-'
#         func()
#         legs = '__'
#     return wrapper

# @risuem
# def human(legs = '-/\-'):
#     print(legs)
# human()

# def decorater(func):
#     def wrapper(arg1):
#         print(f'Got some word {arg1}')
#         func(arg1)
#     return wrapper

# @decorater
# def func(word):
#     print(f'Got word is {word}')

# func('yes')

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f'see args {args}')
#         print('see kwargs {kwargs}')
#         func(*args, **kwargs)
#     return wrapper
# @decorator
# def func_without_params():
#     print('func without params')
# @decorator
# def func_with_params(first_name, last_name):

#     print('func with params')
#     print(f'hello, {first_name}, {last_name}')
# @decorator
# def func_with_params_kwargs(first_name, last_name):
#     print('func with kwargs')
#     print(f'HELLO, {first_name} {last_name}')
   
# func_without_params()
# func_with_params('jack', 'tour')
# func_with_params_kwargs(first_name='jack', last_name='jackson')



def benchmark(iters):
    def actual_decorator(func):
        import time 
        def wrapper(*args, **kwargs):
            total =0
            for i in range(iters):
                start = time.time()
                func_call = func(*args,**kwargs)
                end = time.time()
                total = total + (end - start)
            print(f'srednee vremya vypolneniya {total / iters}')
            return func_call
        return wrapper
    return actual_decorator
@benchmark(iters = 20)
def get_webpage(url):
    import requests
    webpage = requests.get(url)

get_webpage('https://yandex.ru')