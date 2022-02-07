import schedule
import time
import csv

def write_csv():
    name = input('enter ur name: ')
    age = input('enter age: ')
    with open('users.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter='/')
        writer.writerow(
            (name, age)
        )
    answ = input('continue? y or n: ')
    if answ == 'y':
        write_csv()
    else:
        print('stop')

def mailing():
    with open('users.csv', 'r') as csv_file:
        data = csv_file.readlines()
        names = [i.replace('\n','')for i in data]
        for i in names:
            name = i.split('/')
            if int(name[-1]) >=18:
                print(f'skidki segodnya {name[0]}')

schedule.every(3).second.do(mailing)

while True:
    schedule.run_pending()
    time.sleep(1)

# write_csv()
# mailing()


# class Info:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age

#     def check(self):
#         if self.age > 18:
#             print('pokypai vodky so skidkoi')
#         else:
#             print('uchi uroki debil')


#     def write_csv(self):
#         with open('info.csv', 'a') as csv_file:
#             writer = csv.writer(csv_file, delimiter='/')

#             writer.writerow(
#                 (
#                     self.name
#                     self.age
                    
#                 )
#             )
