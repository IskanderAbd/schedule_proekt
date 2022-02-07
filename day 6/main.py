# lst = ['hello', 1, ['hello world', 5, [true]]]
# print(type(lst))
# print(lst[2][1])

# metody spiskov
# list. append(x)
# lst = ['tom', 'bob', 'bob']
# lst.append('jessika')
# print(lst)
# list.extend(l) rasshirenie spiska
# lst = ['some data1', 'some data2']
# lst2 = ['some data3', 'some data4']
# lst.extend(lst2)
# print(lst)

# list.insert(i, x) vstavlyaet na i-nyi element znacheniya x
# lst = ['h', 'e','l', 'l', 'o']
# lst.insert(1, 'ne')
# print(lst)

# list.remove(x udalyaet pervyi element imeyshii element x)
# lst = ['h', 'e','l', 'l', 'o']
# lst.remove('l')
# print(lst)

# list.pop([i]) udalyaet i-nyi element, esli indeks ne ukazan to udalit poslednii,
#  i vizvrashaet znachenie
# lst = ['h', 'e','l', 5, 2, 'l', 'o']
# removed_elem = lst.pop(1) #e
# print(lst)
# print(removed_elem)

# list.index(x, [start [, end]]) vozvrashyaet polojenie elementa(indeks)
# lst = ['h', 'e','l', 'l', 'o']
# print(lst.index('l'))
# print(lst.index('l', 0, 4))

# list.count(x) podshet elementov so znacheniem x
# lst = ['h', 'l', 'e','l', 1, 8, 'l', 'o']
# print(lst.count('l'))

# list.sort() sortirovka
# lst = [5, 2, 4, 2, 1]
# lst.sort()
# print(lst)

# list.reverse() razvorachivaet spisok
# lst = [5, 2, 4, 2, 1]
# lst.sort()
# lst.reverse
# print(lst[::-1])

# list.clear() ochishyaet spisok
# lst = [1, 5, 1, 1, 1, 'hello']
# lst.clear()
# print(lst)

# lst = ['w', 'o', 'r', 'l', 'd']
# result = ''. join(lst)
# print(result)

# kopirovanie spiskov
# kak delat nelzya
# lst1 = ['hello', 'world']
# lst2 = lst1
# lst1.append('HELLO')
# print(lst1)

# copy( poverhnostnoe kopirovanie spiskov)
# lst1 = ['hello', 'world']
# lst2 = lst1.copy()
# lst1.append('HELLO')
# lst1[-1]
# print(lst2)

# deepcopy( )
# import copy
# lst1 = ['hello', 'world']
# lst2 = copy.deepcopy(lst1)
# lst1[-1][-1].pop()
# print(lst2)

# list_of_friends = ['Tom', 'John', 'Sam', 'Jessika', 'Helen']
# for friend in list_of_friends:
#     if friend == 'Sam':
#         pass
#     else:
#         print(f'Welcome to the party!'{friend})

lst = [1, 2, 3, 4, 5, 76, 12, 9]
c = []
for i in lst:
    n = lst[i]
    if i < 7:
        lst.append(i)
print(lst)