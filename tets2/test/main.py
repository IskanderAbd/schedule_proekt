# lst = ['iskanderr', 'beka', 'bob']
# result = list(filter(lambda x: len(x)>7, lst))
# print(result)

# num1 = 1
# num2 = 2
# num3 = 3
# result = list(filter(lambda x: max(x), num1, num2, num3))
# print(result)


# lst = [1, 2, 3, 4, 5, 6, 7]
# result = list(filter(lambda x: x%2 == 0, lst))
# print(result)

# list_ = [-1, 2, 3, 0, 5, -3, 7]
# result = list(map (lambda x:True if x>0 else False, list_))
# print(result)
lst = input('enter smth: ')
lst2 = lst[::-1]
if lst == lst2:
    print('verno')
else:
    print('neverno')
