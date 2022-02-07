# a = set() izmenyaemyi interiruemai i v nem doljny xranitsya neizmenyaemaye 
#   -->(vmesto {})

# a = {'hello', 1, 'a', 'a'}
# print(a)

# a = {'a', True, 125}
# print(len(a))
# print('a' in a)

# set.isdidjoint(other) -- proveryaet na unikalnost'
# a = {'world', 1, 2}
# b = {'world', 5, 'john'}
# print(a.isdisjoint(b))

# a = {'world', 1, 2}          --- sravnenie
# b = {'world', 5, 'john'}
# c = {'world', 5, 'john'}
# print(b == c)
# 
# set.issubset() vse elementy set prinadlejat other
# a = {'hello', 1, 2, 'world'}
# b = {'hello', 1, 2}
# print(b. issubset(a))
# print(b <= a)

# set.issuperset() ---> proverka na nadmnojestvo
# a = {'hello', 1, 2, 'world'}
# b = {'hello', 1, 2}
# print(a.issuperset(b))
# print(b <= a)

# set.union(other, ...) 
# ---> obedinenie mnojestv
# b = {'world', 5, 'tom', True}
# c = {'5', 7, 'hello'}
# d = {15, 'helen'}
# print(b.union(c, d))
# print(b|c|d)

# set.intersection(other, ... ) - peresechenie mnojestv
# b = {'world', 5, 'tom', True}
# c = {5, 7, 'hello'}
# d = {15, 'helen'}
# print(b.intersection(c))
# print(b & c)

# set.difference(other, ...) raznica
# b = {'world', 5, 'tom', True}
# c = {5, 7, 'hello'}
# d = {15, 'helen'}
# print(c.difference(b))
# print(b - c)

# set.simmetric_difference(other) difference naoborot
# b = {'world', 5, 'tom', True}
# c = {5, 7, 'hello'}
# d = {15, 'helen'}
# print(b.symmetric_difference(c))
# print(b ^ c)


# set.copy() copiya mnojestv
# a = {'hello', 1, True}
# b = a.copy() 
# print(a)
# ne raspechatyvaet 'true' potomu chto 1=true 0= false

# set.update(other, ...) obedinenie beret 'a' i izmenyaet spisok
# b = {'world', 5, 'tom', True}
# c = {5, 7, 'hello'}
# d = {15, 'helen'}
# b.update(c, d)
# print(b)

# b |= c
# print(b)

# set.intersection_update(other, ...)
# b = {'world', 5, 'tom', True}
# c = {5, 7, 'hello'}
# b.intersection_update(c)
# print(b)
# b &= c


# b = {'world', 5, 'tom', True}
# c = {5, 7, 'hello'}
# b.difference_update(c)
# print(b)
# b -= c

# set.symmetric_difference_update(other)
# b = {'world', 5, 'tom', True}
# c = {5, 7, 'hello'}
# b.symmetric_update(c)
# print(b)

# set.add(elem) dobavlyaet element
# a = {'hello', 5, True, False}
# a.add('world')
# print(a)

# a = {'world', 5, True, False}
# a.remove('world') -- vydaet oshibku chto net takogo
# print(a)

# set.discard(elem) udalyaet element

# set.pop()
# a = {'world', 5, True, False}
# removed_elem = a.pop()
# print(removed_elem)

# set.clear() ochistka mnojestva
# a = {'world', 5, True, False}
# a.clear()
# print(a)

# from typing import List


# a = {'hello', True, 5}
# b = frozenset(a.copy())
# print(b)

# lst = [True, 5, 5, ' hello']
# lst = list(set(lst))
# print(lst)

# tuples --kortej
# tpl = tuple()- or -())
# print(tpl)

# tpl = (1, 'hello', [1, 2])
# tpl[-1].append('world')
# print(tpl)
# print(tpl.count)
# print(tpl.index('hello'))

# tpl = (5, )
# var = 5
# print(tpl == var)
# # print(type(tpl))

# a = {'world', 5, True, False}
# a.remove('worl
# ')
# print(a)