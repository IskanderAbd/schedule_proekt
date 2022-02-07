# class SomeClassName:

#     def __init__(self):
#         self.public_attr = 'Public attr'
#         self._protected_attr = 'Protected attr'
#         self.__private_attr = 'private attr'

#     def public_method(self):
#         print('hello, public method')

#     def _protected_method(self):
#         print('hello, protected method')

#     def __private_method(self):
#         print('hello, private method')

# obj = SomeClassName()

# print(obj.public_attr)
# print(obj._protected_attr)
# print(obj.__private_attr)

# obj.public_method()
# obj._protected_method()
# obj.__private_method()

# class SomeClass:
#     def __init__(self):
#         self.__private_attr = 'Private attr'
#         self.attr = 'Simple attr'

#     def get_private_attr_info(self):
#         print('return some private attr')
#         return self.__private_attr

#     def set_private_attr(self, new_val):
#         print('i help you set new value, for private attr')
#         self.__private_attr = new_val
#         return self.__private_attr

# obj = SomeClass()
# print(obj.get_private_attr_info())
# print(obj.attr)
# obj.attr = 'new value'
# print(obj.attr)
# obj.__private_attr = 'NEW VALUE'
# print(obj.get_private_attr_info())
# print(obj.__private_attr)
# obj.set_private_attr('NEW VALUE')
# print(obj.get_private_attr_info())



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



# class Geek:
#     def __init__(self, age=0):
#         self.__age = age

#     def get_age(self):
#         return self.__age

#     def set_age(self, x):
#         self.__age = x

# obj = Geek()
# obj.set_age(30)
# print(obj.get_age())


# class Geek:

#     def __init__(self):
#         self.__age = 0
#     @property
#     def age(self):
#         print('getter method called')
#         return self.__age

#     @age.setter
#     def age(self, new_age):
#         if new_age < 18:
#             raise ValueError('Sorry ur age is bellow eligibility criteria')
#         print('setter method called')
#         self.__age = new_age


# obj = Geek()
# obj.age = 8
# print(obj.age)


# from hashlib import new


# class Person:
#     def __init__(self, name, hours, per_hour):
#         self.name = name 
#         self.hours = hours 
#         self._per_hour = per_hour

#     @property
#     def salary(self):
#         try:
#             return self.__salary
#         except:
#             self.__salary = self.hours * self._per_hour
#             return self.__salary

#     @salary.setter
#     def salary(self, new_salary):
#         self.__salary = new_salary


# person1 = Person('Tom', 30 , 15)
# print(person1.salary)

# person1.salary = 9000
# print(person1.salary)

# @staticmethod - decorator kotoryi pomogaet
#  ispolzovat' method vnutri klassa, kotoryi mojet ne prinimat' self(to est' sam obj)

# @abstractmethod --- decorator kotoryi pomogaet sozdat' abstraktnyi metod, kotoyi v poslednuushem 
#  obyazatelno doljen but pereopredelen v dochernih klassah  v protivnom sluchae vyvodit oshibky

# @property -- pomogaet vzaimodeistvovat' s zashishennymi/privatnymi atributami, prevrashyaet metod getter v attribut
#  (pozvolyaet vzaimodeistvovat' s zashishennam atributom cherez setter metod, vyzyvaya ege kak attribut)
# 
# 
# # @name.setter ---  pohoj na property pozvolyaet ustanovit' znachenie zashishennommu attributu

# @classmethod--  decorator kotoryi pozvolyaet sdelat' obychnyi metod metodom klassa ,
#  logika kotorogo budet vliyat' na ves' klass v celom, po suti eto obyjnyi metod klassa, 
# kotoryi imeeet dostup ko vsem attributam klassa, cherez kotoryi on byl sozdan, eto metod, 
# kotoryi privyazan k klassu, a ne k exemplyaru klassa(objektu ot klassa)


# from datetime import date

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age 


#     @classmethod
#     def from_birth_year(cls, name, year):
#         return cls(name, date.today().year - year)

# obj_1 = Person('Tom', 30)
# print(obj_1.age)
# obj_2 = Person.from_birth_year('Helen', 1995)
# print(obj_2.age)


class Post:
    # posts = [
    #     {
    #         'title': 'title', 
    #         'author': 'author'
    #     }
    # ]

    posts = []

    def __init__(self,title, author):
        self.title = title
        self.author = author
        self.comments = []
        self._add_to_posts()
    
    @classmethod
    def _generate_id(cls):
        import random
        id_ =random.randint(100, 999)
        for post in cls.posts:
            if id_ == post.get('id'):
                return cls._generate_id()
        return id_

    def _add_to_posts(self):
        post = {
            'id': Post._generate_id(),
            'title': self.title,
            'author': self.author
        }
        Post.posts.append(post)
    
    def get_all_post(self):
        for post in self.posts:
            print(post)
        
    def add_comments(self, comment):
        self.comments.append(comment)
        print('COMMENT ADDED!!!')

    @property
    def comments_count(self):
        return len(self.comments)

post1 = Post('Python', 'Jack')
post1.add_comments('good post, idiot')
post1.add_comments('good post, idiot and bitch')
print(post1.comments_count)
post2 = Post('python', 'kot')
post2.add_comments('HTML is parasha')
print(post2.comments_count)
# post1.get_all_post()