# class Salary:

#     def __init__(self, pay):
#         self.pay = pay

#     def get_total(self):
#         return (self.pay * 12)
    
# class Employee:
#     def __init__(self, pay, bonus):
#         self.pay = pay
#         self.bonus = bonus
#         self.salary = Salary(self.pay)

#     def total_salary(self):

#         return f'Total: {self.salary.get_total() + self.bonus}'

    
# obj = Employee(100, 10)
# print(obj.total_salary())




# class Engine:
#     def __init__(self, vol):
#         self.volume = vol

#     def amount_of_fuel_consumed(self):
#         if self.volume == 2:
#             print('rashod: 10l/100km')
#         elif self.volume == 3:
#             print('rashod: 15l/100km')
#         elif self.volume == 4:
#             print('rashod: 20l/100km')


# class Car:
#     def __init__(self, name, vol):
#         self.name= name
#         self.volume = vol
#         self.engine = Engine(self.volume)
    
#     def get_info(self):
#         self.engine.amount_of_fuel_consumed()
#         print(f'name is: {self.name}')

# obj = Car(' BMW', 3)
# obj.get_info() ---------------composiciya




# class Salary:              #---------oblegaciya

#     def __init__(self, pay):
#         self.pay = pay

#     def get_total(self):
#         return (self.pay * 12)

# class Employee:
#     def __init__(self, pay, bonus):
#         self.pay = pay
#         self.bonus = bonus
        

#     def total_salary(self):

#         return f'Total: {self.pay.get_total() + self.bonus}'

# salary = Salary(100)
# employee = Employee(salary, 10)
# print(employee.total_salary())


# class Engine:
#     def __init__(self, vol):
#         self.volume = vol

#     def amount_of_fuel_consumed(self):
#         if self.volume == 2:
#             print('rashod: 10l/100km')
#         elif self.volume == 3:
#             print('rashod: 15l/100km')
#         elif self.volume == 4:
#             print('rashod: 20l/100km')


# class Car:
#     def __init__(self, name, vol):
#         self.name= name
#         self.volume = vol
        
    
#     def get_info(self):
#         self.volume.amount_of_fuel_consumed()
#         print(f'name is: {self.name}')

# # obj = Car(' BMW', 3)
# obj_eng = Engine(4)

# obj = Car(' BMW' ,obj_eng )

# obj.get_info() 


# principy OOP:
# 1. Nasledovanie/osnovnoe
# 2. Polimorfizm/osn
# 3. Incopsulyaciya/osn
# 4. Abstrakciya
# 5. Kompoziciya
# 6. Agregaciyz


# from abc import ABC, abstractmethod
# class Salary:
#     @abstractmethod
#     def det_salary(self):
#         pass

# class IT(Salary):
#     def get_salary(self, salary):
#         print(f'my salary is: {salary}')

# class HR(Salary):
#     def get_salary(self, salary):
#         print(f'my salary is: {salary}')

# obj_it = IT()
# obj_hr = HR()
# obj_it.get_salary(2000)
# obj_hr.get_salary(1000)



# class User:
#     def __init__(self, name, password):
#         self.name = name
#         self.__password = password

#     def get_user_info(self):
#         answer = input('Enter ur password: ')
#         if answer == self.__password:
#             print(f'Username: {self.name}, password: {self.__password}')
#         else:
#             print('password is incorrect')

#     def set_new_password(self):
#         answ = input('do u realy want to change ur password? y or n: ')
#         if answ =='y':
#             new_pass = input('Enter new password: ')
#             self.__password = new_pass
#             return self.__password
        

# obj = User('Helen', 'pass123')
# print(obj.name)
# print(obj.__password)

# obj.set_new_password()
# obj.get_user_info()




# class Info:
#     def __init__(self,name, password):
#         self.name = name
#         self.__password = password

#     @property
#     def get_user_info(self):
#         answer = input('Enter ur password: ')
#         if answer == self.__password:
#             return self.__password
       
#     def set_password(self):
#         answ = input('enter new password: ')
#         self.__password = answ



# obj = Info('iska', '123')
# obj.set_password = 'hello'
# print(obj.get_user_info)





# class Name:
#     def __init__(self, file_name):
#         self.file_name = file_name

#     def write_data(self):
        
#         with open(f'{self.file_name}', 'a')as f:
#             while True:
#                 answ = input('write down data? y or n: ')
#                 if answ == 'y':
#                     text = input('enter data/text: ')
#                     f.write(text)
#                 else:
#                     break

                


#     def read_data(self):
#         with open(self.name, 'r') as f:
#             return f.read()

# obj = Name('text.txt')
# obj.write_data()
# print(obj.read_data())

# def __init__(self, file): ---------------pravilnyi variant
#         self.file = file
#     def write_data(self):
#         with open(self.file, 'a') as f:
#             while True:
#                 answ = input('Write down data? y/n')
#                 if answ == 'y':
#                     text = input('Enter text: ')
#                     f.write(text + '\n')
#                 else:
#                     break
    
#     def read_data(self):
#         with open(self.file, 'r') as  f:
#             for i in f.readlines():
#                 print(i)
# obj = Book('text.txt')
# obj.write_data()
# print(obj.read_data())




# 3. создать лифт, в котором будет возможность переключать этажи, также должна быть переменная, которая будет хранить текущий этаж
# должны быть следующие методы: 
# get_curr_fl() - получение текущего этажа
# up_one() - вверх на один этаж
# down_one() - вниз на один этаж
# up(n) - вверх на n этажей
# down(n) - вниз на n этажей
# каждое перемещение должно сопровождаться сообщениями о том на каком этаже находится человек
# Ограничения: в здании 20 этажей, соответственно, выше 20го этажа и ниже 1го ехать нельзя

# obj.get_curr_fl() -> Вы сейчас на 1 этаже
# obj.up_one() -> Вы сейчас на 2 этаже
# obj.up_one() -> Вы сейчас на 3 этаже
# obj.down_one() -> Вы сейчас на 2 этаже

# obj.up(5) -> Вы сейчас на 3 этаже -> 4 -> 5

class Lift:
    floor =1

    def get_curr_fl(self):
        print(f'you are in {self.floor}')
    def up_one(self):
        self.floor +=1
        print(f'you are in {self.floor}')
    def down_one(self):
        self.floor -=1
        print(f'you are in {self.floor}')

    def up(self, num):
        if self.floor >=21:
            print('error')
        else:
            print(f'you are in {self.floor}')
                 
    def down(self, number2):
        print('vy seichas na {} etaje')

obj = Lift()
obj.get_curr_fl()
    
    
class Floor:
    floor = 1
    d