# slovari - izmenyaemyi tip dannyh, interiruenyi

# dct = {}
# print(type(dct))

# sintaksis {key: value}
# dct = {'name': 'john', 'age': 25, 'hobby':['fishing','football', [1,2,3]]}
# print(dct['name'][0])

# dct = dict([[1,2]])
# dct = dict(name='john')
# print(dct)

# metody slovarey

# dct = {'name': 'john', 'age': 25, 'hobby':['fishing','football', [1,2,3]]}
# dct.clear()
# print(dct)

# copy

# dct = {'name': 'john', 'age': 25, 'hobby':['fishing','football', [1,2,3]]}
# dct2 = dct.copy()
# dct2 ['name'] = 'john2'
# dct ['hobby'][0] = '2'
# print(id(dct['hobby']))
# print(id(dct['hobby']))
# print(dct) 

# deep copy 
# dct = {'name': 'john', 'age': 25, 'hobby':['fishing','football', [1,2,3]]}
# import copy

# from typing import dict

# dct2 = copy.deepcopy(dict)
# print(id(dct['hobby']))
# print(id(dct['hobby']))

# fromkeys() - sozdaet slovar s klychom i znacheniem po umolchaniu
# list = ['a', 'b', 'c']
# dct = dict.fromkeys(list,'john')
# print(dct)

# get() - vozvrashyaet snachenie klycha no esli ego net ne brocaet isklychenie a vozvrashyaet po umolchaniu none
# dct = {'name':'john', 'age':25}
# print(dct.get('name2', 'takogo klycha net'))

# values() vozvrashyaet znacheniya v slovare
# print(dct.values())

# dct = {'name':'john', 'age':25}
# item(), keys(), values()
# print(dct.keys())

# print(dct.values()) - vozvrashyaet znacheniya
# print(dct.keys() - vozvrashyaet kluchi)
# print(dct.item()) - vozvrashyaet klychi i znavheniya

# for key, value in dct.items():
#     print(key)
#     print(value)

# pop - udalyaet po klychui vozvrashyaet znacheniy
# dct = {'name':'john', 'age':25}
# k = dct.pop('name')
# print(k)
# print(dct)

# popitem() - udalyaet i vozvrashyaet kluch i znachenie
# k = dct.popitem()
# print(k)


# setdefault() - vozvrashyaet znachenie klycha no esli ego net, ne vydaet oshibky, a sozdaet klychi znacheniya po umolchaniu
# dct = {'name':'john', 'age':25}
# k = dct.setdefault('name')
# print(k)

# update() - obnovlyaet slovar, dobavlya kluch i znachenie esli takoi kluch sushestvuet to perezapisyvaet ego
# dct = {'name':'john', 'age':25}
# dct.update({'name': 'Snow'})
# print(dct)

# dct = {'name':'john', 'age':25}
# for key, value in dct.items():
#     print(key)
#     print(value)

# i = 0
# while i < len(dct):
#     k = list(dct.keys())[i]
#     print(k)
#     i += 1

dct = {'a':18, 'b': 20, 'c': 5, 'f': 30}
for key, value in dct.items():
    if value %2 == 0:
        dct[key] = 'yes'
    else:
        dct[key] = 'no'
print(dct)