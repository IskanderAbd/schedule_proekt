# Vvedenie v funkcii

# anotaciya funkcii - komentarii k argumentam funkcii i vizvrashyaemomu znacheniu
# def func1(a: int, b: int) ->int: #parametry 
#   res = a+b    
#   return res
# num1 = (int(input('Veddite chisklo: ')))
# num2 = (int(input('Veddite chisklo: ')))
# print(func1(num1, num2)) #argumenty

# neobyazatelnyi argument
# def func_for_sum(a,b,c=3):
#     return a+b+c
# print(func_for_sum(1,2,0))

#pozicionnye i imenovanye argumenty

# def func2(x,y):
#     return x*y
# print(func2(2,3)) #poicionnoe 

# print(func2(y=2, x=5)) #imennovannye

# print(func2(y = 2,5))

# *args,  **kwargs 
# args - pozicionnye argumenty
# **kwargs - imennovannye argumenty
# def func5(a,b, *args,**kwargs):
#     print(2,4)
#     print(*args) #tuple
#     print(kwargs)
# func5(2,4,5,6,64,64,name='John')

#DRY - Dont repeat yourself - ne povtoraisya


def summ_(a,b):
    return a+b 
def raznost_(a,b):
    return a-b 
def umnojenie(a,b):
    return a*b
def delenie(a,b):
    return a/b 
while True:
    start = input('zapustit programmu? "da" ili "net": ')
    if start == "net":
        break

    elif start == "da":
        num1= int(input('enter ur first number:'))
        num2 = int(input('enter ur second number:'))
        operation = input('enter +, -, *, / :')
        if operation =='+':
            print(summ_(num1, num2))
        elif operation == '-':
            print(raznost_(num1, num2))
        elif operation == '*':
            print(umnojenie(num1, num2))
        elif operation == '/':
            print(delenie(num1, num2))
    else:
        print("you've entered another word")

def func_summ(*args):
    # sum_ = 0
    for i in args:

        print(b)
