# range( - generator posledovatelnosti)

# for i in range(10):
#     print(i)

# list = list(range(1, 10))
# print(list)

# list_ = ['a','b','c','d']
# count_ = 0
# for i in list_:
#     print(f"pod indeksom{count_},hranitsya element-{i}")
#     count_ += 1

# for i in range(len(list_)):
#     print(f"pod indeksom{i},hranitsya element-{list_[i]}")

#     for j in 'hello':
#         print(j)

# ///////////////////////////////

# list comprehension

# list_ = []
# for i in range(0,10):
#     list_.append(i)
# print(list_)

# list_ = [i**2 for i in range(0,11)]
# print(list_)

# list_ = [i**2 for i in range(0,11) if i % 2 == 0]
# print(list_)

# 
# list_ = [i if i % 2 == 0 else i**3 for i in range(0,11)]
# print(list_)
# ///////////////////////////////////

# set camperhension - predstavlenie spiska

# set_ = {i for i in range(11)}
# print(type(set_))
# /////////////////////////

# dictionary comperhension - predstavlenie slovarya

# dict_ = {i: i **2 if i % 2 == 0 else i **3 for i in range {11}}
# print(dict_)

# import time 

# start = time.time()
# list_ = []
# for i in range(100):
#     list_.append(i)

# end = time.time()

# time_1 = end.time()
# list_2 = [i for i in range(100)]
# print(time_1 > time_2)

# list_= [1,1,2,2,3,3,4]
# dct = {i: list_.count(i)for i in list_}
# print(dct)

# list = list(range(1, 11))


# list_ = ['yes' if i % 2 == 0 else 'no' for i in list]
# print(list_)
