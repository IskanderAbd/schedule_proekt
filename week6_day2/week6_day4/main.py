# class A:

#     class_variable = None

#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname

#     def method(self):
#         pass
    
# obj1 = A()

# class A:
#     def hello(self):
#         print('hello, i\'m class A')
    
# class B(A):
#     def hello(self):
#         print('hello, I\'m class B')

# class C(B):
#     def hello(self):
#         print('hello, im class C')

# obj_a = A()
# obj_b = B()
# obj_c = C()

# for obj in [obj_a, obj_b, obj_c]:
#     obj.hello()

# super()

# class A:
#     def print_hello(self):
#         print('hello i\'m class A')

# class B(A):
#     def print_hello(self):
#         # super(B, self).print_hello()
#         # super().print_hello()
#         print('hello i\'m class B')
    
# obj_b = B()
# obj_b.print_hello()

# class Person:

#     def __init__(self, name, last_name, id_num):
#         self.name = name
#         self.last_name = last_name
#         self.id_num = id_num

#     def get_info(self):
#         print(f'{self.name} {self.last_name} {self.id_num}')

# class Employee(Person):

#     def __init__(self, name, last_name, id_num, position, salary):
#         self.salary = salary
#         self.position = position
#         super().__init__(name, last_name, id_num)

#     def get_full_info(self):
#         super().get_info()
#         print(f'{self.salary} {self.position}')

# empl_1 = Employee('jack', 'jackson', 105, 'IT-specialist', 50000)
# empl_1.get_full_info()


# static mothody
# issubclass, isinstance

# class Animal:
#     animal_sound = 'aaaaaaa'

#     def sound(self):
#         return self.animal_sound

# class Cat(Animal):
#     animal_sound = 'meow'
#     @staticmethod
#     def sound():
#         return 'meow'
#     @staticmethod
#     def jump():
#         return 'i can jump'
    

# class HomeCat(Cat):
#     pass
# # print(issubclass(HomeCat, Animal))
# # print(isinstance(cat, Animal))  # --- opredelyaet yavlyaetsya li objektom ot class

# class Lion(Cat):
#     animal_sound = 'roar'

# cat = Cat()
# # print(cat.jump())
# # print(issubclass(Cat, Animal))  #-- proveryaet dochernyaya li klass




# Создать 2 класса CheckUser, LoginOrRegisterUser, 1й проверяет возраст больше или меньше 18, 
# второй метод проверяет пароль, который должен состоять из чисел и букв, т
# ретий метод проверяет был ли зарегистрирован пользователь

# второй класс: должен хранить список всех пользователей 
# в формате: [{username: username, age: age, password, login:False}], метод register_user проверяет пароль если все ок регистрирует, login_user проверяет зарегистрирован ли пользователь ранее, если да то спрашивает никнейм и меняет статус логин на True, 
# метод для получения всех пользователей, только имена, метод для рассылки,
#  рассылку могут получать только зарегестрированные пользователи старше 18 лет








class CheckUser:
    def check_age(self,):
        if self.age >=18:
            return True

    def check_password(self):
        if self.password.isalpha() or self.password.isdigit(): 
            print('tolko chisla i simvoly')
            return False
        else:
            return True
    def check_user_in_list(self):
        name = input('enter ur name: ')
        if name in [i['username']for i in self.users]:
            return True
        else:
            return False

# age = CheckUser()
# age.self = 




class LoginOrRegisterUser(CheckUser):

    users = []

    def __init__(self, username, age, password):
        self.age = age
        self.password = password
        self.user = username
        self.login = False
        
    def register_user(self):
        if super().check_password():
            user = {
                'username': self.username,
                'age': self.age,
                'password': self.password,
                'login': self.login
            }
            self.users.append(user)
            print('uspeshno')
    def login_user(self):
        if super().check_user_in_list():
            for user in self.users:
                if user['username'] == self.username:
                    user['login']== True
            print('uspeshnyi vhod v sistemu')
            print(self.users)
        else:
            print('takogo polzovatelya net')



    def get_users_list(self):
        print([i['username']for i in self.users])

    def mailing(self):
        if super().check_age() and super(). check_user_in_list():
            print('rasylka oformlena')
        else:
            print('rassylka ne dostupna')



user_jack = LoginOrRegisterUser('jack', 30, 'pass123')
user_jack.register_user()
# user_jack.login_user()

user_jack.mailing()
